#!/usr/bin/python3
import os.path
import json
import datetime


class FileStorage:

    __file_path = './file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        new_dict = {}
        for key in self.__objects.keys():
            temp_dict = self.__objects[key].to_json()
            new_dict[key] = temp_dict
        with open(self.__file_path, 'w+', encoding='utf8') as f:
 #           new_dict.update({'updated_at':'string'} #datetime.datetime.now()
            json.dump(new_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path) == True:
            with open(self.__file_path, 'r', encoding='utf8') as f:
 #           new_dict.update({'updated_at':'string'} #datetime.datetime.now()
                    x = json.load(f)
                    for i in x.keys():
                        self.__objects[i] = BaseModel(**x[i])
"""
            print("theres a file")
            with open('file.json', "a") as f:
                print("++++++++++++++")
                print(f)
                for key in f.keys():
                    self.__object[key] = BaseModel(**jsonOBJ[key])
                    f.write(self.__object[key])
        else:
            print("no file to open")
            pass

            with open(self.__file_path, 'a') as f:
                d = json.load(f)
                for key in d.keys():
                    self.__object[key] = BaseModel(**jsonOBJ[key])
"""
