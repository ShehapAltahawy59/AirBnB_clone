#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
json = my_model.to_dict()
print(json)
print("JSON of my_model:")
for key in json.keys():
    s = "\t{}: ({}) - {}".format(key, type(json[key]), json[key])
    print(s)
