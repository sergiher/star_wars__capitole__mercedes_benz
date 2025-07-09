from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore


class StarwarsEntityRepository(ABC):
    @abstractmethod
    def get_all_elements(self, entity_type: str) -> List[StarwarsEntity]:
        pass
