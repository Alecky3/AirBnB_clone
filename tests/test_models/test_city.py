#!/usr/bin/python3
"""class City"""


from models.city import City
import unittest
import models
import os


class TestCity(unittest.Testcase):
    """Represents City"""

    def setup(self):
        """SetUp method"""

        self.city = City()

    def TearDown(self):
        """TearDown method"""

        del self.city

    def test_docstring(self):
        """Test docstring for module and class"""

        self.assertIsNotNone(
            models.city.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(City.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Test permissions"""

        test_file = os.access("models/city.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/city.py", os.W_OK)
        self.assertTrue(test_file, "Write permissions")
        test_file = os.access("models/city,py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Test type object of City"""

        self.assertEqual(
            str(type(self.city)),
            "<class 'models.city.City'>")
        self.assertIsInstance(self.city, City)
