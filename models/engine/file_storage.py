#!/usr/bin/python3

#Step 1:  We need JSON. So we must import it
import json

#Step 2: We can now start building our Class FileStorage
#Note that the Class as Class Attributes! unlike BaseModel Class
#Note that the class attributes are PRIVATE, so they need a __ at the beginning of the name

class FileStorage:
    #We need a file path to JSON File
    __file_path = "file.json"
    #We also need a dictionary to store our objects
    __objects = {}

    # We need to set objects in __objects with the key we created (objclass)
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    # We need to have the ability to return the dictionary of the objects
    def all(self):
        return self.__objects
    
    #We need to serialize all the __objects to the JSON file
    def save(self):
        sterObj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(sterObj, file)

    #If the file exists, we need to deserialize the JSON file
