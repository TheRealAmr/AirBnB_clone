import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}

    def test_amenity_inherits_from_base_model(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_attributes_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_attributes_updated_at_and_created_at(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_amenity_to_dict_method(self):
        amenity = Amenity()
        self.assertEqual('to_dict' in dir(amenity), True)

    def test_amenity_name(self):
        amenity = Amenity()
        amenity.name = "Bee"
        self.assertEqual(amenity.name, "Bee")

    def tearDown(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}
