import uuid

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    username: str | None = None
    email: str | None = None
    age: int | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: uuid.UUID
    name: str
    email: str
    age: int
