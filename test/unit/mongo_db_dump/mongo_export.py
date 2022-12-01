# Classification (U)

"""Program:  mongo_export.py

    Description:  Unit testing of mongo_export in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/mongo_export.py

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
import version

__version__ = version.__version__


class Server(object):

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
        setUp
        test_missing_value
        test_missing_option
        test_failure
        test_mongo_export

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-b": "Database_Name", "-t": "Table_Name",
                           "-o": "/directory/path"}
        self.args_array2 = {"-b": "Database_Name", "-t": "Table_Name"}
        self.args_array3 = {"-b": "Database_Name", "-t": "Table_Name",
                            "-o": None}

    def test_missing_value(self):

        """Function:  test_missing_value

        Description:  Test with missing -o value.

        Arguments:

        """

        self.assertEqual(
            (mongo_db_dump.mongo_export(self.server, self.args_array3)),
            (True, "Error:  Missing -o option or value."))

    def test_missing_option(self):

        """Function:  test_missing_option

        Description:  Test with missing -o option.

        Arguments:

        """

        self.assertEqual(
            (mongo_db_dump.mongo_export(self.server, self.args_array2)),
            (True, "Error:  Missing -o option or value."))

    @mock.patch("mongo_db_dump.mongo_generic")
    def test_failure(self, mock_cmd):

        """Function:  test_failure

        Description:  Test with failure of mongo export.

        Arguments:

        """

        mock_cmd.return_value = (True, "Error Message")

        self.assertEqual((mongo_db_dump.mongo_export(
            self.server, self.args_array)), (True, "Error Message"))

    @mock.patch("mongo_db_dump.mongo_generic")
    def test_mongo_export(self, mock_cmd):

        """Function:  test_mongo_export

        Description:  Test with mongo export call.

        Arguments:

        """

        mock_cmd.return_value = (False, None)

        self.assertEqual((mongo_db_dump.mongo_export(
            self.server, self.args_array)), (False, None))


if __name__ == "__main__":
    unittest.main()
