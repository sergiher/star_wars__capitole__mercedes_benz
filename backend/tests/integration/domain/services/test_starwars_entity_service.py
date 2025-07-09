import pytest
from app.domain.services.starwars_entity_service import (  # type: ignore
    StarwarsEntityService,
)
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortAlgorithm,
    SortDirection,
    SortOptions,
)
from app.infrastructure.api_repositories.starwars_entity_api_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityApiRepository,
)


@pytest.fixture
def starwars_entity_service() -> StarwarsEntityService:
    repo = StarwarsEntityApiRepository()
    return StarwarsEntityService(repo)


def test_starwars_entity_service_get_all_elements(starwars_entity_service):
    sw_people = starwars_entity_service.get_all_elements(entity_type="people")
    assert sw_people[0].name == "Luke Skywalker"
    assert sw_people[1].name == "C-3PO"
    assert sw_people[2].name == "R2-D2"
    assert type(sw_people[0].created) is str
    assert sw_people[0].created == "2014-12-09T13:50:51.644000Z"

    sw_planets = starwars_entity_service.get_all_elements(entity_type="planets")
    assert sw_planets[0].name == "Tatooine"
    assert sw_planets[1].name == "Alderaan"
    assert sw_planets[2].name == "Yavin IV"
    assert type(sw_planets[0].created) is str
    assert sw_planets[0].created == "2014-12-09T13:50:49.641000Z"


def test_starwars_entity_service_sort_elements(starwars_entity_service):
    sw_people = starwars_entity_service.get_all_elements(entity_type="people")
    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="created",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.POWER_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Tion Medon"
    assert sw_people_sorted[1].name == "Sly Moore"
    assert sw_people_sorted[2].name == "Raymus Antilles"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.POWER_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Zam Wesell"
    assert sw_people_sorted[1].name == "Yoda"
    assert sw_people_sorted[2].name == "Yarael Poof"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.ASC,
            algorithm=SortAlgorithm.POWER_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Ackbar"
    assert sw_people_sorted[1].name == "Adi Gallia"
    assert sw_people_sorted[2].name == "Anakin Skywalker"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.BUBBLE_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Zam Wesell"
    assert sw_people_sorted[1].name == "Yoda"
    assert sw_people_sorted[2].name == "Yarael Poof"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.SELECTION_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Zam Wesell"
    assert sw_people_sorted[1].name == "Yoda"
    assert sw_people_sorted[2].name == "Yarael Poof"
