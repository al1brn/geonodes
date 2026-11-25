"""Handwritten shadernodes specialization of VolumeShader."""
from ...root.shader import VolumeShader as RootVolumeShader


class VolumeShader(RootVolumeShader):
    __slots__ = ()

    def out(self, name=None, panel=""):
        """Send to a group output or the material volume."""
        if self._tree._is_group:
            return super().out(name, panel=panel)
        self._tree.output_node.set_input_socket('Volume', self, create=False)
