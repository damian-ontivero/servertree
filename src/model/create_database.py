"""Doc."""

from model import db

from sqlalchemy_utils import database_exists, create_database


if not database_exists(db.engine.url):
    create_database(db.engine.url)
