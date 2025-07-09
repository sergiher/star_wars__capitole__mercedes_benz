import os


class Settings:
    PROJECT_NAME: str = "Starwars app"
    PROJECT_VERSION: str = "1.0.0"
    FRONTEND_WEB_BASE_URL = os.getenv("FRONTEND_WEB_BASE_URL")
    ENTITIES_LIST = os.getenv("ENTITIES_LIST")


# In case I have to use some config only for tests:
class Settings_tests:
    PROJECT_NAME: str = "Starwars app - tests"
    PROJECT_VERSION: str = "1.0.0"


settings = Settings()
settings_tests = Settings_tests()
