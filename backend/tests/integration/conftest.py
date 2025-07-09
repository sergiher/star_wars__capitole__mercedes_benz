import pytest
from app.main import create_app  # type: ignore
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    """Provides a TestClient with overridden dependencies."""
    app = create_app()

    with TestClient(app) as client:
        yield client
