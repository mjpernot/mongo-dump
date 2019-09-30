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
import version

__version__ = version.__version__


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
        test_db_dump -> Test with database dump successful.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-o": "DirectoryPath", "-p":  "DirectoryPath2"}

    @mock.patch("mongo_db_dump.cmds_gen.run_prog")
    @mock.patch("mongo_db_dump.mongo_libs.create_cmd")
    def test_db_dump(self, mock_cmd, mock_run):

        """Function:  test_db_dump

        Description:  Test with database dump successful.

        Arguments:

        """

        mock_cmd.return_value = "DumpCommand"
        mock_run.return_value = "RunCommand"

        self.assertEqual((mongo_db_dump.mongo_dump(
            self.server, self.args_array)), (False, None))


if __name__ == "__main__":
    unittest.main()
