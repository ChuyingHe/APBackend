import sqlalchemy
from sqlalchemy_utils import database_exists, create_database

from lagom.environment import Env

# TODO: Get parameters from ENV configuration, use ./.env instead
from pydantic import PostgresDsn
# ORM=Object–relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between incompatible type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language.
from sqlalchemy.orm import Session

from infrastructure.database.db_domain import Base


class DBConfig(Env):
    psql_scheme: str
    psql_user: str
    psql_pw: str
    psql_host: str
    psql_db: str

# def config_db(config: DBConfig):
def config_db():
    # 1. create a postgres DSN style URL
    # dsn = PostgresDsn.build(
    #     scheme=config.psql_scheme.strip(),
    #     user=config.psql_user.strip(),
    #     password=config.psql_pw.strip(),
    #     host=config.psql_host.strip(),
    #     path=config.psql_db.strip()
    # )

    # DSN=Data/Database Source Name
    dsn = PostgresDsn.build(
        scheme="postgresql",
        user="root",
        password="top_secret",
        host="localhost",
        path="/asianpearl_db"
    )

    print("🉐️ DSN format URL = ", dsn)

    # 2. create new DB-Engine
    # dsn = "postgresql://root:top_secret@localhost/asianpearl_db"
    engine = sqlalchemy.create_engine(dsn)

    # 3. Create all tables stored in this metadata. (db_domain.py)
    try:
        Base.metadata.create_all(engine)
    except Exception as error:
        print("not able to connect to the database")
        print("Oops! An exception has occured:", error)
        print("Exception TYPE:", type(error))

    # TODO: return Session or Engine?
    session = Session(engine)
    return session

# Engine is the lowest level object used by SQLAlchemy. It maintains a pool of connections available for use whenever the application needs to talk to the database.
# Session use connections and transactions in the background, to run their automatically-generated SQL statements.