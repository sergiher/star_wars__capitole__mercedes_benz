from app.domain.services.sorting import (  # type: ignore
    BubbleSort,
    PowerSort,
    SelectionSort,
    SortingStrategy,
)
from app.domain.types.sort_options import SortAlgorithm  # type: ignore


def get_sorting_strategy(algorithm: SortAlgorithm) -> SortingStrategy:
    if algorithm == SortAlgorithm.POWER_SORT:
        return PowerSort()
    elif algorithm == SortAlgorithm.BUBBLE_SORT:
        return BubbleSort()
    elif algorithm == SortAlgorithm.SELECTION_SORT:
        return SelectionSort()
    else:
        raise ValueError(f"Unsupported sort algorithm: {algorithm}")
