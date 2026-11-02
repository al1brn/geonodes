"""Handwritten shadernodes specialization of Vector."""
from ...root.vector import Vector as RootVector


class Vector(RootVector):
    __slots__ = ()

    def out(self, name=None, **props):
        """Send to a group output, material displacement, or a named color AOV."""
        if self._tree._is_group:
            return super().out(name=name, **props)
        if name is None:
            self._tree.set_displacement(self)
        else:
            self._tree.aov_output(name=name, color=self)
