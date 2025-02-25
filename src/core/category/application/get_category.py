from uuid import UUID
from dataclasses import dataclass
from src.core.category.domain.category import Category
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.application.category_repository import CategoryRepository


@dataclass
class GetCategoryRequest:
    id: UUID

@dataclass
class GetCategoryResponse:
    id: UUID
    name: str
    description: str = ""
    is_active: bool = True

class GetCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self,request: GetCategoryRequest) -> GetCategoryResponse:
            category = self.repository.get_by_id(id=request.id)

            return GetCategoryResponse(
                 id=category.id,
                 name=category.name,
                 description=category.description,
                 is_active=category.is_active,
            )