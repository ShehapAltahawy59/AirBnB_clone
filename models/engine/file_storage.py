
import json
import os
from models.base_model import BaseModel

class FileStorage:

    __file_path="file.json"
    __objects={}

    def all(self):
        self.reload()
        return FileStorage.__objects

    def new(self, obj):
        obj_key="{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key]=obj

    def save(self):
        obj_dict={}
        for key in FileStorage.__objects.keys():
            obj_dict[key]=FileStorage.__objects[key].to_dict()
        with open (self.__file_path,"w") as f:
            json.dump(obj_dict,f)
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            
            with open (FileStorage.__file_path,"r") as f:
                try:
                    
                    obj_dict=json.load(f)

                    for key,value in obj_dict.items():
                        class_name = eval(key.split(".")[0])
                        id=key.split(".")[1]
                        obj=class_name(**value)
                        FileStorage.__objects[key]=obj
                except:
                    pass
                
