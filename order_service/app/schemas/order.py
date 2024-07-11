import uuid

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    user_id: uuid.UUID
    description: str
    order_name: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderCreate):
    pass


class OrderUpdatePartial(OrderCreate):
    user_id: uuid.UUID | None = None
    description: str | None = None
    order_name: str | None = None


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    order_id: int
    user_id: uuid.UUID
    description: str
    order_name: str
