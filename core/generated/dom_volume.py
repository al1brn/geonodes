# Generated 2025-12-06 09:59:03

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves, MenuNode, IndexSwitchNode
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


class Volume(Socket):
    """"
    $DOC SET hidden
    """
    def distribute_points(self,
                    mode: Literal['Random', 'Grid'] = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None):
        """ > Node <&Node Distribute Points in Volume>

        Information
        -----------
        - Socket 'Volume' : self

        Arguments
        ---------
        - mode (menu='Random') : ('Random', 'Grid')
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Volume', {'Volume': self, 'Mode': mode, 'Density': density, 'Seed': seed, 'Spacing': spacing, 'Threshold': threshold})
        return node._out

    @classmethod
    def ImportVDB(cls, path: String = None):
        """ > Node <&Node Import VDB>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Volume
        """
        node = Node('Import VDB', {'Path': path})
        return cls(node._out)

    @classmethod
    def Cube(cls,
                    density: Float = None,
                    background: Float = None,
                    min: Vector = None,
                    max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None):
        """ > Node <&Node Volume Cube>

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - background (Float) : socket 'Background' (id: Background)
        - min (Vector) : socket 'Min' (id: Min)
        - max (Vector) : socket 'Max' (id: Max)
        - resolution_x (Integer) : socket 'Resolution X' (id: Resolution X)
        - resolution_y (Integer) : socket 'Resolution Y' (id: Resolution Y)
        - resolution_z (Integer) : socket 'Resolution Z' (id: Resolution Z)

        Returns
        -------
        - Volume
        """
        node = Node('Volume Cube', {'Density': density, 'Background': background, 'Min': min, 'Max': max, 'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})
        return cls(node._out)

    def to_mesh(self,
                    resolution_mode: Literal['Grid', 'Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    threshold: Float = None,
                    adaptivity: Float = None):
        """ > Node <&Node Volume to Mesh>

        Information
        -----------
        - Socket 'Volume' : self

        Arguments
        ---------
        - resolution_mode (menu='Grid') : ('Grid', 'Amount', 'Size')
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Volume to Mesh', {'Volume': self, 'Resolution Mode': resolution_mode, 'Voxel Size': voxel_size, 'Voxel Amount': voxel_amount, 'Threshold': threshold, 'Adaptivity': adaptivity})
        return node._out

    def store_named_grid(self, name: String = None, grid: Boolean | Float | Integer | Vector = None):
        """ > Node <&Node Store Named Grid>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'data_type' : depending on 'grid' type

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - grid (Boolean | Float | Integer | Vector) : socket 'Grid' (id: Grid)

        Returns
        -------
        - Volume
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedGrid', grid)
        node = Node('Store Named Grid', {'Volume': self, 'Name': name, 'Grid': grid}, data_type=data_type)
        self._jump(node._out)
        return self._domain_to_geometry

    def get_named_grid(self,
                    name: String = None,
                    remove: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT'):
        """ > Node <&Node Get Named Grid>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Volume' : self

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - remove (Boolean) : socket 'Remove' (id: Remove)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']

        Returns
        -------
        - grid
        """
        node = Node('Get Named Grid', {'Volume': self, 'Name': name, 'Remove': remove}, data_type=data_type)
        self._jump(node._out)
        return node.grid

