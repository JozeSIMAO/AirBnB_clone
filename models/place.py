#!/usr/bin/python3
"""Defines a class Place that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the Place

    Attribute:
        city_id (str): City's ID
        user_id (str): User's ID
        name (str): name of the Place
        description (str): Description of the city
        number_rooms (int): Number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): number of maximum guests
        price_by_night (int): price by night
        latitude (float): latitude of place
        longitude (float): longitude of place
        amenity_ids (list): list of amenity ID's
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
