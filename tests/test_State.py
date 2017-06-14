#!/user/bin/python3
"""module: amenity_test"""
import unittest
from models.test_State import State


Class test_State(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        self.assertTrue(hasattr(self.State, "created_at"))
        self.assertTrue(hasattr(self.State, "updated_in"))
        self.assertTrue(hasattr(self.State, "id"))
        self.assertTrue(hasattr(self.State, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "State"))

    def test_update(self):
        self.state.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_Save(self):
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

if __name__ == "__main__":
    unittest.main
