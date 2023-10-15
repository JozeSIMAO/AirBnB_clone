#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_instance_creation(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_str_representation(self):
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
