from sqlalchemy.orm import sessionmaker
from .database import engine

session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
