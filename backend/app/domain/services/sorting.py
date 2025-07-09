from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortDirection,
    SortField,
)


class SortingStrategy(ABC):
    @abstractmethod
    def sort(
        self, data: List[StarwarsEntity], sort_by: SortField, direction: SortDirection
    ) -> List[StarwarsEntity]:
        pass


class PowerSort(SortingStrategy):
    def sort(
        self, data: List[StarwarsEntity], sort_by: SortField, direction: SortDirection
    ) -> List[StarwarsEntity]:
        return sorted(
            data,
            key=lambda p: getattr(p, sort_by),
            reverse=(True if direction is SortDirection.DESC else False),  # noqa: E501
        )


class BubbleSort(SortingStrategy):
    def sort(
        self, data: List[StarwarsEntity], sort_by: SortField, direction: SortDirection
    ) -> List[StarwarsEntity]:
        items = data.copy()
        n = len(items)
        reverse = direction == SortDirection.DESC

        for i in range(n):
            for j in range(0, n - i - 1):
                left = getattr(items[j], sort_by)
                right = getattr(items[j + 1], sort_by)
                if (left > right and not reverse) or (left < right and reverse):
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items


class SelectionSort(SortingStrategy):
    def sort(
        self, data: List[StarwarsEntity], sort_by: SortField, direction: SortDirection
    ) -> List[StarwarsEntity]:
        items = data.copy()
        n = len(items)
        reverse = direction == SortDirection.DESC

        for i in range(n):
            selected_index = i
            for j in range(i + 1, n):
                a = getattr(items[j], sort_by)
                b = getattr(items[selected_index], sort_by)
                if (a > b and reverse) or (a < b and not reverse):
                    selected_index = j
            items[i], items[selected_index] = items[selected_index], items[i]
        return items
