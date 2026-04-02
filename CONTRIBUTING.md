# Contributing to AsyncKeel

Thank you for your interest in contributing to AsyncKeel! We welcome contributions from everyone.

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 12+
- Git
- Virtual environment

### Development Setup

```bash
# Clone repository
git clone https://github.com/asynckeel-max/asynckeel.git
cd asynckeel

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 isort

# Create .env file
cp .env.example .env

# Run migrations
alembic upgrade head
```
## Code Standards
### Style Guide
We follow PEP 8 with the following additions:

- Line length: 88 characters (Black default)
- Imports: Sorted with isort
- Type hints: Required for all functions
### Formatting
```bash
# Format code with Black
black app/

# Sort imports
isort app/

# Lint with flake8
flake8 app/
```
### Pre-commit Hooks
Install pre-commit hooks (optional but recommended):

```bash
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```
### Testing
#### Running Tests
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_auth.py

# Run with coverage
pytest --cov=app
```
#### Writing Tests
- Create tests in `tests/` directory
- Use `test_` prefix for test files
- Use `test_` prefix for test functions
- Mock external dependencies
- Aim for >80% code coverage
***Example test:***

```python
# tests/test_services/test_user.py
import pytest
from app.services.user import UserService
from app.schemas.user import UserCreate

def test_create_user(mock_db):
    """Test user creation"""
    user_data = UserCreate(
        username="john_doe",
        email="john@example.com",
        full_name="John Doe",
        password="SecurePassword123!"
    )
    
    result = UserService.create_user(mock_db, user_data)
    assert result.username == "john_doe"
    assert result.email == "john@example.com"
```
### Git Workflow
#### Branch Naming
Use descriptive branch names:

```
feature/user-authentication
bugfix/login-error
docs/api-reference
refactor/database-layer
```
#### Commit Messages
Write clear, descriptive commit messages:

```
Good:
- Add user authentication endpoint
- Fix database connection timeout
- Update API documentation

Avoid:
- fix bug
- update stuff
- asdf
```
#### Pull Request Process
1. Fork the repository

2. Create a feature branch from `main`

```bash
git checkout -b feature/your-feature-name
```
3. Make your changes

4. Commit with clear messages

```bash
git commit -m "Add user authentication endpoint"
```
5. Push to your fork

```bash
git push origin feature/your-feature-name
```
6. Open a Pull Request with:

- Clear description of changes
- Reference to related issues
- Screenshots/examples if applicable
7. Wait for review and address feedback

8. Squash commits if requested

## PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Related Issues
Closes #123

## Testing
- [ ] Added unit tests
- [ ] Added integration tests
- [ ] All tests pass

## Documentation
- [ ] Updated README
- [ ] Updated API docs
- [ ] Updated code comments
```
## Documentation
### Code Comments
- Comment why, not what
- Use docstrings for functions and classes
```python
# Good
def hash_password(password: str) -> str:
    """
    Hash password using bcrypt for secure storage.
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Avoid
def hash_password(password: str) -> str:
    # Hash the password
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```
### Documentation Updates
- Update docs when adding features
- Keep examples up-to-date
- Update CHANGELOG.md
## Issues
### Reporting Issues
- Use issue templates
- Include reproduction steps
- Include error messages and logs
- Include environment info (Python version, OS, etc.)
### Issue Labels
`bug` - Bug reports
`enhancement` - Feature requests
`documentation` - Documentation improvements
`good first issue` - Good for new contributors
`help wanted` - Need community help

## Review Process
### Code Review Guidelines
- Be respectful and constructive
- Ask questions, don't demand
- Suggest improvements
- Approve when satisfied
### Common Feedback
- Missing error handling
- Insufficient tests
- Performance concerns
- Security issues
- Documentation gaps
## Development Tips
### Useful Commands
```bash
# Run development server
uvicorn app.main:app --reload

# Access API docs
# http://localhost:8000/docs

# Create database
createdb asynckeel

# Run migrations
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "Description"
```
## Project Structure
Familiarize yourself with the architecture:

[Architecture Documentation](/docs/architecture.md)

- API layer: `app/api/`
- Services: `app/services/`
- Database: `app/models/`, `app/repositories/`

## Community
**Discussions:** GitHub Discussions for Q&A
**Issues:** GitHub Issues for bugs and features
**Email:** Contact maintainers for other questions
## Code of Conduct
- Be respectful
- No harassment or discrimination
- Report violations to maintainers
## Questions?
- Check [Getting Started](/docs/getting-started.md)
- Check [API Reference](/docs/api-reference.md)
- Open a discussion in GitHub Discussions
- Create an issue
Thank you for contributing! 🎉
