from dataclasses import dataclass
from datetime import datetime


@dataclass
class StarwarsEntity:
    name: str
    created: datetime
