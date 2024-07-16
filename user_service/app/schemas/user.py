import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    username: str | None = None
    email: EmailStr | None = None
    age: int | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: EmailStr
    age: int
