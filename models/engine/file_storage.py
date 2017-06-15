#!/usr/bin/python3

import json
import os


class FileStorage:

    def __init__(self):
        '''constructor method
        '''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''returns dictionary
        '''
        return (self.__objects)

    def new(self, obj):
        '''assigns the object id to  obj'''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        '''serialize __object to JSON file
        '''
        j_dict = {}
        for key in self.__objects.keys():
            j_dict[key] = self.__objects[key].to_json()
        with open(self.__file_path, mode='w') as f:
            f.write(json.dumps(j_dict, sort_keys=True, indent=4))

    def reload(self):
        '''deserialze the JSON file to __objects
        '''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
        }

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r') as f:
                j_load = json.load(f)
                for key in j_load.keys():
                    key_name = key.split('.')[0]
                    if key_name in classes:
                        self.__objects[key] = eval(key_name)(**j_load[key])
