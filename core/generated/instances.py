# Generated 2026-01-03 16:39:50

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


class Instances(Socket):
    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'INSTANCES'

        Returns
        -------
        - Integer
        """
        node = self._cache('Domain Size', {'Geometry': self}, component='INSTANCES')
        return node._out

    @classmethod
    def FromGeometry(cls, *geometry: Geometry):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Instances
        """
        node = Node('Geometry to Instance', {'Geometry': list(geometry)})
        return cls(node._out)

    @classmethod
    def ImportOBJ(cls, path: String = None):
        """ > Node <&Node Import OBJ>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Instances
        """
        node = Node('Import OBJ', {'Path': path})
        return cls(node._out)

    @classmethod
    @property
    def rotation(cls):
        """ > Node <&Node Instance Rotation>

        Returns
        -------
        - Rotation
        """
        node = Node('Instance Rotation', )
        return node._out

    @classmethod
    @property
    def instance_scale(cls):
        """ > Node <&Node Instance Scale>

        Returns
        -------
        - Vector
        """
        node = Node('Instance Scale', )
        return node._out

    def to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Instances to Points>

        Information
        -----------
        - Socket 'Instances' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Instances to Points', {'Instances': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius})
        return node._out

    def rotate(self,
                    rotation: Rotation = None,
                    pivot_point: Vector = None,
                    local_space: Boolean = None):
        """ > Node <&Node Rotate Instances>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Instances' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - pivot_point (Vector) : socket 'Pivot Point' (id: Pivot Point)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Rotate Instances', {'Instances': self, 'Selection': self.get_selection(), 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})
        self._jump(node._out)
        return self._domain_to_geometry

    def scale(self, scale: Vector = None, center: Vector = None, local_space: Boolean = None):
        """ > Node <&Node Scale Instances>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Instances' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - scale (Vector) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Scale Instances', {'Instances': self, 'Selection': self.get_selection(), 'Scale': scale, 'Center': center, 'Local Space': local_space})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Instance Transform>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Instances' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Instances
        """
        node = Node('Set Instance Transform', {'Instances': self, 'Selection': self.get_selection(), 'Transform': transform})
        self._jump(node._out)
        return self._domain_to_geometry

    def translate(self, translation: Vector = None, local_space: Boolean = None):
        """ > Node <&Node Translate Instances>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Instances' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - local_space (Boolean) : socket 'Local Space' (id: Local Space)

        Returns
        -------
        - Instances
        """
        node = Node('Translate Instances', {'Instances': self, 'Selection': self.get_selection(), 'Translation': translation, 'Local Space': local_space})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def transform(self):
        """ Property get node <Node Set Instance Transform>
        """
        return Node('Instance Transform', {})._out

    @transform.setter
    def transform(self, transform: Matrix = None):
        """ > Node <&Node Set Instance Transform>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Instances' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Instances
        """
        node = Node('Set Instance Transform', {'Instances': self, 'Selection': self.get_selection(), 'Transform': transform})
        self._jump(node._out)
        return self._domain_to_geometry

