# AsyncKeel - Enterprise SaaS Platform Builder

**Status:** This repository contains documentation and examples. Production code is in the private repository.

## 📚 Documentation

- [Getting Started](docs/getting-started.md) - Installation & setup guide
- [API Reference](docs/api-reference.md) - Complete API documentation
- [Architecture](docs/architecture.md) - System architecture & design

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 12+
- pip or poetry

### Installation

```bash
git clone https://github.com/asynckeel-max/asynckeel.git
cd asynckeel
pip install -r requirements.txt
```

## ▶️ Running the Application

### Development Mode

```bash
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📖 Examples

See the examples/ directory for usage examples:

- [Authentication](examples/authentication.py)
- [Organizations](examples/organizations.py)

## 🔐 Security

- JWT-based authentication
- Password hashing with bcrypt
- CORS protection
- API key management

## 📝 License
MIT License - see [LICENSE](https://github.com/asynckeel-max/asynckeel/blob/main/LICENSE) file for details

## 🤝 Contributing
See [CONTRIBUTING.md](https://github.com/asynckeel-max/asynckeel/blob/main/CONTRIBUTING.md) for contribution guidelines.
