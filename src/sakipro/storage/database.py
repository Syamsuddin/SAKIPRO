from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sakipro.core.config import settings
from pathlib import Path
import os

# Ensure the database directory exists
db_path = Path(settings.db_path)
db_path.parent.mkdir(parents=True, exist_ok=True)

# SQLite URL format
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    """Initialize the database by creating all tables."""
    from sakipro.storage.models import Base
    Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency to get DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
