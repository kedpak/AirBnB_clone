#!/user/bin/python3
"""module: test_Review"""
import unittest
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage

class test_Review(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def tearDown(self):
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_in"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "Review"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.reviewls, "user_id"))

    def test_update(self):
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_Save(self):
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

if __name__ == "__main__":
    unittest.main
