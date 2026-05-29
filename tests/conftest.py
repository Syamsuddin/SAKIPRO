import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sakipro.storage.models import Base

@pytest.fixture(scope="function")
def db_session():
    # Use an in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
