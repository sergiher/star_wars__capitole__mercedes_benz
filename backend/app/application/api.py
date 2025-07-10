import logging
from typing import List, Optional

from app.application.dependencies.services.starwars_entity import (  # type: ignore  # noqa: E501
    get_starwars_entity_service,
)
from app.application.dto import SortOptions, StarWarsElement  # type: ignore
from app.domain.services.starwars_entity_service import (  # type: ignore  # noqa: E501
    StarwarsEntityService,
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
    elements = starwars_entity_service.get_all_elements(entity_type)
    if sort_options is None:
        return elements

    sorted_elements = starwars_entity_service.sort_elements(
        elements, sort_options
    )  # noqa: E501
    return sorted_elements
