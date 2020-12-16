#!/usr/bin/python
# Classification (U)

"""Program:  sync_cp_dump.py

    Description:  Integration testing of sync_cp_dump in mongo_db_dump.py.

    Usage:
        test/integration/mongo_db_dump/sync_cp_dump.py

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
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class Server3(object):

    """Class:  Server3

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
        self.hold = None

    def lock_db(self, lock):

        """Method:  lock_db

        Description:  Stub holder for mongo_class.Server.lock_db method.

        Arguments:
            (input) lock -> True|False - Lock the database?

        """

        self.hold = lock
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
        self.hold = None

    def lock_db(self, lock):

        """Method:  lock_db

        Description:  Stub holder for mongo_class.Server.lock_db method.

        Arguments:
            (input) lock -> True|False - Lock the database?

        """

        self.hold = lock

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
        test_db_locked_mail -> Test with database is locked and mail.
        test_unable_to_lock_mail -> Test database unable to lock it & mail.
        test_db_dump_locked_mail -> Test with database locked and mail.
        test_db_dump_mail -> Test with successful dump and mail.
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

        self.mail = gen_class.setup_mail("email_addr", subj="subject_line")
        self.server = Server()
        self.server2 = Server2()
        self.server3 = Server3()
        self.args_array = {"-o": "DirectoryPath"}
        self.msg = "Error/Warning detected in database dump."
        self.msg1 = "Warning:  Database still locked after dump."
        self.msg1a = self.msg + self.msg1
        self.msg2 = "Error:  Unable to lock the database for dump to occur."
        self.msg2a = self.msg + self.msg1
        self.msg3 = ""
        self.msg3a = ""

    @unittest.skip("Not yet working")
    def test_db_locked_mail(self):

        """Function:  test_db_locked_mail

        Description:  Test with database is locked and mail.

        Arguments:

        """

        self.server.locked = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server, self.args_array, mail=self.mail)), (True, self.msg1))
        self.assertEqual(self.mail.msg, self.msg1)

    @unittest.skip("Not yet working")
    @mock.patch("mongo_db_dump.gen_class.Mail.send_mail",
                mock.Mock(return_value=True))
    def test_unable_to_lock_mail(self):

        """Function:  test_unable_to_lock_mail

        Description:  Test with database unable to lock it and mail.

        Arguments:

        """

        self.server.locked = False

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server2, self.args_array, mail=self.mail)), (True, self.msg2))
        self.assertEqual(self.mail.msg, self.msg2a)

    @unittest.skip("Not yet working")
    @mock.patch("mongo_db_dump.gen_class.Mail.send_mail",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump_locked_mail(self, mock_copy):

        """Function:  test_db_dump_locked_mail

        Description:  Test with database locked and mail.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server, self.args_array, mail=self.mail)), (True, self.msg1))
        self.assertEqual(self.mail.msg, self.msg1a)

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump_mail(self, mock_copy):

        """Function:  test_db_dump_mail

        Description:  Test with successful dump and mail.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server3, self.args_array, mail=self.mail)), (False, None))
        self.assertEqual(self.mail.msg, "")


if __name__ == "__main__":
    unittest.main()
