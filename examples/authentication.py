# examples/authentication.py
"""
Authentication Example

Demonstrates:
- User registration
- User login
- Token usage
- Accessing protected endpoints
"""

import requests
import json

BASE_URL = "http://localhost:8000"


def register_user():
    """Register a new user"""
    print("\n=== REGISTERING USER ===")
    
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "password": "SecurePassword123!"
    }
    
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=user_data
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.json() if response.status_code == 200 else None


def login_user(username: str, password: str):
    """Login user and get access token"""
    print("\n=== LOGGING IN USER ===")
    
    login_data = {
        "username": username,
        "password": password
    }
    
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json=login_data
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data.get("access_token") if response.status_code == 200 else None


def get_current_user(token: str):
    """Get current authenticated user"""
    print("\n=== GETTING CURRENT USER ===")
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(
        f"{BASE_URL}/users/me",
        headers=headers
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.json() if response.status_code == 200 else None


def update_user(token: str, user_id: int):
    """Update user information"""
    print("\n=== UPDATING USER ===")
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    update_data = {
        "full_name": "John Updated",
        "email": "newemail@example.com"
    }
    
    response = requests.put(
        f"{BASE_URL}/users/{user_id}",
        json=update_data,
        headers=headers
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.json() if response.status_code == 200 else None


def delete_user(token: str, user_id: int):
    """Delete user"""
    print("\n=== DELETING USER ===")
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.delete(
        f"{BASE_URL}/users/{user_id}",
        headers=headers
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.status_code == 200


def main():
    """Run authentication examples"""
    print("=" * 50)
    print("AsyncKeel Authentication Example")
    print("=" * 50)
    
    # Health check
    print("\n=== HEALTH CHECK ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Register user
    user = register_user()
    if not user:
        print("Registration failed!")
        return
    
    user_id = user.get("id")
    
    # Login
    token = login_user("john_doe", "SecurePassword123!")
    if not token:
        print("Login failed!")
        return
    
    # Get current user
    current_user = get_current_user(token)
    
    # Update user
    updated_user = update_user(token, user_id)
    
    # Delete user
    # delete_user(token, user_id)
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
