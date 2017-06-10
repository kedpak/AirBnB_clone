#!/usr/bin/python3

#from models.base_model import BaseModel
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
        self.__objects[obj.id] = obj

    def save(self):
        '''serialize __object to JSON file
        '''
        j_dict = {}
        print(self.__objects)
        for key in self.__objects.keys():
            j_dict[key] = self.__objects[key].to_json()
        with open(self.__file_path, mode='w') as f:
            f.write(json.dumps(j_dict, sort_keys = True, indent = 4))


    def reload(self):
        '''deserialze the JSON file to __objects
        '''
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode = 'r') as f:
                j_load = json.load(f)
                print("after load")
                for key in j_load.keys():
                    self.__objects[key] = BaseModel(**j_load[key])
