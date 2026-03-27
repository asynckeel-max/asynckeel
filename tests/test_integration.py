import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_health_check():
    """Test API health check endpoint"""
    response = client.get("/")
    assert response.status_code == 200

def test_api_returns_json():
    """Test API returns valid JSON"""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"
