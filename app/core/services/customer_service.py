# use FUNCs here to wrap the FUNCs in *_repository_base.py
# so that the ABSTRACTED methods can be used
# while the implementation of the ABSTRACTS are under /infrastructure
from typing import List

from pydantic import BaseModel

from core.abstractions.customer_repository_base import CustomerRepositoryBase
from core.domain.customer import Customer

# TODO: WHY add extra WRAP on the ABC?
class CustomerService(BaseModel, CustomerRepositoryBase):
    def __init__(self, customer_repository_base: CustomerRepositoryBase):
        self._customer_repository_base = customer_repository_base

    def add_customer(self, customer: Customer) -> Customer:
        self._customer_repository_base.add_customer(customer)

    def get_customers(self) -> List[Customer]:
        self._customer_repository_base.get_customers()

    def get_customer(self, customer_id: str) -> Customer:
        self._customer_repository_base.get_customer()

    def update_customer(self, customer: Customer) -> Customer:
        self._customer_repository_base.update_customer()

    def delete_customer(self):
        self._customer_repository_base.delete_customer()