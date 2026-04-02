# examples/organizations.py
"""
Organizations Example

Demonstrates:
- Create organization
- List organizations
- Get organization details
- Update organization
- Delete organization
"""

import requests
import json

BASE_URL = "http://localhost:8000"
TOKEN = "your_jwt_token_here"  # Get from login example


def get_headers():
    """Get authorization headers"""
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }


def create_organization(name: str, description: str):
    """Create a new organization"""
    print("\n=== CREATING ORGANIZATION ===")
    
    org_data = {
        "name": name,
        "description": description
    }
    
    response = requests.post(
        f"{BASE_URL}/organizations",
        json=org_data,
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data if response.status_code == 200 else None


def list_organizations(skip: int = 0, limit: int = 10):
    """List all organizations"""
    print(f"\n=== LISTING ORGANIZATIONS (skip={skip}, limit={limit}) ===")
    
    params = {
        "skip": skip,
        "limit": limit
    }
    
    response = requests.get(
        f"{BASE_URL}/organizations",
        params=params,
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data if response.status_code == 200 else None


def get_organization(org_id: int):
    """Get organization details"""
    print(f"\n=== GETTING ORGANIZATION {org_id} ===")
    
    response = requests.get(
        f"{BASE_URL}/organizations/{org_id}",
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data if response.status_code == 200 else None


def update_organization(org_id: int, name: str = None, description: str = None):
    """Update organization"""
    print(f"\n=== UPDATING ORGANIZATION {org_id} ===")
    
    update_data = {}
    if name:
        update_data["name"] = name
    if description:
        update_data["description"] = description
    
    response = requests.put(
        f"{BASE_URL}/organizations/{org_id}",
        json=update_data,
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data if response.status_code == 200 else None


def delete_organization(org_id: int):
    """Delete organization"""
    print(f"\n=== DELETING ORGANIZATION {org_id} ===")
    
    response = requests.delete(
        f"{BASE_URL}/organizations/{org_id}",
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    if response.text:
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)}")
    
    return response.status_code == 200


def add_member(org_id: int, user_id: int, role: str = "member"):
    """Add member to organization"""
    print(f"\n=== ADDING MEMBER TO ORGANIZATION {org_id} ===")
    
    member_data = {
        "user_id": user_id,
        "role": role
    }
    
    response = requests.post(
        f"{BASE_URL}/organizations/{org_id}/members",
        json=member_data,
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data if response.status_code == 200 else None


def list_members(org_id: int):
    """List organization members"""
    print(f"\n=== LISTING MEMBERS OF ORGANIZATION {org_id} ===")
    
    response = requests.get(
        f"{BASE_URL}/organizations/{org_id}/members",
        headers=get_headers()
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}")
    
    return data if response.status_code == 200 else None


def main():
    """Run organization examples"""
    print("=" * 60)
    print("AsyncKeel Organizations Example")
    print("=" * 60)
    print("\nNote: Update TOKEN variable with your JWT token from login")
    
    # Create organizations
    org1 = create_organization("Acme Corporation", "Enterprise SaaS Company")
    if not org1:
        print("Failed to create organization!")
        return
    
    org_id = org1.get("id")
    
    org2 = create_organization("TechStart Inc", "Technology Startup")
    
    # List organizations
    orgs = list_organizations(limit=5)
    
    # Get organization details
    org_details = get_organization(org_id)
    
    # Update organization
    updated_org = update_organization(
        org_id,
        name="Acme Corporation Updated",
        description="Enterprise SaaS Company - Updated"
    )
    
    # Add members (if endpoints exist)
    # add_member(org_id, user_id=1, role="admin")
    # list_members(org_id)
    
    # Delete organization
    # delete_organization(org_id)
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
