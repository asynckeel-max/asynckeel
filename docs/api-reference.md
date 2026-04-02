# API Reference ## 
Base URL http://localhost:8000 
## Authentication 
All requests (except login/register) require JWT token in header: ```
```json
Authorization: Bearer <your_token>
``` 
## Response 
Format All responses are JSON with following structure: 
### Success Response
```json
{
  "data": {},
  "status": "success",
  "code": 200
}
```
### Error Response
```json
{
  "detail": "Error message",
  "status": "error",
  "code": 400
}
```
## Endpoints 
### Error Response 
#### Health Check 
**GET** `/health` 

Check API health status.

**Response:**
```json
{
  "status": "ok"
}
```
### Authentication 
**POST** 
`/auth/register`

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "password": "securepassword123"
}
```
**Response:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe"
}
```
### Login 
**POST** `/auth/login` 

**Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```
**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 1800
}
```
### USERS ###
#### GET Current User 

**GET** `/users/me` 

**Headers:**
```json
Authorization: Bearer <token>
```
**Response:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe"
}
```

#### Get User by ID

**GET** `/users/{id}`

**Headers:**

```json
Authorization: Bearer <token>
```
***Response:***

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe"
}
```

#### Update User

**PUT** `/users/{id}`

**Headers:**

```json
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "full_name": "John Updated",
  "email": "newemail@example.com"
}
```
***Response:***

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "newemail@example.com",
  "full_name": "John Updated"
}
```

#### Delete User

**DELETE** `/users/{id}`

**Headers:**

```json
Authorization: Bearer <token>
```
***Response:***

```json
{
  "message": "User deleted successfully"
}
```
### ERROR CODES ###
| Code    | Message | Meaning |
| -------- | ------- |------- |
| 200  | OK    | Request successful |
| 400 | Bad Request     |Invalid request data|
| 401    | Unauthorized    |Missing or invalid token|
| 403    | Forbidden    |No permission for resource|
| 404    | Not Found    |Resource not found|
| 409    | Conflict    |Resource already exists|
| 500    | Internal Server Error    | Server error|

### RATE LIMITTING ###

Currently no rate limiting implemented. Production deployments should implement rate limiting using middleware like `slowapi.`

### PAGINATION ###

List endpoints support pagination:
```
GET /users?skip=0&limit=10
```

Query Parameters:

- `skip` (int): Number of items to skip
- `limit` (int): Max items to return (default: 10, max: 100)

**Response:**

```json
{
  "total": 42,
  "items": [],
  "skip": 0,
  "limit": 10
}
```
