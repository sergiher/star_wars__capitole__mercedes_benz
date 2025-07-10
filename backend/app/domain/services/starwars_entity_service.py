from typing import List

from app.domain.entities.starwars_entity import (  # type: ignore  # noqa: E501
    StarwarsEntity,
)
from app.domain.repositories.starwars_entity_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityRepository,
)
from app.domain.services.sorting_context import (  # type: ignore  # noqa: E501
    SortingContext,
)
from app.domain.services.sorting_factory import (  # type: ignore  # noqa: E501
    get_sorting_strategy,
)
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortAlgorithm,
    SortOptions,
)


class StarwarsEntityService:
    def __init__(self, starwars_entity_repository: StarwarsEntityRepository):
        self._repository = starwars_entity_repository

    def get_all_elements(self, entity_type) -> List[StarwarsEntity]:
        return self._repository.get_all_elements(entity_type)

    def sort_elements(
        self,
        starwars_elements: List[StarwarsEntity],
        sort_options: SortOptions,
    ) -> List[StarwarsEntity]:
        """Sort starwars_elements by sort_options"""
        algorithm = sort_options.algorithm or SortAlgorithm.POWER_SORT
        strategy = get_sorting_strategy(algorithm)
        return SortingContext(strategy).sort_data(
            data=starwars_elements,
            sort_by=sort_options.field,
            direction=sort_options.direction,
        )
