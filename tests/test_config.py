from app.core.config import Settings


def test_settings_load():
    """Test that settings can be loaded"""
    settings = Settings()
    assert settings is not None


def test_settings_default_values():
    """Test default settings values"""
    settings = Settings()
    assert settings.some_variable == "default_value"
    assert settings.another_variable == 42
