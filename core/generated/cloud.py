# Generated 2025-12-15 16:57:50

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


class Cloud(Socket):
    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'POINTCLOUD'

        Returns
        -------
        - Integer
        """
        node = self._cache('Domain Size', {'Geometry': self}, component='POINTCLOUD')
        return node._out

    @classmethod
    def ImportCSV(cls, path: String = None, delimiter: String = None):
        """ > Node <&Node Import CSV>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)
        - delimiter (String) : socket 'Delimiter' (id: Delimiter)

        Returns
        -------
        - Cloud
        """
        node = Node('Import CSV', {'Path': path, 'Delimiter': delimiter})
        return cls(node._out)

    def instance_on(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Instance on Points>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instance (Instances) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', {'Points': self, 'Selection': self.get_selection(), 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def interpolate_curves(self,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None):
        """ > Node <&Node Interpolate Curves>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - guide_curves (Curve) : socket 'Guide Curves' (id: Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve [closest_index_ (Integer), closest_weight_ (Float)]
        """
        node = Node('Interpolate Curves', {'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': self, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node._out

    @classmethod
    def Points(cls, count: Integer = None, position: Vector = None, radius: Float = None):
        """ > Node <&Node Points>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Points', {'Count': count, 'Position': position, 'Radius': radius})
        return cls(node._out)

    def to_curves(self, curve_group_id: Integer = None, weight: Float = None):
        """ > Node <&Node Points to Curves>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - curve_group_id (Integer) : socket 'Curve Group ID' (id: Curve Group ID)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Curve
        """
        node = Node('Points to Curves', {'Points': self, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out

    def to_vertices(self):
        """ > Node <&Node Points to Vertices>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Mesh
        """
        node = Node('Points to Vertices', {'Points': self, 'Selection': self.get_selection()})
        return node._out

    def to_volume(self,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    radius: Float = None):
        """ > Node <&Node Points to Volume>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - resolution_mode (menu='Amount') : ('Amount', 'Size')
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Volume
        """
        node = Node('Points to Volume', {'Points': self, 'Density': density, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Radius': radius})
        return node._out

    def to_sdf_grid(self, radius: Float = None, voxel_size: Float = None):
        """ > Node <&Node Points to SDF Grid>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)

        Returns
        -------
        - Float
        """
        node = Node('Points to SDF Grid', {'Points': self, 'Radius': radius, 'Voxel Size': voxel_size})
        return node._out

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

