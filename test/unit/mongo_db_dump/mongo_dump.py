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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_dump                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

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

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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
        test_missing_value
        test_missing_option
        test_failure
        test_db_dump

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {
            "-b": "Database_Name", "-t": "Table_Name", "-o": "/directory/path"}
        self.args2.args_array = {"-b": "Database_Name", "-t": "Table_Name"}
        self.args3.args_array = {
            "-b": "Database_Name", "-t": "Table_Name", "-o": None}

    def test_missing_value(self):

        """Function:  test_missing_value

        Description:  Test with missing -o value.

        Arguments:

        """

        self.assertEqual(
            (mongo_db_dump.mongo_dump(self.server, self.args3)),
            (True, "Error:  Missing -o option or value."))

    def test_missing_option(self):

        """Function:  test_missing_option

        Description:  Test with missing -o option.

        Arguments:

        """

        self.assertEqual(
            (mongo_db_dump.mongo_dump(self.server, self.args2)),
            (True, "Error:  Missing -o option or value."))

    @mock.patch("mongo_db_dump.mongo_generic")
    def test_failure(self, mock_cmd):

        """Function:  test_failure

        Description:  Test with failure of mongo dump.

        Arguments:

        """

        mock_cmd.return_value = (True, "Error Message")

        self.assertEqual(
            (mongo_db_dump.mongo_dump(self.server, self.args)),
            (True, "Error Message"))

    @mock.patch("mongo_db_dump.mongo_generic")
    def test_db_dump(self, mock_cmd):

        """Function:  test_db_dump

        Description:  Test with database dump successful.

        Arguments:

        """

        mock_cmd.return_value = (False, None)

        self.assertEqual(
            (mongo_db_dump.mongo_dump(self.server, self.args)), (False, None))


if __name__ == "__main__":
    unittest.main()
