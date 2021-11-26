"""Doc."""

from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy import (  # noqa: F401
    Table,
    Column
)
from sqlalchemy import (  # noqa: F401
    Integer,
    String,
    Boolean,
    Float,
    DateTime,
    Text,
    Enum,
    ForeignKey
)
from sqlalchemy.orm import sessionmaker, relationship  # noqa: F401
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

config_file = "./config.ini"
config = ConfigParser()
config.read(config_file)

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    config.get("database", "user"),
    config.get("database", "pass"),
    config.get("database", "host"),
    config.get("database", "port"),
    config.get("database", "database")
)
autocommit = config.getboolean("database", "autocommit")

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine, autocommit=autocommit)
session = Session()
