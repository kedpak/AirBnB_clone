#!/user/bin/python3
"""module: test_City"""
import unittest
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City


class testCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def tearDown(self):
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_instance(self):
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_in"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "City"))

    def test_update(self):
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_Save(self):
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

if __name__ == "__main__":
    unittest.main
