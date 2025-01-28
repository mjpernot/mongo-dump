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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_dump                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mongo_cfg", "-d": "config"}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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


class Server3():

    """Class:  Server3

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


class Server2():

    """Class:  Server2

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
        test_db_locked_mail
        test_unable_to_lock_mail
        test_db_dump_locked_mail
        test_db_dump_mail
        test_db_dump
        test_db_dump_locked
        test_unable_to_lock
        test_db_locked

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.server = Server()
        self.server2 = Server2()
        self.server3 = Server3()
        self.args = ArgParser()
        self.args.args_array = {"-o": "DirectoryPath"}
        self.msg1 = "Error:  Database previously locked, unable to dump."
        self.msg2 = "Error:  Unable to lock the database for dump to occur."
        self.msg3 = "Warning:  Database still locked after dump."

    def test_db_locked_mail(self):

        """Function:  test_db_locked_mail

        Description:  Test with database is locked and mail.

        Arguments:

        """

        self.server.locked = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server, self.args, mail=self.mail)), (True, self.msg1))
        self.assertEqual(self.mail.data, self.msg1)

    def test_unable_to_lock_mail(self):

        """Function:  test_unable_to_lock_mail

        Description:  Test with database unable to lock it and mail.

        Arguments:

        """

        self.server.locked = False

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server2, self.args, mail=self.mail)), (True, self.msg2))
        self.assertEqual(self.mail.data, self.msg2)

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump_locked_mail(self, mock_copy):

        """Function:  test_db_dump_locked_mail

        Description:  Test with database locked and mail.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server, self.args, mail=self.mail)), (True, self.msg3))
        self.assertEqual(self.mail.data, self.msg3)

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump_mail(self, mock_copy):

        """Function:  test_db_dump_mail

        Description:  Test with successful dump and mail.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual((mongo_db_dump.sync_cp_dump(
            self.server3, self.args, mail=self.mail)), (False, None))
        self.assertEqual(self.mail.data, None)

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump(self, mock_copy):

        """Function:  test_db_dump

        Description:  Test with database dump successful.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual(
            (mongo_db_dump.sync_cp_dump(self.server3, self.args)),
            (False, None))

    @mock.patch("mongo_db_dump.shutil.copytree")
    def test_db_dump_locked(self, mock_copy):

        """Function:  test_db_dump_locked

        Description:  Test with dumping of database, but still locked.

        Arguments:

        """

        mock_copy.return_value = True

        self.assertEqual(
            (mongo_db_dump.sync_cp_dump(self.server, self.args)),
            (True, self.msg3))

    def test_unable_to_lock(self):

        """Function:  test_unable_to_lock

        Description:  Test with database unable to lock it.

        Arguments:

        """

        self.server.locked = False

        self.assertEqual(
            (mongo_db_dump.sync_cp_dump(self.server2, self.args)),
            (True, self.msg2))

    def test_db_locked(self):

        """Function:  test_db_locked

        Description:  Test with database is locked.

        Arguments:

        """

        self.server.locked = True

        self.assertEqual(
            (mongo_db_dump.sync_cp_dump(self.server, self.args)),
            (True, self.msg1))


if __name__ == "__main__":
    unittest.main()
