from conferenceX.tests.apptest import FlaskTest
from getpass import getpass


class PermissionTest():

    def __init__(self):
        self.test_app = FlaskTest()
        self.username = input("Enter the correct username: ")
        self.password = getpass()

    def test_login(self, username, password, status_code, message):
        login = self.test_app.login(username, password)
        assert login.status_code == status_code, message + str(login)

    def test_multiple_logins(self):
        """ Tests a bunch of logins, correct and incorrect """

        self.test_login(self.username, self.password, 202, "FAILED good ligin")
        self.test_app.logout()

        self.test_login("walla", "bing", 401, "FAILED bad login")
        self.test_login(self.username, "bing", 401, "FAILED bad username")
        self.test_login("walla", self.password, 401, "FAILED bad password")

        print("PASSED login tests")

    def test_add_table(self, table, status_code, message):
        permission = self.test_app.get_add_table(table)
        assert permission.status_code == status_code,  message +\
            str(permission)

    def test_admin(self, status_code, message):
        admin = self.test_app.get_admin()
        assert admin.status_code == status_code, message + str(admin)

    def test_permissions(self):
        """ Tests a bunch of permissions """

        valid_tables = ["Question", "Person", "Price"]
        self.test_admin(403, "FAILED unlogin admin access")
        self.test_add_table("walla", 403, "FAILED unlogin add invalid table")
        self.test_add_table("HTML", 403, "FAILED unlogin add HTML")

        for table in valid_tables:
            self.test_add_table(table, 403, "FAILED unlogin add " + table)

        print("PASSED invalid permissons")

        self.test_app.login(self.username, self.password)
        self.test_admin(200, "FAILED login admin acess")
        self.test_add_table("wasd", 403, "FAILED login add invalid table")
        self.test_add_table("HTML", 403, "FAILED login add HTML")

        for table in valid_tables:
            self.test_add_table(table, 200, "FAILED login add " + table)
        self.test_app.logout()

        print("PASSED valid permissons")
