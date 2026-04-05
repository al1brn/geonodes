# Generated 2026-04-04 17:31:31

from __future__ import annotations
from .. sockettype import SocketType
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
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Cloud(Socket):

    __slots__ = ()

    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | Geometry    | `self`         |
        | Parameter | `component` | `'POINTCLOUD'` |

        Returns
        -------
        Integer
        """
        node = self._cache('Domain Size', {'Geometry': self}, component='POINTCLOUD')
        return node._out

    @classmethod
    def ImportCSV(cls, path: String = None, delimiter: String = None):
        """ > Node <&Node Import CSV>

        Parameters
        ----------
        path : String, optional
            socket 'Path' (id: Path)
        
        delimiter : String, optional
            socket 'Delimiter' (id: Delimiter)
        

        Returns
        -------
        Cloud
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

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Points    | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        instance : Instances, optional
            socket 'Instance' (id: Instance)
        
        pick_instance : Boolean, optional
            socket 'Pick Instance' (id: Pick Instance)
        
        instance_index : Integer, optional
            socket 'Instance Index' (id: Instance Index)
        
        rotation : Rotation, optional
            socket 'Rotation' (id: Rotation)
        
        scale : Vector, optional
            socket 'Scale' (id: Scale)
        

        Returns
        -------
        Instances
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

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Points | `self` |

        Parameters
        ----------
        guide_curves : Curve, optional
            socket 'Guide Curves' (id: Guide Curves)
        
        guide_up : Vector, optional
            socket 'Guide Up' (id: Guide Up)
        
        guide_group_id : Integer, optional
            socket 'Guide Group ID' (id: Guide Group ID)
        
        point_up : Vector, optional
            socket 'Point Up' (id: Point Up)
        
        point_group_id : Integer, optional
            socket 'Point Group ID' (id: Point Group ID)
        
        max_neighbors : Integer, optional
            socket 'Max Neighbors' (id: Max Neighbors)
        

        Returns
        -------
        Curve
            peer sockets: closest_index_ (Integer), closest_weight_ (Float)

        """
        node = Node('Interpolate Curves', {'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': self, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node._out

    @classmethod
    def Points(cls, count: Integer = None, position: Vector = None, radius: Float = None):
        """ > Node <&Node Points>

        Parameters
        ----------
        count : Integer, optional
            socket 'Count' (id: Count)
        
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Points', {'Count': count, 'Position': position, 'Radius': radius})
        return cls(node._out)

    def to_curves(self, curve_group_id: Integer = None, weight: Float = None):
        """ > Node <&Node Points to Curves>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Points | `self` |

        Parameters
        ----------
        curve_group_id : Integer, optional
            socket 'Curve Group ID' (id: Curve Group ID)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Curve
        """
        node = Node('Points to Curves', {'Points': self, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out

    def to_vertices(self):
        """ > Node <&Node Points to Vertices>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Points    | `self`            |
        | Socket | Selection | `self[selection]` |

        Returns
        -------
        Mesh
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

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Points | `self` |

        Parameters
        ----------
        density : Float, optional
            socket 'Density' (id: Density)
        
        resolution_mode : menu='Amount', optional
            ('Amount', 'Size')
        
        voxel_size : Float, optional
            socket 'Voxel Size' (id: Voxel Size)
        
        voxel_amount : Float, optional
            socket 'Voxel Amount' (id: Voxel Amount)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Volume
        """
        node = Node('Points to Volume', {'Points': self, 'Density': density, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Radius': radius})
        return node._out

    def to_sdf_grid(self, radius: Float = None, voxel_size: Float = None):
        """ > Node <&Node Points to SDF Grid>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Points | `self` |

        Parameters
        ----------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        voxel_size : Float, optional
            socket 'Voxel Size' (id: Voxel Size)
        

        Returns
        -------
        Float
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

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Points    | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Set Point Radius', {'Points': self, 'Selection': self.get_selection(), 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

