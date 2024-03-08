#!bin/usr/python3
"""
test base model
"""

import unittest
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()
        time.sleep(1)
        my_model.save()

        self.assertNotEqual(my_model.updated_at, my_model.created_at)

    def test_to_dict(self):
        model = BaseModel()
        dictt = model.to_dict()
        self.assertIsInstance(dictt, dict)
        self.assertEqual(dictt["__class__"], "BaseModel")
        self.assertEqual(dictt["id"], model.id)
        self.assertEqual(dictt["created_at"], model.created_at.isoformat())
        self.assertEqual(dictt["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()
        string = str(my_model)

        self.assertTrue(string.startswith("[BaseModel]"))
        self.assertIn(my_model.id, string)
        self.assertIn(str(my_model.__dict__), string)


if __name__ == "__main__":
    unittest.main()
