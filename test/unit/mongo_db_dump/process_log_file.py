# Classification (U)

"""Program:  process_log_file.py

    Description:  Unit testing of process_log_file in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/process_log_file.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_suppress
        test_mail_log_suppress
        test_log_file_suppress
        test_mail_log_file
        test_log_file
        test_empty_log
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.dir_path = "./test/unit/mongo_db_dump/tmp"
        self.log_file = self.dir_path + "/log_file"
        self.file_list = ["2020-08-14T14:31:12 writing sysmon.mysql_perf to",
                          "2020-08-14T14:31:12 writing sysmon.mongo_rep to"]

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    def test_no_suppress(self, mock_file):

        """Function:  test_no_suppress

        Description:  Test with no standard out suppression.

        Arguments:

        """

        mock_file.return_value = self.file_list

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_dump.process_log_file(self.log_file, False, None))

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    def test_mail_log_suppress(self, mock_file):

        """Function:  test_mail_log_suppress

        Description:  Test with log file and mail and suppression.

        Arguments:

        """

        mock_file.return_value = self.file_list

        mongo_db_dump.process_log_file(self.log_file, True, self.mail)

        self.assertEqual(self.mail.msg, self.file_list[1])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    def test_log_file_suppress(self, mock_file):

        """Function:  test_log_file_suppress

        Description:  Test with log file with data and suppression.

        Arguments:

        """

        mock_file.return_value = self.file_list

        self.assertFalse(
            mongo_db_dump.process_log_file(self.log_file, True, None))

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    def test_mail_log_file(self, mock_file):

        """Function:  test_mail_log_file

        Description:  Test with log file and mail.

        Arguments:

        """

        mock_file.return_value = self.file_list

        mongo_db_dump.process_log_file(self.log_file, True, self.mail)

        self.assertEqual(self.mail.msg, self.file_list[1])

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_dump.gen_libs.file_2_list")
    def test_log_file(self, mock_file):

        """Function:  test_log_file

        Description:  Test with log file with data.

        Arguments:

        """

        mock_file.return_value = self.file_list

        self.assertFalse(
            mongo_db_dump.process_log_file(self.log_file, True, None))

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=True))
    def test_empty_log(self):

        """Function:  test_empty_log

        Description:  Test with nothing written to log file.

        Arguments:

        """

        self.assertFalse(
            mongo_db_dump.process_log_file(self.log_file, True, None))


if __name__ == "__main__":
    unittest.main()
