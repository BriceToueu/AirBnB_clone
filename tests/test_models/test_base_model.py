import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_example(self):
        """Example test method"""
        model = BaseModel()
        self.assertIsNotNone(model)
