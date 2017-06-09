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
        if len(args) == 0 and len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        else:
            if 'id' in kwargs:
                self.id = kwargs.get("id")
            if 'created_at' in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.now()

    def save(self):
        ''' public method:
        updates current datetime
        '''
        self.updated_at = datetime.now()

    def to_json(self):
        ''' public method:
        returns dictionary containing all key/values
        '''
        self.created_at = str(datetime.now().isoformat())
        if hasattr(self, "updated_at") == True:
            self.updated_at = str(datetime.now().isoformat())
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)

    def __str__(self):
        '''print result
        '''
        return ('[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__))
