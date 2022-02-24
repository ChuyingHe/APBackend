import datetime

from pydantic import BaseModel
import enum

# multiple inheritance: from "str" and "enum)
class OrderStatusCode(str, enum):
    pending_payment = "Nicht bezahlt"
    processing = "In Bearbeitung"
    refunded = "Geld zurückgegeben"
    in_delivery= "Auf dem Weg"
    canceled = "storniert"
    completed = "erfolgreich"
    failed = "failed"
    # on_hold = "halt"

class OrderDetails(BaseModel):
    # TODO: Invoices, Shipme dnts, OrderItems
    pass

class Order(BaseModel):
    order_status_code: OrderStatusCode
    order_date: datetime.datetime
    # order_details: OrderDetails