#!/usr/bin/python3
"""Defines a class FileStorage that serializes and deserializes JSON file to instances"""
#Step 1:  We need JSON. So we must import it
import json
from models.base_model import BaseModel
from models.user import User
#Step 2: We can now start building our Class FileStorage
#Note that the Class as Class Attributes! unlike BaseModel Class
#Note that the class attributes are PRIVATE, so they need a __ at the beginning of the name

class FileStorage:
    """class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    
    Attributes:
        __file_path (str): string - path to the JSON file
        __objects (dict): dictionary - empty but will store all objects by <class name>.id
    """
    #We need a file path to JSON File
    __file_path = "file.json"
    #We also need a dictionary to store our objects
    __objects = {}

    # We need to set objects in __objects with the key we created (objclass)
    def new(self, obj):
        """Sets in __objects the 'obj' with <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    # We need to have the ability to return the dictionary of the objects
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    #We need to serialize all the __objects to the JSON file
    def save(self):
        """serializes __objects to the JSON file(path: __filepath)"""
        sterObj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(sterObj, file)

    #If the file exists, we need to deserialize the JSON file
    
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        # We convert the JSON file back to a py dictionary, then iterate through the dictionary
        # and create new instances of the corresponding class
        try:
            with open(FileStorage.__file_path) as f:
                sterObj = json.load(f) # Converts it back to a python dictionary
                for value in sterObj.values(): # We then loop through the dictionary and create new instances
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return