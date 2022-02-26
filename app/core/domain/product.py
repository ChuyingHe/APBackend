from pydantic import BaseModel


class ProductType(BaseModel):
    soap = "Seife"
    essential_oil = "aetherisches_oel"


class Product(BaseModel):
    product_id: str
    product_name: str
    product_type: ProductType
    product_price: float
    product_color: str
    product_size: str
    product_weight: str
    product_smell: str
    product_ingredient: str


