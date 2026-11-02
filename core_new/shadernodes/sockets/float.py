"""Handwritten shadernodes specialization of Float."""
from ...root.float import Float as RootFloat
from ...root.node import Node


class Float(RootFloat):
    __slots__ = ()

    def compare(self, value=None, epsilon=None, use_clamp=False):
        """Compare for equality within epsilon using shader Math."""
        node = Node('Math', named_sockets={
            'Value': self, 'Value_1': value, 'Epsilon': epsilon,
        }, operation='COMPARE', use_clamp=use_clamp)
        return node._out

    def out(self, name=None, **props):
        """Send to a group output, material thickness, or a named value AOV."""
        if self._tree._is_group:
            return super().out(name=name, **props)
        if name is None:
            self._tree.set_thickness(self)
        else:
            self._tree.aov_output(name=name, value=self)
