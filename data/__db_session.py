from logging import raiseExceptions
import ssl
import sqlalchemy as sqal
from sqlalchemy import orm
from sqlalchemy.orm import Session


from data.modelbase import Base

__session = None

# Session maker follows the Flask and Sqlalchemy session creation and factory creation pattern

def database_init(connection: str):
    global __session

    if __session:
        return

    if not connection:
        return raiseExceptions("The connection path has not been passed to the database_init")
    
    engine = sqal.engine.create_engine(connection)
    __session = orm.sessionmaker(engine, expire_on_commit=False)
    
    Base.metadata.create_all(engine)

def create_session():
    global __session

    session: Session = __session()

    return session