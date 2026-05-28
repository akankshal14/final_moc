from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

DATABASE_URL=settings.get_database_url()
engine=create_engine(DATABASE_URL)
session=sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
