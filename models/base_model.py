

import uuid
from datetime import datetime

class BaseModel :
    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                elif (key =="created_at" or key == "updated_at"):
                    setattr(self,key,datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self,key,value)
        else:
            from models import storage
            self.id=str(uuid.uuid4())
            self.created_at=datetime.now()
            self.updated_at= datetime.now()
            storage.new(self)

    def __str__(self):
        classname=self.__class__.__name__
        return ("[{}] ({}) {}".format(classname,self.id,self.__dict__))

    def save(self):
        from models import storage
        self.updated_at=datetime.now()
        storage.save()

    def to_dict(self):
        dictionary=self.__dict__.copy()
        dictionary["__class__"]=self.__class__.__name__
        dictionary["created_at"]=self.created_at.isoformat()
        dictionary["updated_at"]=self.updated_at.isoformat()
        return dictionary
