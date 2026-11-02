"""Handwritten shadernodes specialization of Shader."""
from ...root.shader import Shader as RootShader


class Shader(RootShader):
    __slots__ = ()

    def out(self, name=None, panel=""):
        """Send to a group output or the material surface."""
        if self._tree._is_group:
            return super().out(name, panel=panel)
        self._tree.output_node.set_input_socket('Surface', self, create=False)
