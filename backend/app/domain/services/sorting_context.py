from typing import List

from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore
from app.domain.services.sorting import SortingStrategy  # type: ignore
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortDirection,
    SortField,
)


class SortingContext:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_data(
        self, data: List[StarwarsEntity], sort_by: SortField, direction: SortDirection
    ) -> List[StarwarsEntity]:
        return self._strategy.sort(data, sort_by, direction)
