import logging
import os

from app.application.api import router  # type: ignore
from app.config import Settings  # type: ignore
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging_level = os.getenv("LOGGING_LEVEL", "DEBUG").upper()
logging.basicConfig(level=logging_level)
logger = logging.getLogger(__name__)


def create_app():
    logger.info("Creating app")
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            Settings.FRONTEND_WEB_BASE_URL,
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    return app


app = create_app()
