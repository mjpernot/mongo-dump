#!/bin/sh
# Classification (U)

# Shell commands follow
# Next line is bilingual: it starts a comment in Python & is a no-op in shell
""":"

# Find a suitable python interpreter (can adapt for specific needs)
# NOTE: Ignore this section if passing the -h option to the program.
#   This code must be included in the program's initial docstring.
for cmd in python3.12 python3.9 ; do
   command -v > /dev/null $cmd && exec $cmd $0 "$@"
done

echo "OMG Python not found, exiting...."

exit 2

# Previous line is bilingual: it ends a comment in Python & is a no-op in shell
# Shell commands end here


   Program:  mongo_db_dump.py

    Description:  The mongo_db_dump program runs dumps against a Mongo database
        and depending on which type of dump is selected can dump individual
        databases.

    Usage:
        mongo_db_dump.py -c file -d path
            {-M -o dir_path [-z | -b database [-r | -t name] | -l | -q | -z |
                -i ] |
             -A -o dir_path |
             -E -o dir_path -b database -t name [-q]}
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
            -z => Compress database dump.
            -l => Oplog option added to mongodump.
            -b database => Database name.
                -t table => Collection name.
                    -r => Include user and roles in dump.
            -q => Turn quiet mode on. By default, displays out log of dump.
            -o dir_path => Directory path to dump directory. Required argument.
            -i => Turn off TLS checking.

        -A => Run the Sync/Copy dump program. Database server being dumped must
                also be part of a replica set.
            -o dir_path => Directory path to dump directory. Required argument.

        -E => Run the mongoexport program.
            -b database => Database name.
                -t table => Collection name.
            -q => Turn quiet mode on. By default, displays out log of dump.
            -o dir_path => Directory path to dump directory. Required argument.

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
            dumping data from a database.

        Leave the Mongo replica set entries set to None as it is not required
            for dumping purposes.

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

        If Mongo is set to use TLS or SSL connections, then one or more of the
            following entries will need to be completed to connect using TLS or
            SSL protocols.
            Note:  Read the configuration file to determine which entries will
                need to be set.

            SSL:
                auth_type = None
                ssl_client_ca = None
                ssl_client_key = None
                ssl_client_cert = None
                ssl_client_phrase = None
            TLS:
                auth_type = None
                tls_ca_certs = None
                tls_certkey = None
                tls_certkey_phrase = None

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

        A log file and error file (if any errors are detected) will be
            written to the same directory as the dump file (-o option).

            Note:  If the -q option is used on the command line, then there
                will be no log entries in the log file of the dump.
                To include the log entries, but still have nothing displayed
                to standard out, then use the "1>/dev/null" after the dump
                command on the command line.  See example 2 below.

    Example 1:
        mongo_db_dump.py c mongo -d config -o /db_dump -z -M -l

    Example 2: Send log entries to file, but have nothing displayed to stdout.
        mongo_db_dump.py c mongo -d config -o /db_dump -z -M -l 1>/dev/null

":"""
# Python program follows


# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import datetime
import subprocess

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mongo_lib import mongo_libs
    from .mongo_lib import mongo_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import mongo_lib.mongo_libs as mongo_libs           # pylint:disable=R0402
    import mongo_lib.mongo_class as mongo_class         # pylint:disable=R0402
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def sync_cp_dump(server, args, **kwargs):

    """Function:  sync_cp_dump

    Description:  Locks the database and then copies the database files to a
        destination directory.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) err_flag -> True|False - If an error has occurred
        (output) err_msg -> Error message
        (input) **kwargs:
            mail -> Email class instance

    """

    err_flag = False
    err_msg = None
    mail = kwargs.get("mail", None)

    if not server.is_locked():
        server.lock_db(lock=True)

        if server.is_locked():
            dmp_dir = args.get_val("-o") + "/cp_dump_" \
                + datetime.datetime.strftime(
                    datetime.datetime.now(), "%Y%m%d_%H%M")

            # Backup database.
            shutil.copytree(server.db_path, dmp_dir)
            server.unlock_db()

            if server.is_locked():
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


