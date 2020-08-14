#!/usr/bin/python
# Classification (U)

"""Program:  mongo_dump.py

    Description:  Unit testing of mongo_dump in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/mongo_dump.py

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

    Super-Class:

    Sub-Classes:

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_log_file -> Test with log file with data.
        test_empty_log -> Test with nothing written to log file.
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
        self.dir_path = "./test/unit/mongo_db_dump/tmp"
        self.args_array = {"-o": "./test/unit/mongo_db_dump/tmp",
                           "-p": "DirectoryPath2"}

    @mock.patch("mongo_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_log_file(self, mock_cmd, mock_subp):

        """Function:  test_log_file

        Description:  Test with log file with data.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual((mongo_db_dump.mongo_dump(
            self.server, self.args_array)), (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_empty_log(self, mock_cmd, mock_subp):

        """Function:  test_empty_log

        Description:  Test with nothing written to log file.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual((mongo_db_dump.mongo_dump(
            self.server, self.args_array)), (False, None))

    @mock.patch("mongo_db_dump.subprocess.Popen")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_db_dump(self, mock_cmd, mock_subp):

        """Function:  test_db_dump

        Description:  Test with database dump successful.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_subp.return_value = self.subp

        self.assertEqual((mongo_db_dump.mongo_dump(
            self.server, self.args_array)), (False, None))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of testing environment.

        Arguments:

        """

        f_list = gen_libs.list_filter_files(self.dir_path, "dump_log_file_*")

        if f_list:
            for line in f_list:
                os.remove(line)


if __name__ == "__main__":
    unittest.main()
