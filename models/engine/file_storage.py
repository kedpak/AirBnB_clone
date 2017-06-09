#!/usr/bin/python3

from models.base_model import BaseModel


class FileStorage:
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
        BaseModel.id = 12121212

    def all(self):
        return (__objects)

    def new(self, obj):
        

print(BaseModel.id)
