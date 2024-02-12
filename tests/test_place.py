import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):

    def setUp(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}

    def test_place_inherits_from_base_model(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "name"))

    def test_place_attributes_default_values(self):
        place = Place()
        self.assertEqual(place.name, "")

    def test_place_attributes_types(self):
        place = Place()
        self.assertIsInstance(place.name, str)

    def test_place_attributes_updated_at_and_created_at(self):
        place = Place()
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_place_to_dict_method(self):
        place = Place()
        self.assertEqual('to_dict' in dir(place), True)

    def test_place_name(self):
        place = Place()
        place.name = "Bee"
        self.assertEqual(place.name, "Bee")

    def tearDown(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}
