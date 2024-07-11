import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class DbSettings(BaseModel):
    url: str = os.getenv("DB_URL")
    # echo: bool = False
    echo: bool = True


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    orders: str = "/orders"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8001


class Settings(BaseSettings):

    db: DbSettings = DbSettings()
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
