import unittest
from run import app
from resources import UserRegistration, CreateBook


class TestUserRegistration(unittest.TestCase):
    def register(self, username, password):
        return self.app.post('/api/auth/register', data=dict(
            username=username, password=password
        ), follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('henry@gmail.com', 'password')
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'Thanks for registering!', response.data)


if __name__ == '__main__':
    unittest.main()

