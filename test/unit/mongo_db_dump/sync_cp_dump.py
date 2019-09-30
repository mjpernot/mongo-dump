#!/usr/bin/python
# Classification (U)

"""Program:  sync_cp_dump.py

    Description:  Unit testing of sync_cp_dump in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/sync_cp_dump.py

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


class Server3(object):

    """Class:  Server3

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

        self.locked = True

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

        self.locked = False


class Server2(object):

    """Class:  Server2

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

        pass

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

        self.locked = False


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
        test_db_dump_locked -> Test with dumping of database, but still locked.
        test_unable_to_lock -> Test with database unable to lock it.
        test_db_locked -> Test with database is locked.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.server2 = Server2()
        self.server3 = Server3()
        self.args_array = {"-o": "DirectoryPath"}
        self.msg1 = "Error:  Database previously locked, unable to dump."
        self.msg2 = "Error:  Unable to lock the database for dump to occur."
        self.msg3 = "Warning:  Database still locked after dump."

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump(self, mock_copy):

        """Function:  test_db_dump

        Description:  Test with database dump successful.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server3, self.args_array)), (False, None))

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump_locked(self, mock_copy):

        """Function:  test_db_dump_locked

        Description:  Test with dumping of database, but still locked.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server, self.args_array)), (True, self.msg3))

    def test_unable_to_lock(self):

        """Function:  test_unable_to_lock

        Description:  Test with database unable to lock it.

        Arguments:

        """

        self.server.locked = False

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server2, self.args_array)), (True, self.msg2))

    def test_db_locked(self):

        """Function:  test_db_locked

        Description:  Test with database is locked.

        Arguments:

        """

        self.server.locked = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server, self.args_array)), (True, self.msg1))


if __name__ == "__main__":
    unittest.main()
