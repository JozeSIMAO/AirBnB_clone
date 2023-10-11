#!/usr/bin/python3

#Inorder to use the uuid and dattime to be able to assign a UUID and to get timestamps
import uuid
from datetime import datetime

class BaseModel:
    # No predefine class attributes (ASSIGNMENTS)
    """
    BaseModel represents a basic model with common attributes and methods.
    Public instance attributes:
    - id (str): A unique identifier for the object.
    - created_at (datetime): The timestamp when the object was created.
    - updated_at (datetime): The timestamp of the last update.

    Public instance methods:
    - save(): Updates the 'updated_at' timestamp to the current time.
    - to_dict(): Converts the object to a dictionary with specific formatting.
    - __str__(): Returns a string representation of the object in a specific format.
    """
    def __init__(self):
        # Instant Attribute (FUNCTION): Generate a unique ID using uuid.uuid4() and convert it to a string
        """Initialize a new BaseModel object with unique ID and timestamps."""
        self.id = str(uuid.uuid4())

        # Instant Attribute (FUNCTION): Sets the creation date and time (created_at) to the current datetime
        self.created_at = datetime.now()

        # Instant Attribute (FUNCTION): Sets the initial updated_at to be the same as created_at
        self.updated_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object in a specific format.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__) #str.format used #check if it prints when building console.py

    def save(self):
        # This method will Update the updated_at attribute with the current datetime
        """Update the 'updated_at' timestamp to the current time."""
        self.updated_at = datetime.now()

    def to_dict(self):
         """
        Convert the object to a dictionary.

        Returns:
            dict: A dictionary representation of the object with specific formatting.
        """
        obj_dict = self.__dict__  # Get all the attributes and their values
        obj_dict['__class__'] = self.__class__.__name__  # Add the class name
        obj_dict['created_at'] = self.created_at.isoformat()  # Converting it into ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Converting it into ISO format
        return obj_dict
