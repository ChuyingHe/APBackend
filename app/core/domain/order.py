import datetime
from typing import Optional, List

from pydantic import BaseModel
import enum

# multiple inheritance: from "str" and "enum)
from core.domain.product import Product


class OrderStatusCode(str, enum):
    pending_payment = "nicht bezahlt"
    processing = "in Bearbeitung"
    refunded = "Geld zurückgegeben"
    in_delivery = "suf dem Weg"
    canceled = "storniert"
    completed = "erfolgreich"
    failed = "failed"
    # on_hold = "halt"


class PaymentMethod(BaseModel):
    paypal = "Paypal"
    klarna = "Ueberweisung"


class Payment(BaseModel):
    payment_method: PaymentMethod
    account_name: Optional[str]
    card_number: Optional[str]


class Invoice(BaseModel):
    invoice_number: Optional[str]
    invoice_date: datetime.datetime
    invoice_amount: float
    payment_method: Payment
    # TODO: make sure product page is still available even its sold out!
    # paid products
    products: List[Product]


class Shipment(BaseModel):
    tracking_number: Optional[str]
    shipment_date: datetime.datetime
    shipment_agent: str
    # TODO: make sure product page is still available even its sold out!
    # shipped products
    products: List[Product]


class Order(BaseModel):
    order_id: str
    order_status_code: OrderStatusCode
    order_date: datetime.datetime
    invoice: Invoice
    shipment: Shipment
    # TODO: make sure product page is still available even its sold out!
    products: List[Product]
