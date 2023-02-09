from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Protocol
from uuid import UUID, uuid4


@dataclass
class Serializable(Protocol):
    id: UUID = field(default_factory=uuid4, kw_only=True)
    timestamp: datetime = field(default_factory=datetime.now, kw_only=True)

    def __post_init__(self):
        if isinstance(self.id, str):
            self.id = UUID(self.id)
        if isinstance(self.timestamp, str):
            self.timestamp = datetime.fromisoformat(self.timestamp)

    def encode(self) -> dict[str, Any]:
        """
        Encodes all serializable object to dict[str, Any].
        """
        val = asdict(self)
        val["id"] = str(self.id)
        val["timestamp"] = self.timestamp.isoformat()
        return val

    @staticmethod
    def decode(data: dict[str, Any]) -> "Serializable":
        ...
