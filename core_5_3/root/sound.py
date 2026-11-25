"""Shared sound socket root."""
from .socket import Socket


class Sound(Socket):
    __slots__ = ()
    SOCKET_TYPE = 'SOUND'
