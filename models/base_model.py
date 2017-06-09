#!/usr/bin/python3
'''module: base_model
creates class BaseModel which defines all common attributes/methods
for other classes
'''
from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    '''class:  defines all common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''constructor:
        sets attributes for id and created_at
        '''
        time = '%Y-%m-%d %H:%M:%S.%f'
        if len(kwargs) > 0:
            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__ = kwargs

            created_time = datetime.strptime(kwargs['created_at'], time)
            self.__dict__['created_at'] = created_time

            if 'updated_at' in self.__dict__:
                updated_time = datetime.strptime(kwargs['updated_at'], time)
                self.__dict__['updated_at'] = updated_time

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        ''' public method:
        updates current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        ''' public method:
        returns dictionary containing all key/values
        '''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = str(self.created_at)
        if 'updated_at' in new_dict:
            new_dict['updated_at'] = str(self.updated_at)
        return new_dict

    def __str__(self):
        '''print result
        '''
        return ('[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__))