def mongo_dump(server, args, **kwargs):

    """Function:  mongo_dump

    Description:  Create the dump command and execute it.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add
            mail -> Email class instance
            req_arg -> List of required options for the command line
        (output) err_flag -> If an error has occurred
        (output) err_msg -> Error message

    """

    log_name = "dump_"
    err_flag = False
    err_msg = None
    dtg = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")

    if args.arg_exist("-o") and args.get_val("-o"):
        log_file = os.path.join(args.get_val("-o"), log_name + dtg + ".log")
        err_file = os.path.join(args.get_val("-o"), log_name + dtg + ".err")
        err_flag, err_msg = mongo_generic(
            server, args, "mongodump", log_file, err_file=err_file, **kwargs)

    else:
        err_flag = True
        err_msg = "Error:  Missing -o option or value."

    return err_flag, err_msg


def mongo_generic(                                      # pylint:disable=R0914
        server, args, cmd_name, log_file, **kwargs):

    """Function:  mongo_generic

    Description:  Create a mongo dump/export command and execute it.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (input) cmd_name -> Name of Mongo binary program to execute
        (input) log_file -> Directory path and file name for log file
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add
            req_arg -> List of required options for the command line
            mail -> Email class instance
            err_file -> Directory path and file name for error file
        (output) err_flag -> If an error has occurred
        (output) err_msg -> Error message

    """

    err_flag = False
    err_msg = None
    mail = kwargs.get("mail", None)
    err_file = kwargs.get("err_file", log_file + ".err")
    e_file = open(                                      # pylint:disable=R1732
        err_file, mode="w", encoding="UTF-8")
    cmd = mongo_libs.create_cmd(
        server, args, cmd_name, "-p", no_pass=True, **kwargs)
    proc2 = subprocess.Popen(                           # pylint:disable=R1732
        ["echo", server.japd], stdout=subprocess.PIPE)

    with open(log_file, mode="w", encoding="UTF-8") as l_file:
        proc1 = subprocess.Popen(                       # pylint:disable=R1732
            cmd, stderr=l_file, stdin=proc2.stdout, stdout=e_file)
        proc1.wait()

    e_file.close()
    process_log_file(log_file, args.arg_exist("-x"), mail)

    if gen_libs.is_empty_file(err_file):
        gen_libs.rm_file(err_file)

    else:
        err_list = gen_libs.file_2_list(err_file)
        err_flag = True
        err_msg = f"Error detected in error file: {err_file}"

        if mail:
            mail.add_2_msg("Error messages detected during dump:")

        for line in err_list:
            print(line)

            if mail:
                mail.add_2_msg(line)

    if mail and mail.msg:
        mail.send_mail()

    return err_flag, err_msg


def process_log_file(log_file, sup_std, mail):

    """Function:  process_log_file

    Description:  Checks and processes the log file to standard out and mail.

    Arguments:
        (input) log_file -> Directory path and file name for log file
        (input) sup_std -> True|False -Suppress standard out
        (input) mail -> Email class instance

    """

    if not gen_libs.is_empty_file(log_file):
        log_list = gen_libs.file_2_list(log_file)

        if not sup_std:
            for line in log_list:
                print(line)

        if mail:
            for line in log_list:
                mail.add_2_msg(line)


def mongo_export(server, args, **kwargs):

    """Function:  mongo_export

    Description:  Setup Mongo Export call.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add
            req_arg -> List of required options for the command line
            mail -> Email class instance
        (output) err_flag -> If an error has occurred
        (output) err_msg -> Error message

    """

    log_name = "export_"
    err_flag = False
    err_msg = None
    opt_name = args.get_val("-b") + "_" + args.get_val("-t")
    dtg = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")

    if "-o" in list(args.get_args_keys()) and args.get_val("-o"):
        log_file = os.path.join(
            args.get_val("-o"), log_name + opt_name + "_" + dtg + ".log")
        err_file = os.path.join(
            args.get_val("-o"), log_name + opt_name + "_" + dtg + ".err")
        args.update_arg("-o", os.path.join(
            args.get_val("-o"), log_name + opt_name + ".json"))
        err_flag, err_msg = mongo_generic(
            server, args, "mongoexport", log_file, err_file=err_file, **kwargs)

    else:
        err_flag = True
        err_msg = "Error:  Missing -o option or value."

    return err_flag, err_msg


