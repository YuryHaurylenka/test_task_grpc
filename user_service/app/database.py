import database.config
from database.db_helper import db_helper


def get_db():
    yield db_helper.scoped_session_dependency()


settings = database.config.settings()
