from datetime import UTC, datetime, timedelta
from typing import List

import pytest
from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore
from app.domain.services.starwars_entity_service import (  # type: ignore
    StarwarsEntityService,
)
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortAlgorithm,
    SortDirection,
    SortOptions,
)


class DummyStarWarsEntityRepo:
    def get_all_elements(self, entity_type: str) -> List[StarwarsEntity]:
        current_time = datetime.now(UTC)
        if entity_type == "people":
            return [
                StarwarsEntity(name="Luke", created=current_time),
                StarwarsEntity(
                    name="Person 2",
                    created=current_time + timedelta(minutes=2),  # noqa: E501
                ),
                StarwarsEntity(
                    name="Person 3",
                    created=current_time + timedelta(minutes=3),  # noqa: E501
                ),
            ]
        elif entity_type == "planets":
            return [
                StarwarsEntity(name="Tatooine", created=current_time),
                StarwarsEntity(
                    name="Planet 2",
                    created=current_time + timedelta(minutes=2),  # noqa: E501
                ),
                StarwarsEntity(
                    name="Planet 3",
                    created=current_time + timedelta(minutes=3),  # noqa: E501
                ),
            ]
        else:
            return []


@pytest.fixture
def starwars_entity_service() -> StarwarsEntityService:
    repo = DummyStarWarsEntityRepo()
    return StarwarsEntityService(repo)


def test_starwars_entity_service_get_all_elements(starwars_entity_service):
    sw_people = starwars_entity_service.get_all_elements(entity_type="people")
    assert sw_people[0].name == "Luke"
    assert sw_people[1].name == "Person 2"
    assert sw_people[2].name == "Person 3"
    assert type(sw_people[0].created) is datetime

    sw_planets = starwars_entity_service.get_all_elements(
        entity_type="planets"
    )  # noqa: E501
    assert sw_planets[0].name == "Tatooine"
    assert sw_planets[1].name == "Planet 2"
    assert sw_planets[2].name == "Planet 3"
    assert type(sw_planets[0].created) is datetime


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
    assert sw_people_sorted[0].name == "Person 3"
    assert sw_people_sorted[1].name == "Person 2"
    assert sw_people_sorted[2].name == "Luke"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.POWER_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Person 3"
    assert sw_people_sorted[1].name == "Person 2"
    assert sw_people_sorted[2].name == "Luke"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.ASC,
            algorithm=SortAlgorithm.POWER_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Luke"
    assert sw_people_sorted[1].name == "Person 2"
    assert sw_people_sorted[2].name == "Person 3"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.BUBBLE_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Person 3"
    assert sw_people_sorted[1].name == "Person 2"
    assert sw_people_sorted[2].name == "Luke"

    sw_people_sorted = starwars_entity_service.sort_elements(
        starwars_elements=sw_people,
        sort_options=SortOptions(
            field="name",
            direction=SortDirection.DESC,
            algorithm=SortAlgorithm.SELECTION_SORT,
        ),
    )
    assert sw_people_sorted[0].name == "Person 3"
    assert sw_people_sorted[1].name == "Person 2"
    assert sw_people_sorted[2].name == "Luke"
