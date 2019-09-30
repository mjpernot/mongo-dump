#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/main.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_help_true -> Test help if returns true.
        test_help_false -> Test help if returns false.
        test_arg_req_true -> Test arg_require if returns true.
        test_arg_req_false -> Test arg_require if returns false.
        test_arg_req_xor_false -> Test arg_req_xor if returns false.
        test_arg_req_xor_true -> Test arg_req_xor if returns true.
        test_arg_noreq_xor_false -> Test arg_noreq_xor if returns false.
        test_arg_noreq_xor_true -> Test arg_noreq_xor if returns true.
        test_arg_cond_req_false -> Test arg_cond_req if returns false.
        test_arg_cond_req_true -> Test arg_cond_req if returns true.
        test_arg_dir_chk_crt_true -> Test arg_dir_chk_crt if returns true.
        test_arg_dir_chk_crt_false -> Test arg_dir_chk_crt if returns false.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "CfgFile", "-d": "CfgDir"}

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.arg_parser.arg_require")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser.arg_parse2")
    def test_help_false(self, mock_arg, mock_help, mock_req):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.arg_parser.arg_require")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser.arg_parse2")
    def test_arg_req_true(self, mock_arg, mock_help, mock_req):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.arg_parser.arg_req_xor")
    @mock.patch("mongo_db_dump.arg_parser.arg_require")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser.arg_parse2")
    def test_arg_req_false(self, mock_arg, mock_help, mock_req, mock_xor):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_xor.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_req_xor_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_xor_false

        Description:  Test arg_req_xor if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_req_xor_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_xor_true

        Description:  Test arg_req_xor if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_noreq_xor_false(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_false

        Description:  Test arg_noreq_xor if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_noreq_xor_true(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_true

        Description:  Test arg_noreq_xor if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_cond_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_cond_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.run_program")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.arg_parser")
    def test_arg_dir_chk_crt_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(mongo_db_dump.main())


if __name__ == "__main__":
    unittest.main()
