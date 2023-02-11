"""
Paviary: Desktop

This currently only has desktop detection module for Linux currently, will add
more implementations later.
"""

from enum import Enum, auto

import dbus


# Recognizable Desktops
class Desktop(Enum):
    GNOME = auto
    KDE = auto
    UNKNOWN = auto


# Desktop Dictionary to find the correct desktop
DESKTOPS = {
    ("org.gnome.SessionManager", "/org/gnome/SessionManager"): Desktop.GNOME,
    ("org.kde.kded", "/kded"): Desktop.KDE,
}


def find_desktop() -> Desktop:
    """
    This method will tell us what system we're using
    """
    ses_bus = dbus.SessionBus()
    detected_desktop = Desktop.UNKNOWN
    for desktop in DESKTOPS:
        try:
            ses_bus.get_object(*desktop)
            detected_desktop = DESKTOPS[desktop]
        except dbus.exceptions.DBusException:
            pass
    return detected_desktop
