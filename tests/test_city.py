import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):

    def setUp(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}

    def test_city_inherits_from_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "name"))

    def test_city_attributes_default_values(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_city_attributes_types(self):
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_attributes_updated_at_and_created_at(self):
        city = City()
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_city_to_dict_method(self):
        city = City()
        self.assertEqual('to_dict' in dir(city), True)

    def test_city_name(self):
        city = City()
        city.name = "Bee"
        self.assertEqual(city.name, "Bee")

    def tearDown(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}
