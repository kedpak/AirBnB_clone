#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_json()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print('\n' * 3)

my_model2 = BaseModel()
my_model2.name = "Christian"
my_model2.my_age = 32
my_model2.year_born = 1985
print("--")
my_model2_json = my_model2.to_json()
print(my_model2_json)
print("JSON of my_model2:")
for key in my_model2_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model2_json[key]), my_model2_json[key]))
print('\n' * 3)

print("--")
my_new_model = BaseModel(**my_model2_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
