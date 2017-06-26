#!/usr/bin/python3
import unittest

class Test_BaseModel(unittest.TestCase):

    def setUp(self):
        self.test = BaseModel()

    def test_id(self):
        new_dict = self.test.__dict__
        self.assertFalse(hasattr(test.__dict__, self.id))

    def test_save(self):
        new_dict = self.test.__dict__
        pre_save = new_dict.get("updated_at")
        self.new_dict.save()
        post_save = new_dict.get("updated_at")
        self.assertNotEqual(pre_save, post_save)

    def test__str__(self):
        correct_format = "[{}] ({}) {}".format(self.test.__class__.__name__,
                                str(self.test.id),
                                self.test.__dict__)
        self.assertEqual(hasattr(correct_format, self.test)

if __name__ == '__main__':
    unittest.main()
