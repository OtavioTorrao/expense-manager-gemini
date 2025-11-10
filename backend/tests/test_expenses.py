import sys
sys.path.insert(0, "D:\\projectx\\backend")

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.database import Base, get_db
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_expense():
    response = client.post(
        "/api/v1/expenses/",
        json={"title": "Test Expense", "amount": 10.5, "description": "Test Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Expense"
    assert data["amount"] == 10.5
    assert data["description"] == "Test Description"
    assert "id" in data

def test_read_expenses():
    client.post(
        "/api/v1/expenses/",
        json={"title": "Test Expense 1", "amount": 10.5, "description": "Test Description 1"},
    )
    client.post(
        "/api/v1/expenses/",
        json={"title": "Test Expense 2", "amount": 20.5, "description": "Test Description 2"},
    )
    response = client.get("/api/v1/expenses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
