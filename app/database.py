from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

db_username = 'postgres'
db_password = 'PostgreSQL1923!'
db_name = 'fastapi'
db_adress = 'localhost:5433'

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:\
{settings.database_password}@\
{settings.database_hostname}:\
{settings.database_port}/\
{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
