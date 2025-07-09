from dataclasses import dataclass
from enum import Enum
from typing import Literal

SortField = Literal["name", "created"]


class SortDirection(Enum):
    ASC = "asc"
    DESC = "desc"


class SortAlgorithm(Enum):
    POWER_SORT = "power_sort"  # The default sorting method in python ^3.11
    BUBBLE_SORT = "bubble_sort"
    SELECTION_SORT = "selection_sort"


@dataclass
class SortOptions:
    field: str
    direction: SortDirection
    algorithm: SortAlgorithm
