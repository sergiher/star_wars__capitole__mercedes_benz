import os


class Settings:
    PROJECT_NAME: str = "Outfits app"
    PROJECT_VERSION: str = "1.0.0"
    FRONTEND_WEB_BASE_URL = os.getenv("FRONTEND_WEB_BASE_URL")


class Settings_tests:
    PROJECT_NAME: str = "Outfits app - tests"
    PROJECT_VERSION: str = "1.0.0"


settings = Settings()
settings_tests = Settings_tests()
