import logging
from typing import List

from app.application.dependencies.services.starwars_entity import (  # type: ignore  # noqa: E501
    get_starwars_entity_service,
)
from app.application.dto import StarWarsElement  # type: ignore
from app.config import Settings  # type: ignore
from app.domain.services.starwars_entity_service import (  # type: ignore  # noqa: E501
    StarwarsEntityService,
)
from fastapi import APIRouter, Depends, HTTPException

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/{entity_type}",
    response_model=List[StarWarsElement],
)
def get_elements(
    entity_type: str,
    starwars_entity_service: StarwarsEntityService = Depends(
        get_starwars_entity_service
    ),
):
    if entity_type not in Settings.ENTITIES_LIST:
        raise HTTPException(status_code=400, detail="Invalid entity type")  # noqa: E501
    data = starwars_entity_service.get_all_elements(entity_type)
    return data
