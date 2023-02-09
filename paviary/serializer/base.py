"""
Serializer Base Class
"""

from typing import Protocol

from paviary.models.serializable import Serializable


class BaseSerializer(Protocol):
    def encode(self, obj_to_encode: Serializable) -> bytes:
        ...

    def decode(self, encoded_data: bytes | str):
        ...
