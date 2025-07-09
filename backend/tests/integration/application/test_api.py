from datetime import UTC, datetime

from app.application.dependencies.services.starwars_entity import (  # type: ignore  # noqa: E501
    get_starwars_entity_service,
)
from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore
from app.domain.types.sort_options import (  # type: ignore  # noqa: E501
    SortDirection,
    SortOptions,
)


class DummyStarwarsEntityService:
    def get_all_elements(self, entity_type):
        return [
            StarwarsEntity(name="A", created=datetime.now(UTC)),
            StarwarsEntity(name="B", created=datetime.now(UTC)),
            StarwarsEntity(name="C", created=datetime.now(UTC)),
        ]

    def sort_elements(self, starwars_elements, sort_options: SortOptions):
        return sorted(
            starwars_elements,
            key=lambda e: e.name,
            reverse=sort_options.direction == SortDirection.DESC,
        )


def test_get_elements(client):
    client.app.dependency_overrides[get_starwars_entity_service] = (
        DummyStarwarsEntityService
    )

    response = client.get("/people")
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 3
    assert data[0]["name"] == "A"
    assert data[1]["name"] == "B"
    assert data[2]["name"] == "C"


def test_sort_starwars_entities(client):
    client.app.dependency_overrides[get_starwars_entity_service] = (
        DummyStarwarsEntityService
    )

    response = client.post(
        "/sort/people",
        json={
            "field": "name",
            "direction": "desc",
            "algorithm": "power_sort",
        },
    )
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 3
    assert data[0]["name"] == "C"
    assert data[1]["name"] == "B"
    assert data[2]["name"] == "A"
