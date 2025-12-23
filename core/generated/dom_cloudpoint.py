# Generated 2025-12-23 17:03:08

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class CloudPoint:
    """"
    $DOC SET hidden
    """
    @property
    def radius(self):
        """ Property get node <Node Set Point Radius>
        """
        return Node('Radius', {})._out

    @radius.setter
    def radius(self, radius: Float = None):
        """ > Node <&Node Set Point Radius>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Set Point Radius', {'Points': self, 'Selection': self.get_selection(), 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

