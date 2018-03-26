import unittest
from run import app


class BookTestCase(unittest.TestCase):
    def add_book(self):
        response = app.test_client().get('/api/books')
        self.assertEquals(response.status_code, 200)

    def book_delete(self):
        response = app.test_client().get('/api/books/<int:book_id>')
        self.assertEquals(response.status_code, 200)

    def book_update(self):
        response = app.test_client().post('/api/books/<int:book_id>')
        self.assertEquals(response.status_code, 200)

    def all_books(self):
        response = app.test_client().post('/api/books/<int:book_id>')
        self.assertEquals(response.status_code, 200)

    def register(self, username, password):
        return app.post('/api/auth/register', data=dict(
            username=username,
            password=password
        ))

    def logout(self):
        return app.get('/api/auth/logout')


if __name__ == '__main__':
    unittest.main()
