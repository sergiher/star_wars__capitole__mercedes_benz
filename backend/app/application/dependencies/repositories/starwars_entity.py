import os
from functools import lru_cache

from app.domain.repositories.starwars_entity_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityRepository,
)
from app.infrastructure.api_repositories.starwars_entity_api_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityApiRepository,
)


@lru_cache()
def get_starwars_entity_repository() -> StarwarsEntityRepository:
    return StarwarsEntityApiRepository(
        base_url=os.getenv("SWAPI_BASE_URL", "https://swapi.info/api"),
        timeout=int(os.getenv("SWAPI_TIMEOUT", "30")),
    )
