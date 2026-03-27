from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./test.db"  # Example: Change this to your actual database URL

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, connect_args={{"check_same_thread": False}})

# Create a configured "Session" class
t SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a session

def get_db():
    # Dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()