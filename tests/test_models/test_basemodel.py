#!/usr/bin/python3
import unittest
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
""" base model test """


class TestBaseModel(unittest.TestCase):
    """ class test """

    def setUp(self):
        self.basemodel = BaseModel()

    def test_id(self):
        new_dict = self.basemodel.__dict__
        self.assertIsNotNone(new_dict.get("id"))

    def test_attr(self):
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertFalse(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "new_attr"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def test_save(self):
        new_dict = self.basemodel.__dict__
        pre_save = new_dict.get("updated_at")
        self.basemodel.save()
        post_save = new_dict.get("updated_at")
        self.assertNotEqual(pre_save, post_save)

    def test__str__(self):
        correct_format = ("[{}] ({}) {}".format
                          (self.basemodel.__class__.__name__,
                           self.basemodel.id,
                           self.basemodel.__dict__))
        self.assertEqual(print(correct_format), print(self.basemodel))

if __name__ == '__main__':
    unittest.main()
