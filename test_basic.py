import os
import unittest
from run import app, db


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
        db.create_all()

    def tearDown(self):
        pass

        ############################
        #### setup and teardown ####
        ############################

    def test_main_page(self):
        response = self.app.get('/api/books', follow_redirects=False)
        self.assertEquals(response.status_code, 500)

    def test_delete_book(self):
        response = self.app.delete('/api/books/<int:book_id>')
        self.assertEquals(response.status_code, 400)

    def test_update_book(self):
        response = self.app.post('/api/books/<int:book_id>')
        self.assertEquals(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
