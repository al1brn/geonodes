"""Handwritten shadernodes specialization of Shader."""
from ...root.shader import Shader as RootShader

from ...root.node import Node

class Shader:
    ...

class Float:
    ...

class Shader(RootShader):
    __slots__ = ()

    def out(self, name=None, panel=""):
        """Send to a group output or the material surface."""
        if self._tree._is_group:
            return super().out(name, panel=panel)
        self._tree.output_node.set_input_socket('Surface', self, create=False)

    def mix(self, shader: Shader = None, factor: Float = None):
        """ Mix with another shader

        @node Mix Shader
        """
        node = Node('Mix Shader', named_sockets={'Shader': self, 'Shader_1': shader, 'Factor': factor})
        return self._jump(node._out)
