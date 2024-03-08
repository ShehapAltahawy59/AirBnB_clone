#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
