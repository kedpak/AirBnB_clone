#!/usr/bin/python3
import unittest
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.test = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_id(self):
        new_dict = self.test.__dict__
        self.assertIsNotNone(new_dict.get("id"))

    def test_save(self):
        new_dict = self.test.__dict__
        pre_save = new_dict.get("updated_at")
        self.test.save()
        post_save = new_dict.get("updated_at")
        self.assertNotEqual(pre_save, post_save)

    def test__str__(self):
        correct_format = ("[{}] ({}) {}".format
                          (self.test.__class__.__name__,
                           self.test.id,
                           self.test.__dict__))
        self.assertEqual(str(correct_format), str(self.test))

if __name__ == '__main__':
    unittest.main()
