#!bin/usr/python3
"""
test base model
"""

import unittest
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        my_model=BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model= BaseModel()
        time.sleep(1)
        my_model.save()
        
        self.assertNotEqual(my_model.updated_at,my_model.created_at)

    def test_to_dict(self):
        my_model=BaseModel()
        dictionary= my_model.to_dict()
        self.assertIsInstance(dictionary,dict)
        self.assertEqual(dictionary["__class__"],"BaseModel")
        self.assertEqual(dictionary["id"],my_model.id)
        self.assertEqual(dictionary["created_at"],my_model.created_at.isoformat())
        self.assertEqual(dictionary["updated_at"],my_model.updated_at.isoformat())

    def test_str(self):
        my_model= BaseModel()
        string= str(my_model)

        self.assertTrue(string.startswith("[BaseModel]"))
        self.assertIn(my_model.id,string)
        self.assertIn(str(my_model.__dict__),string)

if __name__ == "__main__":
    unittest.main()


