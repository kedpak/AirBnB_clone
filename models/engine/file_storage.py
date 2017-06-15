#!/usr/bin/python3
import json
import os
'''module file_storage has class that serializes instances to a JSON file
and deserializes JSON file to instances:
'''


class FileStorage:
    '''serializes instances to a JSON file
    and deserializes JSON file to instances'''

    '''string - path to the JSON file'''
    __file_path = 'file.json'
    '''will store all objects by <class name>.id'''
    __objects = {}

    '''returns __objects'''
    def all(self):
        return self.__objects

    '''sets in __objects the obj with key <obj class name>.id'''
    def new(self, obj):
        self.__objects[obj.id] = obj

    '''serializes __objects to the JSON file (path: __file_path)'''
    def save(self):
        json_dict = {}
        for key in self.__objects.keys():
            json_dict[key] = self.__objects[key].to_json()
        with open(self.__file_path, mode='w', encoding='utf8') as j_file:
            j_file.write(json.dumps(json_dict, sort_keys=True, indent=4,
                                    ensure_ascii=False))
    '''deserializes the JSON file to __objects only if the JSON file exists'''
    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf8') as j_file:
                json_obj = json.load(j_file)
                for key in json_obj.keys():
                    self.__objects[key] = BaseModel(**json_obj[key])
