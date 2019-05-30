from dataclasses import dataclass
from typing import Union


@dataclass()
class Nap:
    id: str
    asleep: int
    awake: Union[int, None] = None
