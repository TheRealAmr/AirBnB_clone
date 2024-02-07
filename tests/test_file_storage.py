import unittest
import time
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_init(self):
        model = FileStorage()
        self.assertIsNotNone(model.file_path)

    def test_all(self):
        model = FileStorage()
        self.assertEqual(model.all(), {})

    def test_save(self):
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_all_with_objects(self):
        model = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        model.new(obj1)
        model.new(obj2)
        all_objects = model.all()

        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", all_objects)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", all_objects)

    def tearDown(self): #delete file.json made during testing
        if os.path.exists("file.json"):
            os.remove("file.json")