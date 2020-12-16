#!/usr/bin/python
# Classification (U)

"""Program:  get_req_options.py

    Description:  Unit testing of get_req_options in mongo_db_dump.py.

    Usage:
        test/unit/mongo_db_dump/get_req_options.py

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

# Local
sys.path.append(os.getcwd())
import mongo_db_dump
import version

__version__ = version.__version__


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

        self.auth_db = "admin"
        self.repset = "spock"
        self.repset_hosts = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_none_option -> Test with an option with None setting.
        test_add_two_options -> Test with adding two options to list.
        test_add_option -> Test with adding option to list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.arg_req_dict = {"auth_db": "--authenticationDatabase="}
        self.arg_req_dict2 = dict(self.arg_req_dict)
        self.arg_req_dict2["repset"] = "--repsetName="
        self.arg_req_dict3 = dict(self.arg_req_dict2)
        self.arg_req_dict3["repset_hosts"] = "--repsetHosts="
        self.results = ["--authenticationDatabase=admin"]
        self.results2 = list(self.results)
        self.results2.append("--repsetName=spock")

    def test_none_option(self):

        """Function:  test_none_option

        Description:  Test with an option with None setting.

        Arguments:

        """

        self.assertEqual(mongo_db_dump.get_req_options(
            self.server, self.arg_req_dict3), self.results2)

    def test_add_two_options(self):

        """Function:  test_add_two_options

        Description:  Test with adding option to list.

        Arguments:

        """

        self.assertEqual(mongo_db_dump.get_req_options(
            self.server, self.arg_req_dict2), self.results2)

    def test_add_option(self):

        """Function:  test_add_option

        Description:  Test with adding option to list.

        Arguments:

        """

        self.assertEqual(mongo_db_dump.get_req_options(
            self.server, self.arg_req_dict), self.results)


if __name__ == "__main__":
    unittest.main()
