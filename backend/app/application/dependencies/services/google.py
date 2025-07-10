from app.infrastructure.external_services.google.gemini import (  # type: ignore  # noqa: E501
    GoogleService,
)


def get_google_service() -> GoogleService:
    return GoogleService()
