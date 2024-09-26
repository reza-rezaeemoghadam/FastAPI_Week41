from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import env

SQLALCHEMY_DATABASE_URL = f"postgresql://{env.SQL_USER}:{env.SQL_PASSWORD}@127.0.0.1:{env.SQL_PORT}/{env.SQL_DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()