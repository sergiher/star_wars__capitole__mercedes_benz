import datetime

from app.domain.types.sort_options import (  # type: ignore
    SortAlgorithm,
    SortDirection,
    SortField,
)
from pydantic import BaseModel


class SortOptions(BaseModel):
    field: SortField
    direction: SortDirection
    algorithm: SortAlgorithm


class StarWarsElement(BaseModel):
    name: str
    created: datetime.datetime
