from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # Configuration variables
    some_variable: str = "default_value"
    another_variable: int = 42

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
