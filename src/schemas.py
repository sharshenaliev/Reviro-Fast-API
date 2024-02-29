from pydantic import BaseModel


class ProductGet(BaseModel):
    product_id: int
    name: str
    description: str
    price: int
    quantity_in_stock: int


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    quantity_in_stock: int


class EstablishmentGet(BaseModel):
    establishment_id: int
    name: str
    description: str
    location: str
    opening_hours: str


class EstablishmentCreate(BaseModel):
    name: str
    description: str
    location: str
    opening_hours: str
