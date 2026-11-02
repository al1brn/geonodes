"""Shared geometry socket root; geometry-specific behavior lives in its environment."""
from .socket import Socket
from .node import Node


class Geometry(Socket):
    __slots__ = ()
    SOCKET_TYPE = 'GEOMETRY'

    @classmethod
    def Join(cls, *geometry):
        """Join geometries and wrap the result in the called geometry class."""
        node = Node('Join Geometry', named_sockets={'Geometry': list(geometry)})
        return cls(node._out)

    def __add__(self, other):
        if isinstance(other, tuple):
            return type(self).Join(self, *other)
        if isinstance(other, type(self)):
            return type(self).Join(self, other)
        return Geometry.Join(self, other)

    def __radd__(self, other):
        if isinstance(other, tuple):
            return type(self).Join(*other, self)
        if isinstance(other, type(self)):
            return type(self).Join(other, self)
        return Geometry.Join(other, self)

    def __iadd__(self, other):
        return self._jump(self + other)
