"""Handwritten shadernodes specialization of Float."""
from ...root.float import Float as RootFloat


class Float(RootFloat):
    __slots__ = ()

    def out(self, name=None, **props):
        """Send to a group output, material thickness, or a named value AOV."""
        if self._tree._is_group:
            return super().out(name=name, **props)
        if name is None:
            self._tree.set_thickness(self)
        else:
            self._tree.aov_output(name=name, value=self)
