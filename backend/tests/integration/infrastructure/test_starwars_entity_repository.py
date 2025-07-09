from app.infrastructure.api_repositories.starwars_entity_api_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityApiRepository,
)


def test_starwars_entity_repository_get_all_elements():
    repository = StarwarsEntityApiRepository()
    people_list = repository.get_all_elements(entity_type="people")

    assert len(people_list) == 82
    assert people_list[0].name == "Luke Skywalker"
    assert people_list[0].created == "2014-12-09T13:50:51.644000Z"