def get_req_options(server, arg_req_dict):

    """Function:  get_req_options

    Description:  Assigns configuration entry values to required options.  If
        the entry is not set (e.g. None), then the option is skipped.

    Arguments:
        (input) server -> Database server instance
        (input) arg_req_dict -> Contains dictionary of config and required
            option
        (output) arg_rep -> List of required options with values

    """

    arg_req_dict = dict(arg_req_dict)

    arg_req = [arg_req_dict[item] + getattr(server, item)
               for item in list(arg_req_dict.keys())
               if hasattr(server, item) and getattr(server, item)]

    return arg_req


def run_program(args, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add
            arg_req_dict -> contains link between config and required option

    """

    func_dict = dict(func_dict)
    arg_req_dict = dict(kwargs.get("arg_req_dict", {}))
    mail = None
    server = mongo_libs.create_instance(
        args.get_val("-c"), args.get_val("-d"), mongo_class.Server)
    status = server.connect()

    if status[0]:
        req_arg = get_req_options(server, arg_req_dict)

        if args.arg_exist("-e"):
            dtg = datetime.datetime.strftime(
                datetime.datetime.now(), "%Y%m%d_%H%M%S")
            subj = args.get_val(
                "-s", def_val=[server.name, ": mongo_db_dump: ", dtg])
            mail = gen_class.setup_mail(args.get_val("-e"), subj=subj)

        # Intersect args_array and func_dict to decide which functions to call
        for item in set(args.get_args_keys()) & set(func_dict.keys()):
            err_flag, err_msg = func_dict[item](
                server, args, mail=mail, req_arg=req_arg, **kwargs)

            if err_flag:
                print(err_msg)
                break

        mongo_libs.disconnect([server])

    else:
        print(f"Connection failure:  {status[1]}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        arg_req_dict -> contains link between config entry and required option
        dir_perms_chk -> contains directories and their octal permissions
        dir_perms_crt -> contains directories to be created and their perms
        func_dict -> dictionary list for the function calls or other options
        opt_arg_list -> contains optional arguments for the command line
        opt_con_req_list -> contains the options that require other options
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values
        opt_xor_dict -> contains dict with key that is xor with it's values
        xor_noreq_list -> contains options that are XOR, but are not required

    Arguments:
        (input) argv -> Arguments from the command line

    """

    arg_req_dict = {"auth_db": "--authenticationDatabase="}
    dir_perms_chk = {"-d": 5, "-p": 5}
    dir_perms_crt = {"-o": 7}
    func_dict = {"-A": sync_cp_dump, "-M": mongo_dump, "-E": mongo_export}
    opt_arg_list = {
        "-l": "--oplog", "-z": "--gzip", "-b": "--db=", "-o": "--out=",
        "-q": "--quiet", "-i": "--tlsInsecure", "-r": "--dumpDbUsersAndRoles",
        "-t": "--collection="}
    opt_con_req_list = {
        "-r": ["-b"], "-t": ["-b"], "-s": ["-e"], "-E": ["-b", "-t"]}
    opt_multi_list = ["-e", "-s"]
    opt_req_list = ["-c", "-d", "-o"]
    opt_val_list = ["-b", "-c", "-d", "-o", "-p", "-t", "-e", "-s", "-y"]
    opt_xor_dict = {"-A": ["-M", "-E"], "-E": ["-M", "-A"], "-M": ["-A", "-E"]}
    xor_noreq_list = {"-l": "-b"}

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)                   \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)              \
       and args.arg_noreq_xor(xor_noreq=xor_noreq_list)             \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)          \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)            \
       and args.arg_dir_crt(dir_perms_crt=dir_perms_crt):

        try:
            prog_lock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args, func_dict, opt_arg=opt_arg_list,
                        arg_req_dict=arg_req_dict)
            del prog_lock

        except gen_class.SingleInstanceException:
            print(f'WARNING:  Lock in place for mongo_db_dump with id:'
                  f' {args.get_val("-y", def_val="")}')


if __name__ == "__main__":
    sys.exit(main())
