import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Create test client"""
    return TestClient(app)

def test_api_health_check(client):
    """Test API health check endpoint"""
    response = client.get("/")
    assert response.status_code == 200

def test_api_response_type(client):
    """Test API response content type"""
    response = client.get("/")
    assert response.status_code == 200
    # Check if response is JSON or has content
    assert response.text