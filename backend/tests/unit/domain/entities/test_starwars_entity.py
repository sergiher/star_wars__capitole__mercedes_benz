from datetime import UTC, datetime

from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore


def test_create_starwars_entity_unit():
    starwars_entity = StarwarsEntity(name="Luke", created=datetime.now(UTC))
    assert starwars_entity.name == "Luke"
    assert type(starwars_entity.created) is datetime
