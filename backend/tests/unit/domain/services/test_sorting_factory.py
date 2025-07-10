import pytest
from app.domain.services.sorting import (  # type: ignore
    BubbleSort,
    PowerSort,
    SelectionSort,
)
from app.domain.services.sorting_factory import (  # type: ignore  # noqa: E501
    get_sorting_strategy,
)
from app.domain.types.sort_options import SortAlgorithm  # type: ignore


def test_sorting_factory():
    assert isinstance(
        get_sorting_strategy(algorithm=SortAlgorithm.POWER_SORT), PowerSort
    )

    assert isinstance(
        get_sorting_strategy(algorithm=SortAlgorithm.BUBBLE_SORT), BubbleSort
    )

    assert isinstance(
        get_sorting_strategy(algorithm=SortAlgorithm.SELECTION_SORT),
        SelectionSort,  # noqa: E501
    )

    with pytest.raises(ValueError):
        get_sorting_strategy(algorithm="algorith_that_dont_use")
