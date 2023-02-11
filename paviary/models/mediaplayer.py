from dataclasses import dataclass
from typing import Any
from .serializable import Serializable


@dataclass
class MediaPlayer(Serializable):
    track_name: str
