import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):

    def setUp(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}

    def test_user_inherits_from_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_attributes_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_types(self):
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_attributes_updated_at_and_created_at(self):
        user = User()
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_user_to_dict_method(self):
        user = User()
        self.assertEqual('to_dict' in dir(user), True)

    def test_user_email(self):
        user = User()
        user.email = "Bee@me"
        self.assertEqual(user.email, "Bee@me")

    def tearDown(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}
