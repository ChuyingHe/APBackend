from typing import List

from pydantic import BaseModel

from core.abstractions.product_repository_base import ProductRepositoryBase
from core.domain.product import Product


class ProductService(BaseModel):
    def __init__(self, product_repository_base: ProductRepositoryBase):
        self._product_repository_base = product_repository_base

    def add_product(self, product: Product) -> Product:
        self._product_repository_base.add_product(product)

    def get_products(self) -> List[Product]:
        self._product_repository_base.get_products()

    def get_product(self, product_id: str) -> Product:
        self._product_repository_base.get_product(product_id)

    def update_product(self, product_id: str) -> Product:
        self._product_repository_base.update_product(product_id)

    def delete_product(self):
        self._product_repository_base.delete_product()