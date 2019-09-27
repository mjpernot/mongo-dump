#!/usr/bin/python
# Classification (U)

"""Program:  mongo_db_dump.py

    Description:  The mongo_db_dump program runs dumps against a Mongo database
        and depending on which type of dump is selected can dump individual
        databases.

    Usage:
        mongo_db_dump.py -c file -d path {-M [-z | -b name [-r | -t name] |
            -l] | -A} [-o name | -p path | -s | -z | -q] [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -o dir path => Directory path to dump directory.
        -p dir path => Directory path to mongo programs.  Only required if the
            mongo binary programs do not run properly.  (i.e. not in the $PATH
            variable.)
        -M => Run the mongodump program.
        -A => Run the Sync/Copy dump program.
            NOTE:  -A and -M are XOR required arguments.
        -z => Compress database dump.  Only for -M option.
        -l => Oplog option added to mongodump.  Only for -M option and
            database must also be part of a replica set.
        -b database => Database name.  Only for -M option.
        -t table => Collection name.  Only available for -b.
        -a database => Name of authenication database.  Required for -b.
        -r => Include user and roles in dump.  Only available for -b.
        -q => Turn quiet mode on.  By default, displays out log of dump.
        -v => Display version of this program.
        -h => Help and usage message.
            NOTE:  -v or -h overrides the other options.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_db_dump.py -a -c mongo -d config -o /db_dump -z -M -l

"""

# Libraries and Global Variables

# Standard
import sys
import shutil
import datetime

# Local
import lib.gen_libs as gen_libs
import lib.arg_parser as arg_parser
import lib.cmds_gen as cmds_gen
import mongo_lib.mongo_class as mongo_class
import mongo_lib.mongo_libs as mongo_libs
import version

# Version
__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def sync_cp_dump(SERVER, args_array, **kwargs):

    """Function:  sync_cp_dump

    Description:  Locks the database and then copies the database files to a
        destination directory.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            None
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None

    if not (SERVER.is_locked()):
        SERVER.lock_db(lock=True)

        if (SERVER.is_locked()):
            dmp_dir = args_array["-o"] + "/cp_dump_" \
                + datetime.datetime.strftime(datetime.datetime.now(),
                                             "%Y%m%d_%H%M")

            # Backup database.
            shutil.copytree(SERVER.db_path, dmp_dir)

            SERVER.unlock_db()

            if (SERVER.is_locked()):
                err_flag = True
                err_msg = "Warning:  Database still locked after dump."

        else:
            err_flag = True
            err_msg = "Error:  Unable to lock the database for dump to occur."

    else:
        err_flag = True
        err_msg = "Error:  Database previously locked, unable to dump."

    return err_flag, err_msg


def mongo_dump(SERVER, args_array, **kwargs):

    """Function:  mongo_dump

    Description:  Create the dump command and execute it.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
        (output) True|False -> if an error has occurred.
        (output) -> Error message.

    """

    dump_cmd = mongo_libs.create_cmd(SERVER, args_array, "mongodump",
                                     arg_parser.arg_set_path(args_array, "-p"),
                                     **kwargs)
    cmds_gen.run_prog(dump_cmd)

    return False, None


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add

    """

    SERVER = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mongo_class.Server)
    SERVER.connect()

    # Intersect args_array and func_dict to determine which functions to call.
    for x in set(args_array.keys()) & set(func_dict.keys()):
        err_flag, err_msg = func_dict[x](SERVER, args_array, **kwargs)

        if err_flag:
            print(err_msg)
            break

    cmds_gen.disconnect([SERVER])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        dir_crt_list -> contain options that require directory to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_arg_list -> contains optional arguments for the command line.
        opt_con_req_list -> contains the options that require other options.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        xor_noreq_list -> contains options that are XOR, but are not required.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d", "-o", "-p"]
    dir_crt_list = ["-o"]
    func_dict = {"-A": sync_cp_dump, "-M": mongo_dump}
    opt_arg_list = {"-l": "--oplog", "-z": "--gzip", "-b": "--db=",
                    "-o": "--out=", "-a": "--authenticationDatabase=",
                    "-q": "--quiet", "-r": "--dumpDbUsersAndRoles",
                    "-t": "--collection="}
    opt_con_req_list = {"-A": ["-o"], "-b": ["-a"], "-r": ["-b"], "-t": ["-b"]}
    opt_req_list = ["-c", "-d"]
    opt_req_xor_list = {"-A": "-M"}
    opt_val_list = ["-a", "-b", "-c", "-d", "-o", "-p", "-t"]
    xor_noreq_list = {"-l": "-b"}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if not arg_parser.arg_require(args_array, opt_req_list) \
           and arg_parser.arg_req_xor(args_array, opt_req_xor_list) \
           and arg_parser.arg_noreq_xor(args_array, xor_noreq_list) \
           and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list,
                                              dir_crt_list):
            run_program(args_array, func_dict, opt_arg=opt_arg_list)


if __name__ == "__main__":
    sys.exit(main())