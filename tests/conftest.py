import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """
    Create a test client for the FastAPI application.

    Returns:
        TestClient: A test client for the FastAPI application
    """
    return TestClient(app)
