import pytest
from unittest.mock import MagicMock
from uuid import UUID
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.application.category_repository import CategoryRepository


class TestCreateCategory:
    def test_create_category_with_calid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
            name="Move",
            description="All moves",
            is_active=True,
        )

        category_id = use_case.execute(request)
    
        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_repository.save.called is True

    def teste_create_category_with_invalid_data(self):
        # Crio 
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)

        # executo
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            
            category_id = use_case.execute(CreateCategoryRequest(name=""))

        # faço as asserts
        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"