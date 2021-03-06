""" This module is a script for testing certain parts of the website """


import argparse
import conferenceX.tests.dbtest as dbtest
from conferenceX.tests.permissiontest import PermissionTest


def run():
    """ runs testing script """
    parser = argparse.ArgumentParser(description="Do some tests")
    parser.add_argument("-all", help="do all tests except db insertions",
                        action="store_true")
    parser.add_argument("-r", "--root", help="add a root user",
                        action="store_true")
    parser.add_argument("-i", "--insert", help="insert test data",
                        action="store_true")
    parser.add_argument("-b", "--blank", help="insert then delete blanks",
                        action="store_true")
    parser.add_argument("-p", "--permission", help="test website permissions",
                        action="store_true")
    parser.add_argument("-f", "--fake", help="try logging in as fake",
                        action="store_true")

    args = parser.parse_args()

    if args.insert:
        dbtest.insert_test_data()

    if args.root:
        dbtest.insert_root()

    if args.blank:
        dbtest.test_blank_data()

    if args.all or args.permission:
        ptest = PermissionTest()
        ptest.test_multiple_logins()
        ptest.test_permissions()

    if args.all or args.fake:
        dbtest.test_fake_login()

if __name__ == "__main__":
    run()
