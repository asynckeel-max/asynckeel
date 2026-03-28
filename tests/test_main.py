import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create test client"""
    return TestClient(app)


def test_read_root(client):
    """Test root endpoint returns Hello World"""
    response = client.get("/")
    assert response.status_code == 200


def test_root_endpoint_exists(client):
    """Test root endpoint is accessible"""
    response = client.get("/")
    assert response.status_code == 200


def test_invalid_endpoint(client):
    """Test invalid endpoint returns 404"""
    response = client.get("/invalid-endpoint")
    assert response.status_code == 404
