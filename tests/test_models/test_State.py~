#!/user/bin/python3
"""module: test_State"""
import unittest
import models
import uuid
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class test_State(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_instance(self):
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_in"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "State"))

    def test_update(self):
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_Save(self):
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

if __name__ == "__main__":
    unittest.main
