#!/usr/bin/python3
import uuid
from datetime import datetime
import json

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_json(self):
        self.created_at = str(datetime.now().isoformat(sep="T"))
        self.updated_at = str(datetime.now().isoformat(sep="T"))
        self.__dict__["__class__"] = self.__class__.__name__
        return(self.__dict__)

    def __str__(self):
        "returns [<class name>] (<self.id>) <self.__dict__>"
        return('[{}] ({}) {}'.format(self.__class__.__name__,self.id, self.__dict__))
