#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage

class test_FileStorage(unittest.TestCase):

    def setUp(self):
        self.filestorage = FileStorge()
        self.basemodel = BaseModel()

    def test_instance(self):
        self.assertIsInstance(self.storage, FileStorgae)

    def test_file(self):
        self.basemodel.save()
        self.assertTrue(os.path.isfile("./file.json")

    def test_All(self):
        basemodel_ID = self.basemodel.id
        objects_list = storage.all()
        if basemodel_ID in objects_list:
            num =1
        self.assertTrue(1 == num)

if __name__ == '__main__':
    unittest.main
