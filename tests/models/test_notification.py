from paviary.models.notification import Notification
from .base import encode_and_decode


def test_notification_obj():
    # Create a notification object
    notif = Notification(
        "WhatsApp", "Class Group: Niharika: Guys shall we go for a trip?"
    )
    # Encode and decode the notification using the default serializer
    decoded_dict = encode_and_decode(notif)
    # Parse the decoded value to the notification object
    decoded_notif = Notification(**decoded_dict)
    assert isinstance(decoded_notif, Notification)
    # Assert parsed-reparsed notification is the same
    assert notif == decoded_notif
