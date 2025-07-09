import logging
from typing import Any, Dict, List

import requests
from app.domain.entities.starwars_entity import StarwarsEntity  # type: ignore
from app.domain.repositories.starwars_entity_repository import (  # type: ignore  # noqa: E501
    StarwarsEntityRepository,
)


class StarwarsEntityApiRepository(StarwarsEntityRepository):
    def __init__(
        self, base_url: str = "https://swapi.info/api", timeout: int = 30
    ):  # noqa: E501
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

        # Mapping entity types to API endpoints
        self.entity_endpoints = {"people": "people", "planets": "planets"}

    def get_all_elements(self, entity_type: str) -> List[StarwarsEntity]:
        """
        Fetch all elements for the specified entity type from SWAPI.

        Args:
            entity_type: Either "people" or "planets"

        Returns:
            List of StarwarsEntity objects

        Raises:
            ValueError: If entity_type is not supported
            requests.RequestException: If API request fails
        """
        if entity_type not in self.entity_endpoints:
            raise ValueError(
                f"Unsupported entity type: {entity_type}. Supported types: {list(self.entity_endpoints.keys())}"  # noqa: E501
            )

        endpoint = self.entity_endpoints[entity_type]
        all_entities = []

        try:
            url = f"{self.base_url}/{endpoint}"

            self.logger.info(f"Fetching data from: {url}")
            response = self._make_request(url)

            if response.status_code != 200:
                raise requests.RequestException(
                    f"API request failed with status {response.status_code}: {response.text}"  # noqa: E501
                )

            data = response.json()

            # Convert API response to StarwarsEntity objects
            entities = self._convert_to_entities(data, entity_type)  # noqa: E501
            all_entities.extend(entities)

            self.logger.info(
                f"Successfully fetched {len(all_entities)} {entity_type} in total"  # noqa: E501
            )
            return all_entities

        except requests.exceptions.RequestException as e:
            self.logger.error(
                f"Error fetching {entity_type} from SWAPI: {str(e)}"
            )  # noqa: E501
            raise
        except Exception as e:
            self.logger.error(
                f"Unexpected error while fetching {entity_type}: {str(e)}"
            )
            raise

    def _make_request(self, url: str) -> requests.Response:
        """Make HTTP request with proper error handling and timeout."""
        try:
            response = requests.get(url, timeout=self.timeout)
            return response
        except requests.exceptions.Timeout:
            raise requests.RequestException(
                f"Request timed out after {self.timeout} seconds"
            )
        except requests.exceptions.ConnectionError:
            raise requests.RequestException("Failed to connect to SWAPI")
        except requests.exceptions.RequestException as e:
            raise requests.RequestException(f"HTTP request failed: {str(e)}")

    def _convert_to_entities(
        self, api_data: List[Dict[str, Any]], entity_type: str
    ) -> List[StarwarsEntity]:
        """
        Convert API response data to StarwarsEntity objects.

        Args:
            api_data: List of dictionaries from API response
            entity_type: Type of entity ("people" or "planets")

        Returns:
            List of StarwarsEntity objects
        """
        entities = []

        for item in api_data:
            try:
                entity = StarwarsEntity(
                    name=item["name"], created=item["created"]
                )  # noqa: E501
                entities.append(entity)
            except Exception as e:
                self.logger.warning(
                    f"Failed to convert item to StarwarsEntity: {item}. Error: {str(e)}"  # noqa: E501
                )
                continue

        return entities
