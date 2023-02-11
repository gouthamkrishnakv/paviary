from dataclasses import dataclass

from paviary.models.serializable import Serializable


@dataclass
class Notification(Serializable):
    # Title of the notification
    title: str
    description: str

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
