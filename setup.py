from setuptools import find_packages, setup

setup(
    name="asynckeel",
    version="0.1.0",
    description="Async Keel - Advanced async framework",
    author="AsyncKeel",
    author_email="asynckeel@gmail.com",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "fastapi==0.109.0",
        "uvicorn[standard]==0.27.0",
        "sqlalchemy==2.0.23",
        "pydantic==2.5.0",
        "pydantic-settings==2.1.0",
        "email-validator==2.1.0",
        "passlib[bcrypt]==1.7.4",
        "bcrypt==4.1.1",
    ],
)
