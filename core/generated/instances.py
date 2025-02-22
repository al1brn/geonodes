from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

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
        - node [instance_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='INSTANCES')
        return node

    @classmethod
    def FromGeometry(cls, *geometry):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Instances
        """
        node = Node('Geometry to Instance', sockets={'Geometry': list(geometry)})
        return cls(node._out)

    @classmethod
    def ImportOBJ(cls, path=None):
        """ > Node <&Node Import OBJ>

        Arguments
        ---------
        - path (String) : socket 'Path' (id: Path)

        Returns
        -------
        - Instances
        """
        node = Node('Import OBJ', sockets={'Path': path})
        return cls(node._out)

    @classmethod
    @property
    def rotation(cls):
        """ > Node <&Node Instance Rotation>

        Returns
        -------
        - Rotation
        """
        node = Node('Instance Rotation', sockets={})
        return node._out

    @classmethod
    @property
    def instance_scale(cls):
        """ > Node <&Node Instance Scale>

        Returns
        -------
        - Vector
        """
        node = Node('Instance Scale', sockets={})
        return node._out

    def to_points(self, position=None, radius=None):
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
        node = Node('Instances to Points', sockets={'Instances': self, 'Selection': self._sel, 'Position': position, 'Radius': radius})
        return node._out

    def rotate(self, rotation=None, pivot_point=None, local_space=None):
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
        node = Node('Rotate Instances', sockets={'Instances': self, 'Selection': self._sel, 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})
        self._jump(node._out)
        return self._domain_to_geometry

    def scale(self, scale=None, center=None, local_space=None):
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
        node = Node('Scale Instances', sockets={'Instances': self, 'Selection': self._sel, 'Scale': scale, 'Center': center, 'Local Space': local_space})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_transform(self, transform=None):
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
        node = Node('Set Instance Transform', sockets={'Instances': self, 'Selection': self._sel, 'Transform': transform})
        self._jump(node._out)
        return self._domain_to_geometry

    def translate(self, translation=None, local_space=None):
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
        node = Node('Translate Instances', sockets={'Instances': self, 'Selection': self._sel, 'Translation': translation, 'Local Space': local_space})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def transform(self):
        """ Property get node <Node Set Instance Transform>
        """
        return Node('Instance Transform', sockets={})._out

    @transform.setter
    def transform(self, transform=None):
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
        node = Node('Set Instance Transform', sockets={'Instances': self, 'Selection': self._sel, 'Transform': transform})
        self._jump(node._out)
        return self._domain_to_geometry

