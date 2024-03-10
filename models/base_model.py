#!/usr/bin/env python3
"""A Base class with common methods/attributes
for other classes
"""
import uuid
from datetime import datetime
from models import storage
import time

class BaseModel:
    """a class that defines attributes id,created_at, updated_at and methods
    """

    def __init__(self, *args, **kwargs):
        """constructor for class attrs id
        created_at and updated_at
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string repr of the class
        """
        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__))

    def save(self):
        """updates the updated_at attr
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary repr of the instance
        """
        my_dictionary = self.__dict__.copy()
        my_dictionary.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dictionary
