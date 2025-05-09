# Classification (U)

"""Program:  mongo_generic.py

    Description:  Unit testing of mongo_generic in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/mongo_generic.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_dump                            # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mongo_cfg", "-d": "config"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array


class Mail():

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.msg = ""

    def add_2_msg(self, line):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:
            (input) line -> Message line to add to email body.

        """

        self.msg = line

        return True

    def send_mail(self):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class SubProcess():

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        wait
        PIPE
        stdout

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

    def PIPE(self):                                     # pylint:disable=C0103

        """Method:  PIPE

        Description:  Mock representation of subprocess.PIPE method.

        Arguments:

        """

    def stdout(self):

        """Method:  stdout

        Description:  Mock representation of subprocess.stdout method.

        Arguments:

        """


class Server():

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        lock_db
        is_locked
        unlock_db

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_path = "Database_Directory_Path"
        self.locked = False
        self.japd = "JAPD"

    def lock_db(self, lock):

        """Method:  lock_db

        Description:  Stub holder for mongo_class.Server.lock_db method.

        Arguments:
            (input) lock -> True|False - Lock the database?

        """

        self.locked = lock

    def is_locked(self):

        """Method:  is_locked

        Description:  Stub holder for mongo_class.Server.is_locked method.

        Arguments:

        """

        return self.locked

    def unlock_db(self):

        """Method:  unlock_db

        Description:  Stub holder for mongo_class.Server.unlock_db method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mail_error_file
        test_error_file
        test_log_file2
        test_mail_log_suppress
        test_log_file_suppress
        test_empty_log_mail
        test_mail_log_file
        test_log_file
        test_empty_log
        test_export
        test_db_dump
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.subp = SubProcess()
        self.mail = Mail()
        self.cmd_name = "mongodump"
        self.cmd_name2 = "mongoexport"
        self.dir_path = "./test/unit/mongo_db_dump/tmp"
        self.log_file = self.dir_path + "/log_file"
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-p": "DirectoryPath2"}
        self.args2.args_array = {"-p": "DirectoryPath2", "-x": True}
        self.file_list = ["2020-08-14T14:31:12 writing sysmon.mysql_perf to",
                          "2020-08-14T14:31:12 writing sysmon.mongo_rep to"]
        self.file_list2 = ["Error detected in dump"]
        e_file = self.dir_path + "/log_file.err"
        self.msg = f"Error detected in error file: {e_file}"

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, False]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_mail_error_file2(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_mail_error_file2

        Description:  Test with error file with data and mail.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.side_effect = [self.file_list, self.file_list2]

        with gen_libs.no_std_out():
            mongo_db_dump.mongo_generic(
                self.server, self.args2, self.cmd_name, self.log_file,
                mail=self.mail)

        self.assertEqual(self.mail.msg, self.file_list2[0])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, False]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_mail_error_file(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_mail_error_file

        Description:  Test with error file with data and mail.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.side_effect = [self.file_list, self.file_list2]

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_dump.mongo_generic(
                    self.server, self.args2, self.cmd_name,
                    self.log_file, mail=self.mail), (True, self.msg))

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, False]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_error_file(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_error_file

        Description:  Test with error file with data.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.side_effect = [self.file_list, self.file_list2]

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_dump.mongo_generic(
                    self.server, self.args2, self.cmd_name,
                    self.log_file), (True, self.msg))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_log_file2(self, mock_cmd, mock_subp):

        """Function:  test_log_file2

        Description:  Test with passed in log name.

        Arguments:

        """

        mock_cmd.return_value = "ExportCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            mongo_db_dump.mongo_generic(
                self.server, self.args, self.cmd_name2, self.log_file),
            (False, None))

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, True]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_mail_log_suppress(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_mail_log_suppress

        Description:  Test with log file and mail and suppression.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.return_value = self.file_list

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_dump.mongo_generic(
                    self.server, self.args2, self.cmd_name,
                    self.log_file, mail=self.mail), (False, None))

        self.assertEqual(self.mail.msg, self.file_list[1])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, True]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_log_file_suppress(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_log_file_suppress

        Description:  Test with log file with data and suppression.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.return_value = self.file_list

        self.assertEqual(
            mongo_db_dump.mongo_generic(
                self.server, self.args2, self.cmd_name, self.log_file),
            (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_empty_log_mail(self, mock_cmd, mock_subp):

        """Function:  test_empty_log_mail

        Description:  Test with nothing written to log file and mail.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            mongo_db_dump.mongo_generic(
                self.server, self.args, self.cmd_name, self.log_file,
                mail=self.mail), (False, None))

        self.assertEqual(self.mail.msg, "")

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, True]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_mail_log_file(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_mail_log_file

        Description:  Test with log file and mail.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.return_value = self.file_list

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_dump.mongo_generic(
                    self.server, self.args, self.cmd_name, self.log_file,
                    mail=self.mail), (False, None))

        self.assertEqual(self.mail.msg, self.file_list[1])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(side_effect=[False, True]))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_log_file(self, mock_cmd, mock_subp, mock_file):

        """Function:  test_log_file

        Description:  Test with log file with data.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp
        mock_file.return_value = self.file_list

        with gen_libs.no_std_out():
            self.assertEqual(
                mongo_db_dump.mongo_generic(
                    self.server, self.args, self.cmd_name,
                    self.log_file), (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_empty_log(self, mock_cmd, mock_subp):

        """Function:  test_empty_log

        Description:  Test with nothing written to log file.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            mongo_db_dump.mongo_generic(
                self.server, self.args, self.cmd_name, self.log_file),
            (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_export(self, mock_cmd, mock_subp):

        """Function:  test_export

        Description:  Test with database export successful.

        Arguments:

        """

        mock_cmd.return_value = "ExportCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            mongo_db_dump.mongo_generic(
                self.server, self.args, self.cmd_name2, self.log_file),
            (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_db_dump(self, mock_cmd, mock_subp):

        """Function:  test_db_dump

        Description:  Test with database dump successful.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            (mongo_db_dump.mongo_generic(
                self.server, self.args, self.cmd_name, self.log_file)),
            (False, None))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of testing environment.

        Arguments:

        """

        f_list = gen_libs.list_filter_files(self.dir_path, "log_file*")

        if f_list:
            for line in f_list:
                os.remove(line)


if __name__ == "__main__":
    unittest.main()
