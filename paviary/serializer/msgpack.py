"""
MessagePack Serializer

This serializes and deserializes a messagepack object.
"""

from typing import Any
from msgpack import packb
from msgpack import unpackb

from paviary.models.serializable import Serializable
from paviary.serializer.base import BaseSerializer


class MessagePackSerializer(BaseSerializer):
    def encode(self, obj_to_encode: Serializable):
        return packb(obj_to_encode.encode())

    def decode(self, data_to_decode: bytes) -> dict[str, Any]:
        return unpackb(data_to_decode, raw=False)
