import datetime
from typing import Optional

from app.domain.types.sort_options import (  # type: ignore
    SortAlgorithm,
    SortDirection,
    SortField,
)
from pydantic import BaseModel


class SortOptions(BaseModel):
    field: SortField
    direction: SortDirection
    algorithm: Optional[SortAlgorithm] = None


class StarWarsElement(BaseModel):
    name: str
    created: datetime.datetime
