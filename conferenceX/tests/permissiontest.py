from conferenceX.tests.apptest import FlaskTest, ResponseTest
from getpass import getpass


class PermissionTest():
    """ This class is used for testing admin permissions on the website"""

    def __init__(self):
        self.test_app = FlaskTest()
        self.username = input("Enter the correct username: ")
        self.password = getpass()

    def test_login(self, username, password, expected, message):
        """ Test login by redirect """
        login = self.test_app.login(username, password)
        ResponseTest.test_path(login, expected, message)

    def test_add_table(self, table, status_code, message):
        """ Test table by status code """
        permission = self.test_app.get_add_table(table)
        ResponseTest.test_status_code(permission, status_code, message)

    def test_admin(self, expected, message):
        """ Test admin by searching for redirect """
        admin = self.test_app.get_admin()
        ResponseTest.test_path(admin, expected, message)

    def test_multiple_logins(self):
        """ Tests a bunch of logins, correct and incorrect """

        self.test_login(self.username, self.password, "/admin",
                        "FAILED good login")
        self.test_app.logout()

        self.test_login("walla", "bing", b"", "FAILED bad login")
        self.test_login(self.username, "bing", b"", "FAILED bad username")
        self.test_login("walla", self.password, b"", "FAILED bad password")

        print("PASSED login tests")

    def test_permissions(self):
        """ Tests a bunch of valid and invalid permissions """

        valid_tables = ["Question", "Person", "Price"]

        self.test_admin("/login", "FAILED unlogin admin access")
        self.test_add_table("walla", 403,
                            "FAILED unlogin add invalid table")
        self.test_add_table("HTML", 403, "FAILED unlogin add HTML")

        for table in valid_tables:
            self.test_add_table(table, 403, "FAILED unlogin add " + table)

        print("PASSED invalid permissons")

        self.test_app.login(self.username, self.password)
        self.test_admin(b"", "FAILED login admin acess")
        self.test_add_table("wasd", 403, "FAILED login add invalid table")
        self.test_add_table("HTML", 403, "FAILED login add HTML")

        for table in valid_tables:
            self.test_add_table(table, 200, "FAILED login add " + table)
        self.test_app.logout()

        print("PASSED valid permissons")
