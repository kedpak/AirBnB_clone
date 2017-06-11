#!/usr/bin/python3
import uuid
import datetime
import json
from models import storage

format = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        if kwargs:
            if kwargs.get('id') is not None:
                self.__dict__ = kwargs
            self.created_at = datetime.datetime.strptime(kwargs.get('created_at'), format)
            self.__dict__ == kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_json(self):
        new_dict = self.__dict__.copy()
        new_dict.update({'created_at': self.created_at.strftime(self.format)})
        new_dict.update({"__class__":str(self.__class__.__name__)})
        if hasattr(self, 'updated_at'):
            new_dict['updated_at'] = str(self.updated_at)
        else:
            pass
        return new_dict

    def __str__(self):
        "returns [<class name>] (<self.id>) <self.__dict__>"
        return('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))
