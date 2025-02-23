import pytest
import uuid
from uuid import UUID, uuid4
from src.core.category.domain.category import Category

class TestCategory:

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            Category(name="a" * 256)
    
    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Move")
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Move")
        assert category.name == "Move"
        assert category.description == ""
        
    def test_created_category_is_active_by_default(self):
        category = Category(name="Move")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Move",
            description="All moves",
            is_active=False
        )

        assert category.id == cat_id
        assert category.name == "Move"
        assert category.description == "All moves"
        assert category.is_active == False 

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")   

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Move", description="All moves")

        category.update_category("Series", description="All series")

        assert category.name == "Series"
        assert category.description == "All series"

    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="Move", description="All moves")

        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            category.update_category(name="a" * 256, description="All moves")

    def test_cannot_update_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")   

class TestActivate:
    def test_activate_inactive_category(self):
        category = Category(
            name="Move", 
            description="All moves",
            is_active = False,
            )

        category.activate()

        assert category.is_active is True

    def test_activate_active_category(self):
        category = Category(
            name="Move", 
            description="All moves",
            is_active = True,
            )

        category.activate()

        assert category.is_active is True

class TestDesactivate:
    def test_inactivate_inactive_category(self):
        category = Category(
            name="Move", 
            description="All moves",
            is_active = False,
            )

        category.desactivate()

        assert category.is_active is False

    def test_inactivate_activate_category(self):
        category = Category(
            name="Move", 
            description="All moves",
            is_active = True,
            )

        category.desactivate()

        assert category.is_active is False