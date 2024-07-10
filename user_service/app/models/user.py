import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
