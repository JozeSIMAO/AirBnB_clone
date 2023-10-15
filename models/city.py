#!/usr/bin/python3
"""Defines a class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the City

    Attributes:
        state_id (str): the States ID
        name (str): The name of the city
    """

    state_id = ""
    name = ""
