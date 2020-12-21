#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_dump
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__ -> Class initialization.
        add_2_msg -> Stub method holder for Mail.add_2_msg.
        send_mail -> Stub method holder for Mail.send_mail.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:
            (input) data -> Message line to add to email body.

        """

        self.data = data

        return True

    def send_mail(self):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class SubProcess(object):

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__ -> Initialize configuration environment.
        wait -> subprocess.wait method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

        pass

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """

        pass


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.
        lock_db -> Stub holder for mongo_class.Server.lock_db method.
        is_locked -> Stub holder for mongo_class.Server.is_locked method.
        unlock_db -> Stub holder for mongo_class.Server.unlock_db method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_path = "Database_Directory_Path"
        self.locked = False

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

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_log_file -> Test with passed in log name.
        test_mail_log_suppress -> Test with log file and mail and suppression.
        test_log_file_suppress -> Test with log file with data and suppression.
        test_empty_log_mail -> Test with nothing written to log file and mail.
        test_mail_log_file -> Test with log file and mail.
        test_log_file -> Test with log file with data.
        test_empty_log -> Test with nothing written to log file.
        test_export -> Test with database export successful.
        test_db_dump -> Test with database dump successful.
        tearDown -> Cleanup of testing environment.

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
        self.args_array = {"-p": "DirectoryPath2"}
        self.args_array2 = {"-p": "DirectoryPath2", "-x": True}
        self.file_list = ["2020-08-14T14:31:12 writing sysmon.mysql_perf to",
                          "2020-08-14T14:31:12 writing sysmon.mongo_rep to"]

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_log_file(self, mock_cmd, mock_subp):

        """Function:  test_log_file

        Description:  Test with passed in log name.

        Arguments:

        """

        mock_cmd.return_value = "ExportCommand"
        mock_subp.return_value = self.subp

        self.assertEqual((mongo_db_dump.mongo_generic(
            self.server, self.args_array, self.cmd_name2, self.log_file)),
                         (False, None))

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
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
            self.assertEqual((mongo_db_dump.mongo_generic(
                self.server, self.args_array2, self.cmd_name, self.log_file,
                mail=self.mail)), (False, None))

        self.assertEqual(self.mail.data, self.file_list[1])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
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

        self.assertEqual((mongo_db_dump.mongo_generic(
            self.server, self.args_array2, self.cmd_name, self.log_file)),
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

        self.assertEqual((mongo_db_dump.mongo_generic(
            self.server, self.args_array, self.cmd_name, self.log_file,
            mail=self.mail)), (False, None))

        self.assertEqual(self.mail.data, None)

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
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
            self.assertEqual((mongo_db_dump.mongo_generic(
                self.server, self.args_array, self.cmd_name, self.log_file,
                mail=self.mail)), (False, None))

        self.assertEqual(self.mail.data, self.file_list[1])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
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
            self.assertEqual((mongo_db_dump.mongo_generic(
                self.server, self.args_array, self.cmd_name, self.log_file)),
                             (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_empty_log(self, mock_cmd, mock_subp):

        """Function:  test_empty_log

        Description:  Test with nothing written to log file.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual((mongo_db_dump.mongo_generic(
            self.server, self.args_array, self.cmd_name, self.log_file)),
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

        self.assertEqual((mongo_db_dump.mongo_generic(
            self.server, self.args_array, self.cmd_name2, self.log_file)),
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

        self.assertEqual((mongo_db_dump.mongo_generic(
            self.server, self.args_array, self.cmd_name, self.log_file)),
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
