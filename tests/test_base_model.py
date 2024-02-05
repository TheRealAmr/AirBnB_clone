import unittest
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        model = BaseModel()
        self.assertTrue(str(model).startswith("[BaseModel]"))

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        time.sleep(.1)
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_from_dict(self):
        model1 = BaseModel()
        model_dict = model1.to_dict()
        model2 = BaseModel(**model_dict)
        model_dict2 = model2.to_dict()
        self.assertEqual(model_dict['__class__'], model_dict2['__class__'])
        self.assertEqual(model_dict['id'], model_dict2['id'])
        self.assertEqual(model_dict['created_at'], model_dict2['created_at'])
        self.assertIn('id', model_dict2)
        self.assertIn('created_at', model_dict2)
        self.assertIn('updated_at', model_dict2)