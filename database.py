from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_UR = "postgresql://postgres:postgres@127.0.0.1/test"

engine = create_engine(SQLALCHEMY_DB_UR)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)