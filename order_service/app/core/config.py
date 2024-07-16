import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class DbSettings(BaseModel):
    url: str = os.getenv("DB_URL")
    echo: bool = False


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    orders: str = "/orders"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):

    db: DbSettings = DbSettings()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
