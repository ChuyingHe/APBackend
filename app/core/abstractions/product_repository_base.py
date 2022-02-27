from abc import ABC, abstractmethod
from typing import List

from core.domain.product import Product


class ProductRepositoryBase(ABC):
    # CRUD
    @abstractmethod
    def add_product(self) -> Product:
        pass

    @abstractmethod
    def get_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def update_product(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def delete_product(self):
        pass