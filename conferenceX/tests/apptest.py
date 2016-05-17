from runserver import app


class FlaskTest():
    def __init__(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.app.post('/login', data=data, follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def get_add_table(self, table):
        return self.app.get('/admin/add/' + table, follow_redirects=True)

    def get_admin(self):
        return self.app.get('/admin', follow_redirects=True)
