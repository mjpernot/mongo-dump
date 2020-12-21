#!/usr/bin/python
# Classification (U)

"""Program:  mongo_db_dump.py

    Description:  The mongo_db_dump program runs dumps against a Mongo database
        and depending on which type of dump is selected can dump individual
        databases.

    Usage:
        mongo_db_dump.py -c file -d path
            {-M -o dir_path [-z | -b database [-r | -t name] | -l | -q | -z] |
             -A -o dir_path}
            [-p path | -y flavor_id | -x]
            [-e email {email2 email3 ...} {-s subject_line}]
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir_path => Directory path to config file (-c). Required arg.
        -p dir path => Directory path to mongo programs.
            Only needed if the mongo binary programs do not run properly.
            (i.e. not in the $PATH variable.)

        -M => Run the mongodump program.
            -z => Compress database dump.  Only for -M option.
            -l => Oplog option added to mongodump. Only for -M option.
            -b database => Database name. Only for -M option.
            -t table => Collection name. Only available for -b option.
            -r => Include user and roles in dump. Only available for -b option.
            -q => Turn quiet mode on. By default, displays out log of dump.
            -o dir_path => Directory path to dump directory. Required argument
                for option.

        -A => Run the Sync/Copy dump program. Database server being dumped must
                also be part of a replica set.
            -o dir_path => Directory path to dump directory. Required argument
                for option.

        -e email_address(es) => Send output to one or more email addresses.
        -s subject_line => Subject line of email.
            Requires -e option.
        -y value => A flavor id for the program lock.  To create unique lock.
        -x => Suppress standard out.
        -v => Display version of this program.
        -h => Help and usage message.
            NOTE 1:  -v or -h overrides the other options.
            NOTE 2:  -A and -M are Xor required arguments.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format for the Mongo connection used for
            dumping data from a database.  Leave the Mongo replica set entries
            set to None as it is not required for dumping purposes.

            Configuration file for Mongo Database Server connection.
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOSTNAME"
            port = 27017
            conf_file = None
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"
            use_arg = True
            use_uri = False

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_db_dump.py c mongo -d config -o /db_dump -z -M -l

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import datetime
import subprocess

# Third-party

# Local
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import lib.arg_parser as arg_parser
import mongo_lib.mongo_class as mongo_class
import mongo_lib.mongo_libs as mongo_libs
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def sync_cp_dump(server, args_array, **kwargs):

    """Function:  sync_cp_dump

    Description:  Locks the database and then copies the database files to a
        destination directory.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (output) err_flag -> True|False - If an error has occurred.
        (output) err_msg -> Error message.
        (input) **kwargs:
            mail -> Email class instance.

    """

    args_array = dict(args_array)
    err_flag = False
    err_msg = None
    mail = kwargs.get("mail", None)

    if not (server.is_locked()):
        server.lock_db(lock=True)

        if (server.is_locked()):
            dmp_dir = args_array["-o"] + "/cp_dump_" \
                + datetime.datetime.strftime(datetime.datetime.now(),
                                             "%Y%m%d_%H%M")

            # Backup database.
            shutil.copytree(server.db_path, dmp_dir)
            server.unlock_db()

            if (server.is_locked()):
                err_flag = True
                err_msg = "Warning:  Database still locked after dump."

        else:
            err_flag = True
            err_msg = "Error:  Unable to lock the database for dump to occur."

    else:
        err_flag = True
        err_msg = "Error:  Database previously locked, unable to dump."

    if mail and err_flag:
        mail.add_2_msg("Error/Warning detected in database dump.")
        mail.add_2_msg(err_msg)
        mail.send_mail()

    return err_flag, err_msg


def mongo_dump(server, args_array, **kwargs):

    """Function:  mongo_dump

    Description:  Create the dump command and execute it.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
            mail -> Email class instance.
            req_arg -> List of required options for the command line.
        (output) err_flag -> If an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    subp = gen_libs.get_inst(subprocess)
    args_array = dict(args_array)
    mail = kwargs.get("mail", None)
    sup_std = args_array.get("-x", False)
    dtg = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
    f_name = os.path.join(args_array["-o"], "dump_log_file_" + dtg + ".log")
    dump_cmd = mongo_libs.create_cmd(
        server, args_array, "mongodump",
        arg_parser.arg_set_path(args_array, "-p"), **kwargs)

    with open(f_name, "w") as l_file:
        proc1 = subp.Popen(dump_cmd, stderr=l_file)
        proc1.wait()

    if not gen_libs.is_empty_file(f_name):
        log_list = gen_libs.file_2_list(f_name)

        for line in log_list:
            if not sup_std:
                print(line)

            if mail:
                mail.add_2_msg(line)

        if mail:
            mail.send_mail()

    return err_flag, err_msg


