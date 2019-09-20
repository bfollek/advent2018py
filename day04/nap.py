from dataclasses import dataclass
from typing import Optional


@dataclass()
class Nap:
    id: str
    asleep: int
    awake: int = -1
