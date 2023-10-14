#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):

    def __init__(self):
        super().__init__() #Super allows us to call methods from the parent class - BaseModel
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
    
    def __str__(self):
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        user_dict = super().to_dict()
        
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        user_dict['email'] = self.email
        user_dict['password'] = self.password
      
        return user_dict
