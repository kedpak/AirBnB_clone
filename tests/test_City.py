#!/user/bin/python3
"""module: amenity_test"""
import unittest
from models.test_City import City


Class test_City(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.state, City)

    def test_attributes(self):
        self.assertTrue(hasattr(self.City, "created_at"))
        self.assertTrue(hasattr(self.City, "updated_in"))
        self.assertTrue(hasattr(self.City, "id"))
        self.assertTrue(hasattr(self.City, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "City"))

    def test_update(self):
        self.state.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_Save(self):
        self.city.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

if __name__ == "__main__":
    unittest.main
