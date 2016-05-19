from runserver import app
from urllib.parse import urlparse


class FlaskTest():
    """ A class that simulates an instance of the web application"""

    def __init__(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.app.post('/login', data=data, follow_redirects=False)

    def logout(self):
        return self.app.get('/logout', follow_redirects=False)

    def get_add_table(self, table):
        return self.app.get('/admin/add/' + table, follow_redirects=False)

    def get_admin(self):
        return self.app.get('/admin', follow_redirects=False)


class ResponseTest():
    """ A class for testing HTTP responses """

    @staticmethod
    def test_path(response, expected, message):
        """ Check if the path of a response object is the same as what was
        expected
        """
        path = urlparse(response.location).path
        assert path == expected, \
            message + ", expected: " + str(path) + " got: " + str(expected)

    @staticmethod
    def test_status_code(response, status_code, message):
        """ Check if status code is what was expected """
        assert response.status_code == status_code,  message +\
            str(response) + " expected: " + status_code
