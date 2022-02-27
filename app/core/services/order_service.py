from typing import List

from pydantic import BaseModel

from core.abstractions.order_repository_base import OrderRepositoryBase
from core.domain.order import Order


class OrderService(BaseModel):
    def __init__(self, order_repository_base: OrderRepositoryBase):
        self._order_repository_base = order_repository_base

    def add_order(self, order: Order) -> Order:
        self._order_repository_base.add_order(order)

    def get_order(self, order_id: str) -> Order:
        self._order_repository_base.get_order(order_id)

    def get_orders(self) -> List[Order]:
        self._order_repository_base.get_orders()

    def update_order(self, order_id: str) -> Order:
        self._order_repository_base.update_order(order_id)

    def delete_order(self, order_id: str):
        self._order_repository_base.delete_order()