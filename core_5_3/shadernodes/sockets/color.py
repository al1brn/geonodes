"""Handwritten shadernodes specialization of Color."""
from ...root.color import Color as RootColor


class Color(RootColor):
    __slots__ = ()

    def out(self, name=None, panel: str = ""):
        """Send to a group output or a color AOV."""
        if self._tree._is_group:
            return super().out(name=name, panel=panel)
        self._tree.aov_output(name='Color' if name is None else name, color=self)
