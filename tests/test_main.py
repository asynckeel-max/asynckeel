import pytest
from fastapi.testclient import TestClient
from your_application import app  # Replace with the actual import for your FastAPI application

client = TestClient(app)

def test_read_main():
    response = client.get("")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}  # Adjust according to your actual response

# Add more tests for other endpoints
