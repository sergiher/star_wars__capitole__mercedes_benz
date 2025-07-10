import logging
from typing import List, Optional

from app.application.dependencies.services.google import (  # type: ignore  # noqa: E501
    get_google_service,
)
from app.application.dependencies.services.starwars_entity import (  # type: ignore  # noqa: E501
    get_starwars_entity_service,
)
from app.application.dto import SortOptions, StarWarsElement  # type: ignore
from app.domain.services.starwars_entity_service import (  # type: ignore  # noqa: E501
    StarwarsEntityService,
)
from app.infrastructure.external_services.google.gemini import (  # type: ignore  # noqa: E501
    GoogleService,
)
from fastapi import APIRouter, Body, Depends

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    "/sort/{entity_type}",
    response_model=List[StarWarsElement],
)
def sort_starwars_entities(
    entity_type: str,
    sort_options: Optional[SortOptions] = Body(default=None),
    starwars_entity_service: StarwarsEntityService = Depends(
        get_starwars_entity_service
    ),
):
    logger.info(f"--------- Sort event: sort_options: {sort_options} ---------")

    elements = starwars_entity_service.get_all_elements(entity_type)
    if sort_options is None:
        return elements

    sorted_elements = starwars_entity_service.sort_elements(
        elements, sort_options
    )  # noqa: E501
    return sorted_elements


@router.post(
    "/simulate-ai-insight/{entity_type}/{name}",
    response_model=str,
)
def simulate_ai_insight(
    entity_type: str,
    name: str,
    google_service: GoogleService = Depends(get_google_service),
):  # noqa: E501
    question_to_the_ai = (
        "please, explain me, in 50 words or less, about the "
        + entity_type
        + " "
        + name
        + ", from the Star Wars universe"
    )  # noqa: E501
    return google_service.explain_about(input_text=question_to_the_ai)
