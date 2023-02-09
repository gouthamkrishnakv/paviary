__all__ = ["BaseSerializer", "MessagePackSerializer", "get_serializer"]

from .msgpack import MessagePackSerializer
from .base import BaseSerializer


def get_serializer():
    return MessagePackSerializer()