def mongo_generic(server, args_array, cmd_name, log_file, **kwargs):

    """Function:  mongo_generic

    Description:  Create a mongo dump/export command and execute it.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) cmd_name -> Name of Mongo binary program to execute.
        (input) log_file -> Directory path and file name for log.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
            req_arg -> List of required options for the command line.
            mail -> Email class instance.
        (output) err_flag -> If an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    subp = gen_libs.get_inst(subprocess)
    args_array = dict(args_array)
    mail = kwargs.get("mail", None)
    sup_std = args_array.get("-x", False)

    cmd = mongo_libs.create_cmd(
        server, args_array, cmd_name,
        arg_parser.arg_set_path(args_array, "-p"), **kwargs)

    with open(log_file, "w") as l_file:
        proc1 = subp.Popen(cmd, stderr=l_file)
        proc1.wait()

    if not gen_libs.is_empty_file(log_file):
        log_list = gen_libs.file_2_list(log_file)

        for line in log_list:
            if not sup_std:
                print(line)

            if mail:
                mail.add_2_msg(line)

        if mail:
            mail.send_mail()

    return err_flag, err_msg


def mongo_export(server, args_array, **kwargs):

    """Function:  mongo_export

    Description:  Setup Mongo Export call.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
            req_arg -> List of required options for the command line.
            mail -> Email class instance.
        (output) err_flag -> If an error has occurred.
        (output) err_msg -> Error message.

    """

    log_name = "export_"
    args_array = dict(args_array)
    err_flag = False
    err_msg = None
    opt_name = args_array["-b"] + "_" + args_array["-t"]
    dtg = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")

    if "-o" in args_array.keys() and args_array["-o"]:
        log_file = os.path.join(
            args_array["-o"], log_name + opt_name + "_" + dtg + ".log")
        args_array["-o"] = os.path.join(
            args_array["-o"], log_name + opt_name + ".json")
        err_flag, err_msg = mongo_generic(
            server, args_array, "mongoexport", log_file, **kwargs)

    else:
        err_flag = True
        err_msg = "Error:  Missing -o option or value."

    return err_flag, err_msg


def get_req_options(server, arg_req_dict, **kwargs):

    """Function:  get_req_options

    Description:  Assigns configuration entry values to required options.  If
        the entry is not set (e.g. None), then the option is skipped.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Dict of command line options and values.
        (output) arg_rep -> List of required options with values.

    """

    arg_req_dict = dict(arg_req_dict)

    arg_req = [arg_req_dict[item] + getattr(server, item)
               for item in arg_req_dict.keys()
               if hasattr(server, item) and getattr(server, item)]

    return arg_req


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
            arg_req_dict -> contains link between config and required option.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    arg_req_dict = dict(kwargs.get("arg_req_dict", {}))
    mail = None
    server = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mongo_class.Server)
    status = server.connect()

    if status[0]:
        req_arg = get_req_options(server, arg_req_dict)

        if args_array.get("-e", False):
            dtg = datetime.datetime.strftime(datetime.datetime.now(),
                                             "%Y%m%d_%H%M%S")
            subj = args_array.get("-s",
                                  [server.name, ": mongo_db_dump: ", dtg])
            mail = gen_class.setup_mail(args_array.get("-e"), subj=subj)

        # Intersect args_array and func_dict to decide which functions to call.
        for item in set(args_array.keys()) & set(func_dict.keys()):
            err_flag, err_msg = func_dict[item](server, args_array, mail=mail,
                                                req_arg=req_arg, **kwargs)

            if err_flag:
                print(err_msg)
                break

        mongo_libs.disconnect([server])

    else:
        print("Connection failure:  %s" % (status[1]))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        arg_req_dict -> contains link between config entry and required option.
        dir_chk_list -> contains options which will be directories.
        dir_crt_list -> contain options that require directory to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_arg_list -> contains optional arguments for the command line.
        opt_con_req_list -> contains the options that require other options.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        opt_xor_dict -> contains dict with key that is xor with it's values.
        xor_noreq_list -> contains options that are XOR, but are not required.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    arg_req_dict = {"auth_db": "--authenticationDatabase="}
    dir_chk_list = ["-d", "-o", "-p"]
    dir_crt_list = ["-o"]
    func_dict = {"-A": sync_cp_dump, "-M": mongo_dump, "-E": mongo_export}
    opt_arg_list = {"-l": "--oplog", "-z": "--gzip", "-b": "--db=",
                    "-o": "--out=", "-q": "--quiet",
                    "-r": "--dumpDbUsersAndRoles", "-t": "--collection="}
    opt_con_req_list = {"-r": ["-b"], "-t": ["-b"], "-s": ["-e"],
                        "-E": ["-b", "-t"]}
    opt_multi_list = ["-e", "-s"]
    opt_req_list = ["-c", "-d", "-o"]
    opt_val_list = ["-b", "-c", "-d", "-o", "-p", "-t", "-e", "-s", "-y"]
    opt_xor_dict = {"-A": ["-M", "-E"], "-E": ["-M", "-A"], "-M": ["-A", "-E"]}
    xor_noreq_list = {"-l": "-b"}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
       and arg_parser.arg_noreq_xor(args_array, xor_noreq_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list,
                                          dir_crt_list):

        try:
            prog_lock = gen_class.ProgramLock(cmdline.argv,
                                              args_array.get("-y", ""))
            run_program(args_array, func_dict, opt_arg=opt_arg_list,
                        arg_req_dict=arg_req_dict)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("WARNING:  Lock in place for mongo_db_dump with id: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())
