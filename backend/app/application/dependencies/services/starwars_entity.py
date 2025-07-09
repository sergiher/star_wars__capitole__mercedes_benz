from app.application.dependencies.repositories.starwars_entity import (  # type: ignore  # noqa: E501
    get_starwars_entity_repository,
)
from app.domain.repositories.starwars_entity_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityRepository,
)
from app.domain.services.starwars_entity_service import (  # type: ignore
    StarwarsEntityService,
)
from fastapi import Depends


def get_starwars_entity_service(
    starwars_entity_repository: StarwarsEntityRepository = Depends(
        get_starwars_entity_repository
    ),
) -> StarwarsEntityService:
    return StarwarsEntityService(
        starwars_entity_repository,
    )
