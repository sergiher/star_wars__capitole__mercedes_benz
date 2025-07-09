from datetime import UTC, datetime

from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore
from app.domain.services.sorting_context import (  # type: ignore  # noqa: E501
    SortingContext,
)
from app.domain.services.sorting_factory import (  # type: ignore  # noqa: E501
    get_sorting_strategy,
)
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortAlgorithm,
    SortDirection,
)


def test_sort_data():
    sorted_list = SortingContext(
        strategy=get_sorting_strategy(SortAlgorithm.POWER_SORT)
    ).sort_data(
        data=[
            StarwarsEntity(name="A", created=datetime.now(UTC)),
            StarwarsEntity(name="B", created=datetime.now(UTC)),
            StarwarsEntity(name="C", created=datetime.now(UTC)),
        ],
        sort_by="name",
        direction=SortDirection.DESC,
    )
    assert sorted_list[0].name == "C"
    assert sorted_list[1].name == "B"
    assert sorted_list[2].name == "A"
