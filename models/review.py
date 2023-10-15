#!/usr/bin/python3
"""Defines a class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review

    Attributes:
        place_id (str): id of place
        user_id (str): id of user
        text (str): word review from user
    """

    place_id = ""
    user_id = ""
    text = ""
