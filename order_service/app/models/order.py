import uuid

from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    order_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(String, index=True, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "order_name",
            name="_user_order_uc",
        ),
    )
