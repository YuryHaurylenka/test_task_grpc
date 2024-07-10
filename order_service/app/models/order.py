import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, default=uuid.uuid4, index=True)
    description = Column(String, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
