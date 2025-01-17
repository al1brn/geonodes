from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

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
        - node [point_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='POINTCLOUD')
        return node

    @classmethod
    def DistributeingridDensityRandom(cls, grid=None, density=None, seed=None):
        """ > Node <&Node Distribute Points in Grid>

        Information
        -----------
        - Parameter 'mode' : 'DENSITY_RANDOM'

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Density': density, 'Seed': seed}, mode='DENSITY_RANDOM')
        return cls(node._out)

    @classmethod
    def DistributeingridDensityGrid(cls, grid=None, spacing=None, threshold=None):
        """ > Node <&Node Distribute Points in Grid>

        Information
        -----------
        - Parameter 'mode' : 'DENSITY_GRID'

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Spacing': spacing, 'Threshold': threshold}, mode='DENSITY_GRID')
        return cls(node._out)

    @classmethod
    def DistributeInGrid(cls, grid=None, density=None, seed=None, mode='DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - mode (str): parameter 'mode' in ['DENSITY_RANDOM', 'DENSITY_GRID']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Distribute Points in Grid', 'mode', mode, 'DistributeInGrid', ('DENSITY_RANDOM', 'DENSITY_GRID'))
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Density': density, 'Seed': seed}, mode=mode)
        return cls(node._out)

    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Node <&Node Instance on Points>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instance (Geometry) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', sockets={'Points': self, 'Selection': self._sel, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def interpolate_curves(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Node <&Node Interpolate Curves>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - guide_curves (Geometry) : socket 'Guide Curves' (id: Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve [closest_index_ (Integer), closest_weight_ (Float)]
        """
        node = Node('Interpolate Curves', sockets={'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': self, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node._out

    @classmethod
    def Points(cls, count=None, position=None, radius=None):
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
        node = Node('Points', sockets={'Count': count, 'Position': position, 'Radius': radius})
        return cls(node._out)

    def to_curves(self, curve_group_id=None, weight=None):
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
        node = Node('Points to Curves', sockets={'Points': self, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out

    def to_sdf_grid(self, radius=None, voxel_size=None):
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
        node = Node('Points to SDF Grid', sockets={'Points': self, 'Radius': radius, 'Voxel Size': voxel_size})
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
        node = Node('Points to Vertices', sockets={'Points': self, 'Selection': self._sel})
        return node._out

    def to_volume(self, density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Points to Volume>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - radius (Float) : socket 'Radius' (id: Radius)
        - resolution_mode (str): parameter 'resolution_mode' in ['VOXEL_AMOUNT', 'VOXEL_SIZE']

        Returns
        -------
        - Volume
        """
        utils.check_enum_arg('Points to Volume', 'resolution_mode', resolution_mode, 'to_volume', ('VOXEL_AMOUNT', 'VOXEL_SIZE'))
        node = Node('Points to Volume', sockets={'Points': self, 'Density': density, 'Voxel Amount': voxel_amount, 'Radius': radius}, resolution_mode=resolution_mode)
        return node._out

    @property
    def radius(self):
        """ Property get node <Node Set Point Radius>
        """
        return Node('Radius', sockets={})._out

    @radius.setter
    def radius(self, radius=None):
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
        node = Node('Set Point Radius', sockets={'Points': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

