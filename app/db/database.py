from sqlalchemy import create_engine

db_url = "postgresql://postgres:1234@localhost:5432/fastapi-play"
engine = create_engine(db_url)
