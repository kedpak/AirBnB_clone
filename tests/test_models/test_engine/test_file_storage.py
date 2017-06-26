#!/usr/bin/python3
import unittest
import os
import uuid
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class testFileStorage(unittest.TestCase):

    def setUp(self):
        self.filestorage = FileStorage()
        self.basemodel = BaseModel()

    def tearDown(self):
        '''teardown'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_file(self):
        self.basemodel.save()
        self.assertTrue(os.path.isfile("./file.json"))


if __name__ == '__main__':
    unittest.main
