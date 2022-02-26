import base64
from typing import Optional

from pydantic import BaseModel
import enum


class Gender(str, enum):
    male = "männlich"
    female = "weblich"


class Customer(BaseModel):
    customer_id: str
    organisation_or_person: bool
    organisation_name: Optional[str]
    gender: Optional[Gender]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email_address: str
    login_name: str
    login_password: str
    phone_number: Optional[str]
    address_part_1: str
    address_part_2: Optional[str]
    address_part_3: Optional[str]
    address_part_4: Optional[str]
    town_city: str
    state: str
    country: str
