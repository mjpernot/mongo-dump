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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_dump
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_cond_req
        arg_dir_chk
        arg_dir_crt
        arg_noreq_xor
        arg_require
        get_val
        arg_xor_dict

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.dir_perms_crt = None
        self.dir_perms_crt2 = True
        self.opt_xor_val = None
        self.opt_xor_val2 = True
        self.xor_noreq = None
        self.xor_noreq2 = True
        self.opt_con_req = None
        self.opt_con_req2 = True

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_dir_crt(self, dir_perms_crt):

        """Method:  arg_dir_crt

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_crt.

        Arguments:

        """

        self.dir_perms_crt = dir_perms_crt

        return self.dir_perms_crt2

    def arg_noreq_xor(self, xor_noreq):

        """Method:  arg_noreq_xor

        Description:  Method stub holder for gen_class.ArgParser.arg_noreq_xor.

        Arguments:

        """

        self.xor_noreq = xor_noreq

        return self.xor_noreq2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def get_val(self, skey, def_val):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def arg_xor_dict(self, opt_xor_val):

        """Method:  arg_xor_dict

        Description:  Method stub holder for gen_class.ArgParser.arg_xor_dict.

        Arguments:

        """

        self.opt_xor_val = opt_xor_val

        return self.opt_xor_val2


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline -> Argv command line.
            (input) flavor -> Lock flavor ID.

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_help_true
        test_help_false
        test_arg_req_false
        test_arg_req_true
        test_arg_xor_dict_false
        test_arg_xor_dict_true
        test_arg_noreq_xor_false
        test_arg_noreq_xor_true
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_arg_dir_chk_false
        test_arg_dir_chk_true
        test_arg_dir_crt_false
        test_arg_dir_crt_true
        test_run_program
        test_programlock_id
        test_programlock_false
        test_programlock_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args2.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-y": "Flavor"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.opt_xor_val2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_xor_dict_false(self, mock_arg, mock_help):

        """Function:  test_arg_xor_dict_false

        Description:  Test arg_xor_dict if returns false.

        Arguments:

        """

        self.args.opt_xor_val2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_xor_dict_true(self, mock_arg, mock_help):

        """Function:  test_arg_xor_dict_true

        Description:  Test arg_xor_dict if returns true.

        Arguments:

        """

        self.args.xor_noreq2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_noreq_xor_false(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_false

        Description:  Test arg_noreq_xor if returns false.

        Arguments:

        """

        self.args.xor_noreq2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_noreq_xor_true(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_true

        Description:  Test arg_noreq_xor if returns true.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_cond_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_cond_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_dir_chk_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_false

        Description:  Test arg_dir_chk if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_dir_chk_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_true

        Description:  Test arg_dir_chk if returns true.

        Arguments:

        """

        self.args.dir_perms_crt2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_dir_crt_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_crt_false

        Description:  Test arg_dir_crt if returns false.

        Arguments:

        """

        self.args.dir_perms_crt2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_class.ProgramLock")
    @mock.patch("mongo_db_dump.run_program")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_arg_dir_crt_true(self, mock_arg, mock_help, mock_run,
                                   mock_lock):

        """Function:  test_arg_dir_crt_true

        Description:  Test arg_dir_crt if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_class.ProgramLock")
    @mock.patch("mongo_db_dump.run_program")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_class.ProgramLock")
    @mock.patch("mongo_db_dump.run_program")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_programlock_true(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_class.ProgramLock")
    @mock.patch("mongo_db_dump.run_program")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_programlock_false(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.side_effect = \
            mongo_db_dump.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_dump.main())

    @mock.patch("mongo_db_dump.gen_class.ProgramLock")
    @mock.patch("mongo_db_dump.run_program")
    @mock.patch("mongo_db_dump.gen_libs.help_func")
    @mock.patch("mongo_db_dump.gen_class.ArgParser")
    def test_programlock_id(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_id

        Description:  Test with ProgramLock with flavor id.

        Arguments:

        """

        mock_arg.return_value = self.args2
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mongo_db_dump.main())


if __name__ == "__main__":
    unittest.main()
