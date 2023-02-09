from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from paviary.models.serializable import Serializable

@dataclass
class Notification(Serializable):
    # Title of the notification
    title: str
    description: str

    @staticmethod
    def decode(data: dict[str, Any]) -> "Notification":
        """
        Decodes Notification
        """
        return Notification(**data)

    # def show(self):  # OR DISPLAY
    #     """
    #     Show the notification
    #     """
    #     ...

    # def close(self):  # OR DISMISS
    #     """
    #     Close the notification
    #     """
    #     ...

    # def update(self):
    #     """
    #     Update the notification
    #     """
    #     ...
