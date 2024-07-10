import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class DbSettings(BaseModel):
    url: str = os.getenv("DB_URL")
    # echo: bool = False
    echo: bool = True


class Settings(BaseSettings):

    db: DbSettings = DbSettings()


settings = Settings()
