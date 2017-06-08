#!/usr/bin/python3
import uuid, json
from datetime import datetime
from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):
        "init BaseModel class"
        if (kwargs.get('id') is not None):
            self.id = kwargs.get('id')
            self.created_at = datetime.now()
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        "save updates updated_at with current datetime"
        self.updated_at = datetime.now()

    def to_json(self):
        "returns dict of all keys and values"
        dict = {}
        x = self.__dict__
        dict = x
        dict.update({'__class__': self.__class__.__name__})
        return dict

    def __str__(self):
        "Sting method returns type, uuid and self dict"
        return('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))
