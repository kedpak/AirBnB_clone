#!/usr/bin/python3
import unittest
from models.amenity import Amenity
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""module: amenity_test"""


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_instance(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_in"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "Amenity"))

    def test_update(self):
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_str__(self):
        string = "[{}] ({}) {}".format(
            self.amenity.__class__.__name__, str(
                self.amenity.id), self.amenity.__dict__)
        self.assertEqual(string, self.amenity)

if __name__ == '__main__':
    unittest.main()
