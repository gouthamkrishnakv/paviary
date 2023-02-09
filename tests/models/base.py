from paviary.models.serializable import Serializable
from paviary.serializer import BaseSerializer, get_serializer


def encode_and_decode(obj: Serializable, serializer: BaseSerializer | None = None):
    if serializer is None:
        serializer = get_serializer()
    # Encode into bytes
    encoded_bytes = serializer.encode(obj)
    # Make sure encoded_bytes are actually a byte-array
    assert isinstance(encoded_bytes, bytes)
    decoded_dict = serializer.decode(encoded_bytes)
    # Check wheher the decoded dict is proper
    assert isinstance(decoded_dict, dict)
    return decoded_dict
