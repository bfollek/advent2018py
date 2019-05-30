from dataclasses import dataclass


@dataclass()
class Nap:
    id: str
    asleep: int
    awake: int
