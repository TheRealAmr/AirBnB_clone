import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):

    def setUp(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}

    def test_review_inherits_from_base_model(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attributes_default_values(self):
        review = Review()
        self.assertEqual(review.text, "")

    def test_review_attributes_types(self):
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_review_attributes_updated_at_and_created_at(self):
        review = Review()
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_review_to_dict_method(self):
        review = Review()
        self.assertEqual('to_dict' in dir(review), True)

    def test_review_place_id(self):
        review = Review()
        review.place_id = "Bee"
        self.assertEqual(review.place_id, "Bee")

    def tearDown(self):
        if hasattr(FileStorage, "_FileStorage__objects"):
            FileStorage._FileStorage__objects = {}
