import unittest
from category import Category
from uuid import UUID

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category(name="a" * 256)
    
    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Move")
        self.assertEqual(type(category.id), UUID)

if __name__ == "__main__":
    unittest.main()