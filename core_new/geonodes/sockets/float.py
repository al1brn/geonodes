"""Handwritten geonodes specialization of Float."""
from ...root.float import Float as RootFloat
from ...root.node import Node


class Float(RootFloat):
    __slots__ = ()

    def compare(self, value=None, epsilon=None, use_clamp=False):
        """Compare for equality within epsilon. use_clamp is ignored in geometry."""
        node = Node('Compare', named_sockets={
            'A': self, 'B': value, 'Epsilon': epsilon,
        }, data_type='FLOAT', mode='ELEMENT', operation='EQUAL')
        return node._out
