from abc import ABC, abstractmethod
from typing import List

from core.domain.order import Order


class OrderRepositoryBase(ABC):
    @abstractmethod
    def add_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def get_orders(self) -> List[Order]:
        pass

    @abstractmethod
    def update_order(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def delete_order(self, order_id: str):
        pass