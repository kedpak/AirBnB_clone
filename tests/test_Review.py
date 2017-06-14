#!/user/bin/python3
"""module: amenity_test"""
import unittest
from models.test_Review import Review

Class test_Review(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        self.assertTrue(hasattr(self.Review, "created_at"))
        self.assertTrue(hasattr(self.Review, "updated_in"))
        self.assertTrue(hasattr(self.Review, "place_id"))
        self.assertTrue(hasattr(self.Review, "name"))
        self.assertEqual(hasattr(self.__class__.__name__, "Review"))
        self.assertTrue(hasattr(self.Review, "text"))
        self.assertTrue(hasattr(self.Review, "user_id"))

    def test_update(self):
        self.state.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_Save(self):
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

if __name__ == "__main__":
    unittest.main
