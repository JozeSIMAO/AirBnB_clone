#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
