import os
import unittest
from run import app


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):
    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['JWT_BLACKLIST_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        "tear down test fixtures"
        print('### Tearing down the flask server ###')

        ############################
        #### setup and teardown ####
        ############################

    def test_books(self):
        response = self.app.get('/api/books', follow_redirects=True)
        self.assertEqual(response.status_code, 500)

    def test_delete_book(self):
        response = self.app.delete('/api/books/<int:book_id>')
        self.assertEqual(response.status_code, 404)

    def test_update_book(self):
        response = self.app.post('/api/books/<int:book_id>')
        self.assertEqual(response.status_code, 404)


        ########################
        #### helper methods ####
        ########################
    def register(self, username, password):
        return self.app.post('/api/auth/register', data=dict(
            username=username, password=password
        ), follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/api/auth/login', data=dict(
            username=username, password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/api/auth/logout', follow_redirects=True)

    def password_reset(self, username):
        return self.app.post('/api/auth/reset-password', data=dict(
            username=username
        ), follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('henry@gmail.com', 'password')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username', response.data)

    def test_valid_user_login(self):
        response = self.login('henry@gmail.com', 'password')
        self.assertEqual(response.status_code, 200)

    def test_password_reset(self):
        response = self.password_reset('henry@gmail.com')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
