import uuid

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    description: str
    user_id: uuid.UUID


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderCreate):
    pass


class OrderUpdatePartial(OrderCreate):
    description: str | None = None
    user_id: uuid.UUID | None = None


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    order_id: int
    description: str
    user_id: uuid.UUID
