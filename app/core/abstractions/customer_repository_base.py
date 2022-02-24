from abc import ABC, abstractmethod

from app.core.domain.customer import Customer

class CustomerRepositoryBase(ABC):
    # CRUD
    # C: add new customer
    @abstractmethod
    def add(self, customer: Customer) -> Customer:
        pass

    # R: get info of one custoner
    @abstractmethod
    def get_customer(self, customer_id: str) -> Customer:
        pass

    # U: update customer info
    @abstractmethod
    def update_customer(self, customer: Customer) -> Customer:
        pass

    # D: delete account of a customer
    @abstractmethod
    def delete_customer(self):
        pass