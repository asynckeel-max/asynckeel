from pydantic import BaseSettings

class Settings(BaseSettings):
    # Configuration variables
    some_variable: str = 'default_value'
    another_variable: int = 42

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()