# test_app.py

import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Sends HTTP GET to /
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Adjust based on your app output

if __name__ == "__main__":
    unittest.main()

