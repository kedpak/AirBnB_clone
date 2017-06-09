#!/usr/bin/python3
import json, os
'''
'''


class FileStorage:
    ''' '''
    __file_path = './file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        json_dict = {}
        for key in self.__objects.keys():
            json_dict[key] = self.__objects[key].to_json()
        with open(self.__file_path, mode='w', encoding='utf8') as j_file:
           j_file.write(json.dumps(json_dict, sort_keys = True, indent = 4,
                                   ensure_ascii = False))

    def reload(self):
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf8') as j_file:
                obj = json.load(j_file)
                for key in obj.keys():
                    self.__objects[key] = BaseModel(**obj[key])
