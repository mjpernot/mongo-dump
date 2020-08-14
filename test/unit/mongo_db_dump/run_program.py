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

    status = True
    err_msg = "Dump Failure"

    if server and args_array:
        status = True
        err_msg = "Dump Failure"

    return status, err_msg


def mongo_dump(server, args_array, **kwargs):

    """Method:  mongo_dump

    Description:  Function stub holder for mongo_db_dump.mongo_dump.

    Arguments:
        (input) server -> Server instance.
        (input) args_array -> Dictionary of arguments.

    """

    status = False
    err_msg = None

    if server and args_array:
        status = False
        err_msg = None

    return status, err_msg


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

        self.name = "Mongo_name"

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
        
        test_suppress_success -> Test with successful dump and suppression.
        test_email_subj -> Test with subject line passed.
        test_email_no_subj -> Test with no subject line passed.
        test_mail -> Test with mail setup.
        test_dump_error -> Test with dump returning error.
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
        self.args_array2 = {"-d": True, "-c": True, "-M": True, "-e": True}
        self.args_array3 = {"-d": True, "-c": True, "-M": True, "-e": True,
                            "-s": ["subject", "line"]}
        self.args_array4 = {"-d": True, "-c": True, "-M": True, "-x": True}

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_suppress_failure(self, mock_inst, mock_disconn):

        """Function:  test_suppress_failure

        Description:  Test with dump failure and suppression.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        
        self.assertFalse(mongo_db_dump.run_program(self.args_array4,
                                                   self.func_dict2))

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_suppress_success(self, mock_inst, mock_disconn):

        """Function:  test_suppress_success

        Description:  Test with successful dump and suppression.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_db_dump.run_program(self.args_array,
                                                   self.func_dict))

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_email_subj(self, mock_inst, mock_disconn):

        """Function:  test_email_subj

        Description:  Test with subject line passed.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_db_dump.run_program(self.args_array3,
                                                   self.func_dict))

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_email_no_subj(self, mock_inst, mock_disconn):

        """Function:  test_email_no_subj

        Description:  Test with no subject line passed.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_db_dump.run_program(self.args_array2,
                                                   self.func_dict))

    @mock.patch("mongo_db_dump.cmds_gen.disconnect")
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_mail(self, mock_inst, mock_disconn):

        """Function:  test_mail

        Description:  Test with mail setup.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_disconn.return_value = True

        self.assertFalse(mongo_db_dump.run_program(self.args_array2,
                                                   self.func_dict))

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
