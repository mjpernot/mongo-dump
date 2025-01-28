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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_dump                            # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

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

    if server and args_array and kwargs.get("mail", True):
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

    if server and args_array and kwargs.get("mail", True):
        status = False
        err_msg = None

    return status, err_msg


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val
        get_args_keys

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

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())


class Server():                                         # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "Mongo_name"
        self.status = True
        self.errmsg = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.errmsg


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connect_failure
        test_suppress_failure
        test_suppress_success
        test_email_subj
        test_email_no_subj
        test_mail
        test_dump_error
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_names = {"-M": mongo_dump}
        self.func_names2 = {"-M": mongo_dump2}
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args.args_array = {"-d": True, "-c": True, "-M": True}
        self.args2.args_array = {
            "-d": True, "-c": True, "-M": True, "-e": True}
        self.args3.args_array = {
            "-d": True, "-c": True, "-M": True, "-e": True,
            "-s": ["subject", "line"]}
        self.args4.args_array = {
            "-d": True, "-c": True, "-M": True, "-x": True}

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_connect_failure(self, mock_inst):

        """Function:  test_connect_failure

        Description:  Test with connection failure.

        Arguments:

        """

        self.server.status = False
        self.server.errmsg = "Connection failure"
        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_dump.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_suppress_failure(self, mock_inst):

        """Function:  test_suppress_failure

        Description:  Test with dump failure and suppression.

        Arguments:

        """

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_dump.run_program(self.args4, self.func_names2))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_suppress_success(self, mock_inst):

        """Function:  test_suppress_success

        Description:  Test with successful dump and suppression.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(
            mongo_db_dump.run_program(self.args, self.func_names))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_email_subj(self, mock_inst):

        """Function:  test_email_subj

        Description:  Test with subject line passed.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(
            mongo_db_dump.run_program(self.args3, self.func_names))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_email_no_subj(self, mock_inst):

        """Function:  test_email_no_subj

        Description:  Test with no subject line passed.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(
            mongo_db_dump.run_program(self.args2, self.func_names))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_mail(self, mock_inst):

        """Function:  test_mail

        Description:  Test with mail setup.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(
            mongo_db_dump.run_program(self.args2, self.func_names))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_dump_error(self, mock_inst):

        """Function:  test_dump_error

        Description:  Test with dump returning error.

        Arguments:

        """

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(
                mongo_db_dump.run_program(self.args, self.func_names2))

    @mock.patch("mongo_db_dump.get_req_options", mock.Mock(return_value=[]))
    @mock.patch("mongo_db_dump.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_dump.mongo_libs.create_instance")
    def test_run_program(self, mock_inst):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mongo_db_dump.run_program(self.args, self.func_names))


if __name__ == "__main__":
    unittest.main()
