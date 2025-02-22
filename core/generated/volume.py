from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Volume(Socket):
    """"
    $DOC SET hidden
    """
    def distribute_points_density_random(self, density=None, seed=None):
        """ > Node <&Node Distribute Points in Volume>

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'mode' : 'DENSITY_RANDOM'

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Volume', sockets={'Volume': self, 'Density': density, 'Seed': seed}, mode='DENSITY_RANDOM')
        return node._out

    def distribute_points_density_grid(self, spacing=None, threshold=None):
        """ > Node <&Node Distribute Points in Volume>

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'mode' : 'DENSITY_GRID'

        Arguments
        ---------
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Volume', sockets={'Volume': self, 'Spacing': spacing, 'Threshold': threshold}, mode='DENSITY_GRID')
        return node._out

    def distribute_points(self, density=None, seed=None, mode='DENSITY_RANDOM'):
        """ > Node <&Node Distribute Points in Volume>

        Information
        -----------
        - Socket 'Volume' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - mode (str): parameter 'mode' in ['DENSITY_RANDOM', 'DENSITY_GRID']

        Returns
        -------
        - Cloud
        """
        utils.check_enum_arg('Distribute Points in Volume', 'mode', mode, 'distribute_points', ('DENSITY_RANDOM', 'DENSITY_GRID'))
        node = Node('Distribute Points in Volume', sockets={'Volume': self, 'Density': density, 'Seed': seed}, mode=mode)
        return node._out

    def get_named_grid(self, name=None, remove=None, data_type='FLOAT'):
        """ > Node <&Node Get Named Grid>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Volume' : self

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - remove (Boolean) : socket 'Remove' (id: Remove)
        - data_type (str): parameter 'data_type' in ['FLOAT', 'VECTOR']

        Returns
        -------
        - Volume [grid_ (Float)]
        """
        utils.check_enum_arg('Get Named Grid', 'data_type', data_type, 'get_named_grid', ('FLOAT', 'VECTOR'))
        node = Node('Get Named Grid', sockets={'Volume': self, 'Name': name, 'Remove': remove}, data_type=data_type)
        self._jump(node._out)
        return self._domain_to_geometry

    def named_float_grid(self, name=None, remove=None):
        """ > Node <&Node Get Named Grid>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'data_type' : 'FLOAT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - remove (Boolean) : socket 'Remove' (id: Remove)

        Returns
        -------
        - Volume [grid_ (Float)]
        """
        node = Node('Get Named Grid', sockets={'Volume': self, 'Name': name, 'Remove': remove}, data_type='FLOAT')
        self._jump(node._out)
        return self._domain_to_geometry

    def named_vector_grid(self, name=None, remove=None):
        """ > Node <&Node Get Named Grid>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'data_type' : 'VECTOR'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - remove (Boolean) : socket 'Remove' (id: Remove)

        Returns
        -------
        - Volume [grid_ (Vector)]
        """
        node = Node('Get Named Grid', sockets={'Volume': self, 'Name': name, 'Remove': remove}, data_type='VECTOR')
        self._jump(node._out)
        return self._domain_to_geometry

    def store_named_grid(self, name=None, grid=None):
        """ > Node <&Node Store Named Grid>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'data_type' : depending on 'grid' type

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - grid (Float) : socket 'Grid' (id: Grid)

        Returns
        -------
        - Volume
        """
        data_type = utils.get_argument_data_type(grid, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Volume.store_named_grid', 'grid')
        node = Node('Store Named Grid', sockets={'Volume': self, 'Name': name, 'Grid': grid}, data_type=data_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
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
        node = Node('Volume Cube', sockets={'Density': density, 'Background': background, 'Min': min, 'Max': max, 'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})
        return cls(node._out)

    def to_mesh(self, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ > Node <&Node Volume to Mesh>

        Information
        -----------
        - Socket 'Volume' : self

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)
        - resolution_mode (str): parameter 'resolution_mode' in ['GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Volume to Mesh', 'resolution_mode', resolution_mode, 'to_mesh', ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE'))
        node = Node('Volume to Mesh', sockets={'Volume': self, 'Threshold': threshold, 'Adaptivity': adaptivity}, resolution_mode=resolution_mode)
        return node._out

    def to_mesh_grid(self, threshold=None, adaptivity=None):
        """ > Node <&Node Volume to Mesh>

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'resolution_mode' : 'GRID'

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Volume to Mesh', sockets={'Volume': self, 'Threshold': threshold, 'Adaptivity': adaptivity}, resolution_mode='GRID')
        return node._out

    def to_mesh_voxel_amount(self, voxel_amount=None, threshold=None, adaptivity=None):
        """ > Node <&Node Volume to Mesh>

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'resolution_mode' : 'VOXEL_AMOUNT'

        Arguments
        ---------
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Volume to Mesh', sockets={'Volume': self, 'Voxel Amount': voxel_amount, 'Threshold': threshold, 'Adaptivity': adaptivity}, resolution_mode='VOXEL_AMOUNT')
        return node._out

    def to_mesh_voxel_size(self, voxel_size=None, threshold=None, adaptivity=None):
        """ > Node <&Node Volume to Mesh>

        Information
        -----------
        - Socket 'Volume' : self
        - Parameter 'resolution_mode' : 'VOXEL_SIZE'

        Arguments
        ---------
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)
        - threshold (Float) : socket 'Threshold' (id: Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (id: Adaptivity)

        Returns
        -------
        - Mesh
        """
        node = Node('Volume to Mesh', sockets={'Volume': self, 'Voxel Size': voxel_size, 'Threshold': threshold, 'Adaptivity': adaptivity}, resolution_mode='VOXEL_SIZE')
        return node._out

