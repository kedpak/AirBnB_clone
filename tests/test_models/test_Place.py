#!/usr/bin/python3
import unittest
from models.place import Place
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""module: test_Place"""

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()


    def tearDown(self):
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_instance(self):
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_in"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "Amenity"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_update(self):
        self.place.save()
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_Save(self):
        self.place.save()
        self.assertTrue(hasattr(self.place, "updated_at"))

if __name__ == '__main__':
    unittest.main()
