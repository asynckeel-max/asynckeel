# Getting Started with AsyncKeel

## Installation

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip or poetry package manager

### Step 1: Clone Repository

```bash
git clone https://github.com/asynckeel-max/asynckeel.git
cd asynckeel
```

### Step 2: Create Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost/asynckeel

# JWT
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server
DEBUG=True
HOST=0.0.0.0
PORT=8000

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
```
## Running the Application

### Development Mode
```bash
uvicorn app.main:app --reload
```
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```
## Database Setup
### Create Database
```bash
createdb asynckeel
```
### Run Migrations
```bash
alembic upgrade head
```
## Verification
Test the installation:

```bash
# Health check
curl http://localhost:8000/health

# Should return:
# {"status":"ok"}
```
## Next Steps

- Read the [API Reference](api-reference.md)
- Check [Architecture](architecture.md) documentation
- Review [Examples](../examples/)

## Troubleshooting

### Database Connection Error

```bash
Error: could not connect to server
```

**Solution:** Check PostgreSQL is running and DATABASE_URL is correct

### Port Already in Use

```bash
Address already in use
```

**Solution:** Change port in .env or kill process on port 8000

### Import Errors

```bash
ModuleNotFoundError
```

**Solution:** Ensure virtual environment is activated and dependencies installed
