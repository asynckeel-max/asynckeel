# Architecture

## Overview

AsyncKeel follows a clean, layered architecture pattern for maintainability, testability, and scalability.

## Directory Structure

```
app/
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   └── organizations.py
│   │   └── api.py
│   └── dependencies.py
├── core/
│   ├── config.py
│   ├── security.py
│   └── database.py
├── db/
│   ├── database.py
│   └── session.py
├── models/
│   ├── user.py
│   └── organization.py
├── repositories/
│   ├── user.py
│   └── organization.py
├── schemas/
│   ├── user.py
│   └── organization.py
├── services/
│   ├── user.py
│   └── organization.py
└── main.py
```


## Architecture Layers

### 1. API Layer (Route Handlers)

**Location:** `app/api/`

Handles HTTP requests and responses. Converts JSON to Pydantic models.

```python
# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user_data)
```
#### Responsibilities:

- Route definition
- Request validation (via Pydantic)
- Response serialization
- Error handling

### 2. Service Layer (Business Logic)
**Location:** `app/services/`

Contains all business logic. Orchestrates repositories and other services.

```python
# app/services/user.py
from app.repositories.user import UserRepository
from app.core.security import hash_password
from app.schemas.user import UserCreate

class UserService:
    @staticmethod
    def create_user(db, user_data: UserCreate):
        # Hash password
        hashed_pwd = hash_password(user_data.password)
        user_data.password = hashed_pwd
        
        # Save via repository
        return UserRepository.create(db, user_data)
    
    @staticmethod
    def authenticate(db, username: str, password: str):
        user = UserRepository.get_by_username(db, username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user
```

#### Responsibilities:

- Business logic
- Validation
- Orchestration
- Transaction management

### 3. Repository Layer (Data Access)
**Location:** `app/repositories/`

Abstracts database operations. Single point of data access.
```python
# app/repositories/user.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    @staticmethod
    def create(db: Session, user: UserCreate) -> User:
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_by_username(db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()
```

#### Responsibilities:

- CRUD operations
- Query building
- Database transactions
- Data mapping

### 4. Model Layer (Database Schema)
**Location:** `app/models/`

SQLAlchemy ORM models representing database tables.
```python
# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
```

#### Responsibilities:

- Table definition
- Column definition
- Relationships
- Constraints

### 5. Schema Layer (Data Validation)
**Location:** `app/schemas/`

Pydantic models for request/response validation.

```python
# app/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True
```
#### Responsibilities:

- Request validation
- Response serialization
- Type checking
- Documentation

### Data Flow
```
HTTP Request
    ↓
[API Layer] - Route handler, validation
    ↓
[Service Layer] - Business logic
    ↓
[Repository Layer] - Data access
    ↓
[Model Layer] - Database operations
    ↓
Database
    ↓
[Model Layer] - Database result
    ↓
[Repository Layer] - Map to model
    ↓
[Service Layer] - Process data
    ↓
[Schema Layer] - Serialize to response
    ↓
[API Layer] - Return JSON
    ↓
HTTP Response
```

### Key Design Patterns
#### Dependency Injection
Using FastAPI's `Depends()` for injection:
```python
@app.get("/users/me")
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    pass
```
#### Repository Pattern
Abstraction for data access:
```python
# In service
user = UserRepository.get_by_id(db, user_id)

# Can be swapped with any implementation
# Memory, SQL, NoSQL, API, etc.
```
#### Service Locator
Central configuration and initialization:
```python
# app/core/config.py
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    # ...
```
### Security Architecture
#### Authentication Flow

```
User Login
    ↓
Validate Credentials (UserService.authenticate)
    ↓
Generate JWT Token (security.create_access_token)
    ↓
Return Token to Client
    ↓
Client Includes Token in Authorization Header
    ↓
FastAPI Validates Token (Depends)
    ↓
Allow Request to Proceed
```
#### Password Security

```
User Registration
    ↓
Receive Plain Password
    ↓
Hash Password (bcrypt)
    ↓
Store Hashed Password in Database
    ↓
User Login
    ↓
Hash Provided Password
    ↓
Compare with Stored Hash
    ↓
Match = Success, Mismatch = Failure
```
### Testing Strategy

#### Unit Tests

Test individual components in isolation:
```python
# tests/test_services/test_user.py
def test_create_user(mock_db):
    user_data = UserCreate(...)
    result = UserService.create_user(mock_db, user_data)
    assert result.username == user_data.username
```

#### Integration Tests
Test layer interactions:
```python
# tests/test_integration/test_user_flow.py
def test_create_and_login_user(test_db, client):
    # Create user
    response = client.post("/auth/register", json={...})
    assert response.status_code == 200
    
    # Login
    response = client.post("/auth/login", json={...})
    assert "access_token" in response.json()
```

### Performance Considerations
#### Database Optimization
- Use indexes on frequently queried columns
- Lazy load relationships
- Pagination for list endpoints

#### Caching
Consider implementing:

- Redis for session/token caching
- Query result caching
- Response caching

#### Async Support
FastAPI supports async:
```python
@app.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    users = await db.execute(select(User))
    return users.scalars().all()
```
### Scalability

#### Horizontal Scaling
- Stateless API layer
- Shared database
- Load balancer (nginx, HAProxy)
#### Vertical Scaling
 Database optimization
- Connection pooling
- Query optimization
#### Microservices Readiness
- Current architecture easily splits into:
- Auth service
- User service
- Organization service
- etc.

