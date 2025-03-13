# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

#database connection handler
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#database initialization
def init_db():
    from models import Base
    Base.metadata.create_all(bind=engine)
