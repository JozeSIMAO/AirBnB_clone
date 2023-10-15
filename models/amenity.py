#!/usr/bin/python3
"""Defines a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity
    Attributes:
        name (str): the name of the amenity
    """

    name = ""
