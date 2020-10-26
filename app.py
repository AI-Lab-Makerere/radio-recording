from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from settings import DATABASE_URL
from storage.base import BaseModel


def initialize() -> None:
    engine = create_engine(
        DATABASE_URL,
        echo=True
    )

    session_factory = sessionmaker(bind=engine)

    session = scoped_session(session_factory)
    BaseModel.set_session(session=session)
    BaseModel.prepare(engine, reflect=True)  # BaseModel.metadata.create_all(engine)


def run() -> None:
    # We will add the argument parser library for python and determine what command is to be run
    # record to start off recorder
    # migrate to migrate sql
    # clean to wipe out all tables and rollback
    pass
