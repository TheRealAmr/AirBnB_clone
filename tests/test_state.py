import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):

    def setUp(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}

    def test_state_inherits_from_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_state_attributes_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attributes_types(self):
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_attributes_updated_at_and_created_at(self):
        state = State()
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_state_to_dict_method(self):
        state = State()
        self.assertEqual('to_dict' in dir(state), True)

    def test_state_name(self):
        state = State()
        state.name = "Bee"
        self.assertEqual(state.name, "Bee")

    def tearDown(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}
