from dataclasses import dataclass

from curio.events.event import Event


@dataclass
class Observation(Event):
    content: str
