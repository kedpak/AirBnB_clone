#!/usr/bin/python3
import unittest
from models.user import User
"""module : test_user """

class TestUser(unittest.TestCase):
    """ class: TestUser """
    def setUp(self):
        self.user = User()

    def testattr(self):
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

if __name__ == '__main__':
    unittest.main()
