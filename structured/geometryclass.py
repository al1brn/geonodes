import bpy

from geonodes.structured.scripterror import NodeError
from geonodes.structured import constants
from geonodes.structured import utils
from geonodes.structured.treeclass import Tree, Node
from geonodes.structured.socketclass import DataSocket
from geonodes.structured.booleanclass import Boolean
from geonodes.structured.floatclass import Float, Integer
from geonodes.structured.vectorclass import Vector, Rotation

# =============================================================================================================================
# Domain : the root class implements all the geometry methods which don't depend upon de domain

class GeoBase:

    # =============================================================================================================================
    # Read only properties

    @classmethod
    @property
    def ID(cls):
        return Node('ID')._out

    @classmethod
    @property
    def Index(cls):
        return Node('Index')._out

    @classmethod
    @property
    def Normal(cls):
        return Node('Normal')._out

    @classmethod
    @property
    def Radius(cls):
        return Node('Radius')._out

    @classmethod
    @property
    def Position(cls):
        return Node('Position')._out

    @classmethod
    def named_attribute(cls, name, attribute):
        return attribute.NamedAttribute(name)

    # ----- Position

    @property
    def position(self):
        return GeoBase.Position

    @position.setter
    def position(self, value):
        node = Node('Set Position', {'Geometry': self._geometry, 'Selection': self.get_selection, 'Position': value})
        return self._geometry._jump(node._out)

    @property
    def offset(self):
        raise NodeError(f"offset is write only property")

    @offset.setter
    def offset(self, value):
        node = Node('Set Position', {'Geometry': self._geometry, 'Selection': self.get_selection, 'Offset': value})
        return self._geometry._jump(node._out)

    # ----- ID

    @property
    def id(self):
        return GeoBase.ID

    @id.setter
    def id(self, value):
        node = Node('Set ID', {'Geometry': self._geometry, 'Selection': self.get_selection, 'ID': value})
        return self._geometry._jump(node._out)

    # ====================================================================================================
    # Selection mechanism

    # ----- Selection socket is used once

    @property
    def get_selection(self):
        if hasattr(self, '_selection'):
            sel = self._selection
            self._selection = None
            return sel
        else:
            return None

    # ----- Set the selection
    # Domain array index can be:
    # - a boolean
    # - an int -> int == index
    # - a tuple of ints -> or on (int == index)
    # - a slice -> index matches the slice

    def __getitem__(self, selection):

        if selection is None:
            self._selection = None
            return

        if isinstance(selection, slice):
            if slice.start is None:
                selection = GeoBase.Index.less_than(slice.stop)
            elif slice.stop is None:
                selection = GeoBase.Index.greater_equal(slice.start)
            else:
                a = (selection.start + selection.stop)/2
                dist = a - selection.start + .1
                selection = Float(GeoBase.Index).equal(a, epsilon=dist)

        elif isinstance(selection, tuple):
            sel = None
            idx = GeoBase.Index
            for item in selection:
                if sel is None:
                    sel = idx.equal(item)
                else:
                    sel |= idx.equal(item)

            selection = sel

        else:
            socket_type = utils.get_value_socket_type(selection)
            if socket_type in ['INT', 'VALUE', 'FLOAT']:
                selection = GeoBase.Index.equal(selection)

        self._selection = Boolean(selection)

        return self

# =============================================================================================================================
# Geometry

class Geometry(DataSocket, GeoBase):

    @property
    def _geometry(self):
        return self

    # ====================================================================================================
    # Methods

    # ----- Index of nearest

    @staticmethod
    def index_of_nearest(position=None, group_id=None):
        return Node('Index of Nearest', {'Position': position, 'Group ID': group_id})

    # ----- Raycast

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        data_type = utils.get_value_data_type_1(attribute)
        node = Node('Raycast', {'Target Geometry': self, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length},
            data_type=data_type, mapping=mapping)

    def raycast_nearest(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='NEAREST'):
        return self.raycast(attribute, source_position, ray_direction, ray_length, mapping=mapping)





# =============================================================================================================================
# Domain

class Domain(GeoBase):

    DOMAIN_NAME = None

    def __init__(self, geometry):
        self._geometry  = geometry

    # ====================================================================================================
    # Properties

    # ----- Position

    @property
    def position(self):
        return Geometry.position

    @position.setter
    def position(self, value):
        node = Node('Set Position', {'Geometry': self._geometry, 'Selection': self.get_selection, 'Position': value})
        return self._geometry._jump(node._out)

    @property
    def offset(self):
        raise NodeError(f"Point.offset is write only property")

    @offset.setter
    def offset(self, value):
        node = Node('Set Position', {'Geometry': self._geometry, 'Selection': self.get_selection, 'Offset': value})
        return self._geometry._jump(node._out)

    # ====================================================================================================
    # Test domain in a restricted set

    def restrict_domain(self, domains=(), title=""):
        if self.DOMAIN_NAME in domains:
            return True
        raise NodeError(f"{title} restricted to domains {domains}, not '{self.DOMAIN_NAME}'")

    # ====================================================================================================
    # Methods

    def store_named_attribute(self, name, value=None):

        socket_type = utils.get_value_socket_type(value)
        data_type   = constants.DATA_TYPES_1.get(socket_type)

        node = Node('Store Named Attribute', {'Geometry': self._geometry, 'Selection': self.get_selection, 'Name': name, 'Value': value},
            data_type=data_type, domain=self.DOMAIN_NAME)

        return self._geometry._jump(node._out)

    # ----- Proximity

    def proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        self.restrict_domain(['POINT', 'EDGE', 'FACE'], 'Proximity')
        node = Node('Geometry Proximity', {'Geometry': self._geometry, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=self.DOMAIN_NAME + 'S')
        return node

    def extrude(self, offset=None, offset_scale=None, individual=None):
        self.restrict_domain(['POINT', 'EDGE', 'FACE'], 'Extrude')
        node = Node('Extrude Mesh', {'Mesh': self._geometry, 'Selection': self.get_selection, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode = self.DOMAIN_NAME + 'S')

        mesh = self._geometry._jump(node.mesh)
        mesh.top  = node.top
        mesh.side = node.side

        return mesh



class Point(Domain):
    DOMAIN_NAME = 'POINT'

    @property
    def count(self):
        return Integer(self._geometry.domain_size_node['Point Count'])

class Face(Domain):
    DOMAIN_NAME = 'FACE'

class Edge(Domain):
    DOMAIN_NAME = 'EDGE'

class Corner(Domain):
    DOMAIN_NAME = 'CORNER'

class Mesh(Geometry):
    def _reset(self):
        self.points  = Point(self)
        self.edges   = Edge(self)
        self.faces   = Face(self)
        self.corners = Corner(self)

    @classmethod
    def Cube(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        node = Node('Cube', {0: size, 1: vertices_x, 2: vertices_y, 3:vertices_z})
        mesh = Mesh(node.mesh)
        mesh.uv_map = node.uv_map
        return mesh

    @property
    def domain_size_node(self):
        if not hasattr(self, '_domain_size_node'):
            self._domain_size_node = Tree._cnode('GeometryNodeAttributeDomainSize', {0: self}, component='MESH')
        return self._domain_size_node

    # =============================================================================================================================
    # Methods
