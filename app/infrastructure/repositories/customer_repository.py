from app.core.abstractions.customer_repository_base import CustomerRepositoryBase
from app.core.domain.customer import Customer

class CustomerRepository(CustomerRepositoryBase):
    def add(self, customer: Customer) -> Customer:
        pass