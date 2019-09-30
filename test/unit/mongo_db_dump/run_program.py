#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/run_program.py

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


def mongo_dump2(server, args_array, **kwargs):

    """Method:  mongo_dump2

    Description:  Function stub holder for mongo_db_dump.mongo_dump.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of arguments.

    """

    return True, "Dump Failure"


def mongo_dump(server, args_array, **kwargs):

    """Method:  mongo_dump

    Description:  Function stub holder for mongo_db_dump.mongo_dump.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of arguments.

    """

    return False, None


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_run_program -> Test run_program function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_dict = {"-M": mongo_dump}
        self.func_dict2 = {"-M": mongo_dump2}
        self.args_array = {"-d": True, "-c": True, "-M": True}

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_dump_error(self, mock_inst, mock_disconn):

        """Function:  test_dump_error

        Description:  Test with dump returning error.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_dump.run_program(self.args_array,
                                                       self.func_dict2))

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_run_program(self, mock_inst, mock_disconn):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_db_dump.run_program(self.args_array,
                                                   self.func_dict))


if __name__ == "__main__":
    unittest.main()
