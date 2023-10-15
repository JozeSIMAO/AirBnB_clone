#!/usr/bin/python3
"""Defines a class User that inherits from class BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class that represents a user

    Attributes:
        email (str): users email
        passsword (str): users password
        first_name (str): users first name
        last_name (str): users last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
