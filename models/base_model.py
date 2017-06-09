#!/usr/bin/python3
'''module: base_model
creates class BaseModel which defines all common attributes/methods
for other classes
'''
from datetime import datetime
import uuid


class BaseModel:
    '''class:  defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''constructor:
        sets attributes for id and created_at
        '''
        if kwargs:
            self.__dict__ = kwargs
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs.get("created_at"), '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs.get("updated_at"), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def save(self):
        ''' public method:
        updates current datetime
        '''
        self.updated_at = datetime.now()

    def to_json(self):
        ''' public method:
        returns dictionary containing all key/values
        '''
        self.created_at = str(self.created_at.isoformat())
        if hasattr(self, "updated_at") == True:
            self.updated_at = str(self.updated_at.isoformat())
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)

    def __str__(self):
        '''print result
        '''
        return ('[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__))
