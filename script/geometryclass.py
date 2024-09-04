"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : geometryclass
----------------------
- Implement geometry data socket

The Geometry base class for type 'GEOMETRY' has specialized children: Mesh, Curve, Points, Instances and Volume
each one implementing the node specific to their geometry.

In addition, nodes making use of a 'domain', parameter are implemented through Domain class.

``` python
# A node not specific to a geometry
Geometry().index_of_nearest()

# Nodes specific to geometries
Mesh().triangulate()
Curve().resample()

# Nodes requiring domain specification
Mesh().points.sample_index()
Mesh().faces.sample_index()
```

The domain specific to geometries are the followings:
    - Mesh:
        - points
        - faces
        - edges
        - corners
    - Curve:
        - points
        - splines
    - Instances
        - insts
    - Points
        - points

The components of a geometry can be separated with the following properties:

``` python
geo = Geometry()
mesh     = geo.mesh        # Node 'Separate Component', socket 'Mesh'
curve    = geo.curve       # Node 'Separate Component', socket 'Curve'
points   = geo.point_cloud # Node 'Separate Component', socket 'Point Cloud'
volume   = geo.volume      # Node 'Separate Component', socket 'Volume'
instance = geo.instances   # Node 'Separate Component', socket 'Instances'
```

classes
-------
- GeoBase       : Base class for Geometry and Domain
- Domain        : Domain base class
- Point         : POINT domain
- Vertex        : POINT domain for Mesh
- CloudPoint    : POINT domain for Points
- Face          : FACE domain
- Edge          : EDGE domain
- Corner        : CORNER domain
- Spline        : SPLINE domain
- Instance      : INSTANCE domain
- Geometry      : DataSocket of type 'Geometry'
- Mesh          : Subclass of Geometry specific to Mesh
- Curve         : Subclass of Geometry specific to Curve
- Instances     : Subclass of Geometry specific to Instances
- Points        : Subclass of Geometry specific to Points
- Volume        : Subclass of Geometry specific to Points

functions
---------

updates
-------
- creation : 2024/07/23
"""

import bpy

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Tree, Node, Layout
from .socketclass import NodeCache, DataSocket
from .booleanclass import Boolean
from .floatclass import Float
from .staticclass_gn import nd

# =============================================================================================================================
# =============================================================================================================================
# Interface for Geometry and Domain
# =============================================================================================================================
# =============================================================================================================================


# =============================================================================================================================

class GeoBase:

    @property
    def _geo_type(self):
        return type(self._geo)

    # =============================================================================================================================
    # Properties

    # ----- Position

    @property
    def position(self):
        return Node('Position')._out

    @position.setter
    def position(self, value):
        node = Node('Set Position', {'Geometry': self._geo, 'Selection': self._sel, 'Position': value})
        return self._geo._jump(node._out)

    @property
    def offset(self):
        raise NodeError(f"offset is write only property")

    @offset.setter
    def offset(self, value):
        node = Node('Set Position', {'Geometry': self._geo, 'Selection': self._sel, 'Offset': value})
        return self._geo._jump(node._out)

    # ----- ID

    @property
    def id(self):
        return GeoBase.ID

    @id.setter
    def id(self, value):
        node = Node('Set ID', {'Geometry': self._geo, 'Selection': self._sel, 'ID': value})
        return self._geo._jump(node._out)

    # ----- Material

    @property
    def material_index(self):
        return Node('Material Index')._out

    @material_index.setter
    def material_index(self, value):
        self._geo._jump(Node('Set Material Index', {'Geometry': self._geo, 'Selection': self._sel, 'Material Index': value})._out)

    @property
    def material(self):
        raise NodeError("Material property is write only.")

    @material.setter
    def material(self, value):
        self._geo._jump(Node('Set Material', {'Geometry': self._geo, 'Selection': self._sel, 'Material': value})._out)

    def replace_material(self, old=None, new=None):
        return self._geo._jump(Node('Replace Material', {'Geometry': self._geo, 'Old': old, 'New': new})._out)

    @classmethod
    def material_selection(cls, material=None):
        return Node('Material Selection', {'Material': material})._out

    # ====================================================================================================
    # Selection mechanism

    # ----- Selection socket is used once

    @property
    def _raw_sel(self):
        if hasattr(self, '_selection'):
            sel = self._selection
            self._selection = sel
            return sel
        else:
            return None

    @property
    def _sel(self):

        selection = self._raw_sel

        # No selection
        if selection is None:
            return None

        if isinstance(selection, slice):
            with Layout(f"selection = {selection}", color='AUTO_GEN'):
                if selection.start is None:
                    selection = nd.index.less_than(selection.stop)
                elif selection.stop is None:
                    selection = nd.index.greater_equal(selection.start)
                else:
                    a = (selection.start + selection.stop)/2
                    dist = a - selection.start + .1
                    selection = Float(nd.index).equal(a, epsilon=dist)

        elif isinstance(selection, tuple):
            with Layout(f"selection = tuple", color='AUTO_GEN'):
                sel = None
                idx = nd.index
                for item in selection:
                    if sel is None:
                        sel = idx.equal(item)
                    else:
                        sel |= idx.equal(item)

                selection = sel

        else:
            socket_type = utils.get_socket_type(selection)
            if socket_type in ['INT', 'VALUE', 'FLOAT']:
                with Layout(f"selection = []", color='AUTO_GEN'):
                    selection = nd.index.equal(selection)

        return selection

    # ----- Set the selection
    # Domain array index can be:
    # - a boolean
    # - an int -> int == index
    # - a tuple of ints -> or on (int == index)
    # - a slice -> index matches the slice

    def __getitem__(self, selection):
        # ----- Store the selection value
        # The selection is supposed to be a Boolean
        # If an Integer, a slice or a tuple, it is transformed into a boolean through _sel function
        # The _raw_sel function returns the passed value without transformation

        self._selection = selection
        return self

        """
        if selection is None:
            self._selection = None
            return self

        if isinstance(selection, slice):
            with Layout(f"selection = {selection}", color='AUTO_GEN'):
                if selection.start is None:
                    selection = nd.index.less_than(selection.stop)
                elif selection.stop is None:
                    selection = nd.index.greater_equal(selection.start)
                else:
                    a = (selection.start + selection.stop)/2
                    dist = a - selection.start + .1
                    selection = Float(nd.index).equal(a, epsilon=dist)

        elif isinstance(selection, tuple):
            with Layout(f"selection = tuple", color='AUTO_GEN'):
                sel = None
                idx = nd.index
                for item in selection:
                    if sel is None:
                        sel = idx.equal(item)
                    else:
                        sel |= idx.equal(item)

                selection = sel

        else:
            socket_type = utils.get_socket_type(selection)
            if socket_type in ['INT', 'VALUE', 'FLOAT']:
                with Layout(f"selection = []", color='AUTO_GEN'):
                    selection = nd.index.equal(selection)

        self._selection = Boolean(selection)

        return self
        """

# =============================================================================================================================
# =============================================================================================================================
# Geometry
# =============================================================================================================================
# =============================================================================================================================

class Geometry(DataSocket, GeoBase):

    SOCKET_TYPE = 'GEOMETRY'

    def __init__(self, value=None, name=None, tip=None):
        """ DataSocket of type 'GEOMETRY'.

        If value is None, a Group Input socket of type Geometry is created.
        When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

        Arguments
        ---------
        - value (DataSocket = None) : initial value
        - name (str = None) : Create an Group Input socket with the provided str
        - tip (str = None) : User tip (for Group Input sockets)
        - subtype (str='NONE') : socket subtype
        """

        bsock = utils.get_bsocket(value)

        # ---------------------------------------------------------------------------
        # This is not a socket : let's get the geometry as Group Input

        if bsock is None:

            tree = Tree.current_tree

            # ----- Name is None:
            # - group : we read the socket from its default name
            # - modifier : input geometry

            if name is None:
                name = type(self).__name__
                if tree._is_group:
                    bsock = tree.new_input('NodeSocketGeometry', name, description=tip)
                else:
                    bsock = tree.get_input_geometry(name, description=tip)

            # ----- Name is not None
            # - group : we want this name
            # - Modifier : we create the input geometry with this name

            else:
                if tree._is_group:
                    bsock = tree.new_input('NodeSocketGeometry', name, description=tip)
                else:
                    bsock = tree.get_input_geometry(name, description=tip)

        super().__init__(bsock)

    @property
    def _geo(self):
        return self

    # ====================================================================================================
    # Geometry nodes are created with
    # {'Geometry': self, 'Selection': self._sel}

    def _node(self, node_name, sockets={}, geometry='Geometry', selection='Selection', use_cache=False, **parameters):

        all_sockets = {**sockets}
        if geometry is not None:
            all_sockets[geometry] = self
        #if selection is not None:
        #    all_sockets[selection] = self._sel

        if use_cache:
            node = self._cache(node_name, sockets=all_sockets, **parameters)
        else:
            node = Node(node_name, sockets=all_sockets, **parameters)

        if selection is not None:
            node.plug_selection(self._sel)

        return node

    # ====================================================================================================
    # Methods

    # ----- Viewer

    def viewer(self, value=None):
        """ Create a viewer node.

        [!Node] Viewer

        Arguments
        ---------
        - value (DataSocket) : socket

        Returns
        -------
        - Node
        """
        return Node('Viewer', {'Geometry': self, 'Value': value}, data_type=utils.get_data_type(value))

    # ----- Operations

    def set_id(self, id=None):
        """ Set ID.

        [!Node] Set ID

        Arguments
        ---------
        - id (Integer) : socket

        Returns
        -------
        - Geometry
        """
        return Node("Set ID", {'Geometry': self, 'Selection': self._sel, 'ID': id})._out

    def set_position(self, position=None, offset=None):
        """ Set Position.

        [!Node] Set Position

        Arguments
        ---------
        - position (Vector) : socket

        Returns
        -------
        - Geometry
        """
        return Node("Set Position", {'Geometry': self, 'Selection': self._sel, 'Position': position, 'Offset': offset})._out

    def set_material(self, material=None):
        """ Set Material.

        [!Node] Set Material

        Arguments
        ---------
        - material (Material) : socket

        Returns
        -------
        - Geometry
        """
        return Node("Set Material", {'Geometry': self, 'Selection': self._sel, 'Material': material})._out

    def set_shade_smooth(self, shade_smooth=True, edge=False):
        """ Set Shade Smooth.

        [!Node] Set Shade Smooth

        Arguments
        ---------
        - shade_smooth (Boolean) : socket

        Returns
        -------
        - Geometry
        """
        return Node("Set Shade Smooth", {'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE' if edge else 'FACE')._out

    # ----- Remove named attribute

    def remove_named_attribute(self, name, exact=True):
        """ Remove named attribute

        [!Node] Remove Named Attribute

        Arguments
        ---------
        - name (String) : socket
        - exact (Boolean) : pattern_mode = 'EXACT' if True else 'WILDCARD'

        Returns
        -------
        - Geometry
        """
        #node = Node('Remove Named Attribute', {'Geometry': self, 'Name': name}, pattern_mode = 'EXACT' if exact else 'WILDCARD')
        #self._jump(node._out)
        return self._jump(Node('Remove Named Attribute', {'Geometry': self, 'Name': name}, pattern_mode = 'EXACT' if exact else 'WILDCARD')._out)

    # ====================================================================================================
    # Sample nodes without domain

    # ----- Index of nearest

    @staticmethod
    def index_of_nearest(position=None, group_id=None):
        """ Node 'Index of Nearest' (GeometryNodeIndexOfNearest)

        [!Node] Index of Nearest

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - group_id (Integer) : socket 'Group ID' (Group ID)

        Returns
        -------
        - Integer, [has_neighbor_]
        """

        index = Node('Index of Nearest', {'Position': position, 'Group ID': group_id})._out
        index.has_neighbor_ = index.node.has_neighbor
        return index

    # ----- Raycast

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, interpolated=True):
        """ Node 'Raycast' (GeometryNodeRaycast)

        [!Node] Raycast

        mapping in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (Attribute)
        - source_position (Vector) : socket 'Source Position' (Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (Ray Length)
        - interpolated (bool) : mapping = 'INTERPOLATED' if True, 'NEAREST' otherwise

        Returns
        -------
        - Node: [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        """

        data_type = utils.get_data_type(attribute, restrict_to=['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'])
        node = Node('Raycast', {'Target Geometry': self, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length},
            data_type=utils.get_data_type(attribute), mapping='INTERPOLATED' if interpolated else 'NEAREST')
        return node

    # ====================================================================================================
    # Geometry Operations

    def bake(self, **kwargs):

        node = Node('Bake', {'Geometry': self})

        items = node._bnode.bake_items
        for name, value in kwargs.items():
            items.new(utils.get_input_type(value), name)

        self._jump(node._out)

        return node

    @property
    def bounding_box(self):
        """ Property node 'Bounding Box' (GeometryNodeBoundBox)

        [!Node] Bounding Box

        Returns
        -------
        - Mesh [min_, max_]
        """
        bb = Mesh(Node('Bounding Box', {'Geometry': self})._out)
        bb.min_ = bb.node.min
        bb.max_ = bb.node.max
        return bb

    @property
    def convex_hull(self):
        """ Property node 'Convex Hull' (GeometryNodeConvexHull)

        [!Node] Convex Hull

        Returns
        -------
        - convex_hull (Geometry)
        """
        return Mesh(Node('Convex Hull', {'Geometry': self})._out)

    def merge_by_distance(self, distance=None, all=True):
        """ Node 'Merge by Distance' (GeometryNodeMergeByDistance)

        [!Node] Merge by Distance

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (Distance)
        - all (bool) : mode = 'ALL' if True, 'CONNECTED' otherwise

        Returns
        -------
        - geometry (Geometry)
        """
        return self._geo_type(self._node('Merge by Distance', {'Distance': distance}, mode = 'ALL' if all else 'CONNECTED')._out)

    def transform(self, translation=None, rotation=None, scale=None, matrix=None):
        """ Node 'Transform Geometry' (GeometryNodeTransform)

        [!Node] Transform Geometry

        If 'matrix' argument is None, the mode 'COMPONENTS' is set.
        If 'matrix' argument is not NOne, the mode 'MATRIX' is set and the other arguments are ignored.

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)
        - matrix (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - geometry (Geometry)
        """
        if matrix is None:
            return self._geo_type(Node('Transform Geometry', {'Geometry': self, 'Translation': translation, 'Rotation': rotation, 'Scale': scale}, mode='COMPONENTS')._out)
        else:
            return self._geo_type(Node('Transform Geometry', {'Geometry': self, 'Transform': matrix}, mode='MATRIX')._out)

    @property
    def separate_components(self):
        """ Property node 'Separate Components' (GeometryNodeSeparateComponents)

        [!Node] Separate Components

        Returns
        -------
        - Node: [mesh (Geometry), curve (Geometry), grease_pencil (Geometry), point_cloud (Geometry), volume (Geometry), instances (Geometry)]
        """
        return self._cache('Separate Components', {'Geometry': self})

    @property
    def mesh(self):
        """ Property mesh component

        [!Node] Separate Components

        Returns
        -------
        - Mesh
        """
        return Mesh(self.separate_components.mesh)

    @property
    def curve(self):
        """ Property curve component

        [!Node] Separate Components

        Returns
        -------
        - Curve
        """
        return Curve(self.separate_components.curve)

    @property
    def point_cloud(self):
        """ Property cloud component

        [!Node] Separate Components

        Returns
        -------
        - Cloud
        """
        return Cloud(self.separate_components.point_cloud)

    @property
    def volume(self):
        """ Property volume component

        [!Node] Separate Components

        Returns
        -------
        - Volume
        """
        return Volume(self.separate_components.volume)

    @property
    def instances(self):
        """ Property instances component

        [!Node] Separate Components

        Returns
        -------
        - Instances
        """
        return Instances(self.separate_components.instances)

    def join(self, *geometries):
        """ Node 'Join Geometry' (GeometryNodeJoinGeometry)

        [!Node] Join Geometry

        Operator + can be used : ``` geo + other_geo ``` is equivalent to ``` geo.join(other) ```
        If all the geometries are of the same type, the returned geometry uses this type.

        ``` python
        cube = Mesh.Cube()
        cone = Mesh.Cone()
        circle = Curve.Circle()

        # Returns Mesh
        mesh = cube.join(cone)
        assert(isinstance(mesh, Mesh))

        # Returns Geometry
        geo = mesh + circle
        assert(isinstance(geo, Geometry))
        ```

        Arguments
        ---------
        - *geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Geometry
        """

        if False and self.node._bnode.bl_idname == 'GeometryNodeJoinGeometry':
            node = self.node
            node.set_input_sockets({'Geometry': list(geometries)})
        else:
            node = Node('Join Geometry', {'Geometry': [self] + list(geometries)})

        geo = node._out
        classes = set()
        classes.add(type(self))
        for g in geometries:
            classes.add(type(g))
        if len(classes) == 1:
            return list(classes)[0](geo)
        else:
            return geo

    # ====================================================================================================
    # Operations

    def to_instance(self, *geometries):
        """ Node 'Geometry to Instance' (GeometryNodeGeometryToInstance)

        [!Node] Geometry to Instance

        Arguments
        ---------
        - geometries (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Instances
        """
        return Instances.FromGeometry([self] + list(geometries))

    # ====================================================================================================
    # Python Operations

    def __add__(self, other):
        return self.join(other)

# =============================================================================================================================
# =============================================================================================================================
# Domain
# =============================================================================================================================
# =============================================================================================================================

class Domain(GeoBase, NodeCache):

    DOMAIN_NAME = None

    def __init__(self, geometry):
        self._geo  = geometry
        self._cache_reset()

    def __str__(self):
        return f"<Domain {self.DOMAIN_NAME} of {self._geo}>"

    # ----- Overrides selection
    # Selection can be done either on the geometry or on the domain (or both but strange !)

    @property
    def _sel(self):
        sel = super()._sel
        geo_sel = self._geo._sel
        if sel is None:
            return geo_sel
        elif geo_sel is None:
            return sel
        else:
            return sel & geo_sel

    # ====================================================================================================
    # Domain nodes are created with
    # {'Geometry': self._geo, 'Selection': self._sel}, domain=self.DOMAIN_NAME

    def _node(self, node_name, sockets={}, geometry='Geometry', selection='Selection', domain='domain', use_cache=False, **parameters):

        all_sockets = {**sockets}
        if geometry is not None:
            all_sockets[geometry] = self._geo
        #if selection is not None:
        #    all_sockets[selection] = self._sel

        all_parameters = {**parameters}
        if domain is not None:
            all_parameters[domain] = self.DOMAIN_NAME

        if use_cache:
            node = self._cache(node_name, sockets=all_sockets, **all_parameters)
        else:
            node = Node(node_name, sockets=all_sockets, **all_parameters)

        if selection is not None:
            node.plug_selection(self._sel)

        return node

    # ====================================================================================================
    # Test domain in a restricted set

    def restrict_domain(self, domains=(), title=""):
        if self.DOMAIN_NAME in domains:
            return True
        raise NodeError(f"{title} restricted to domains {domains}, not '{self.DOMAIN_NAME}'")

    def exclude_corner(self, title):
        return self.restrict_domain(['POINT', 'FACE', 'EDGE', 'CURVE', 'INSTANCE'])

    def plural_domain(self, domains=None, title=""):
        PLURAL = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES', 'CORNER': 'CORNERS', 'SPLINE': 'SPLINES', 'CURVE': 'SPLINES'}
        if domains is not None:
            self.restrict_domain(domains=domains, title=title)
        return PLURAL[self.DOMAIN_NAME]

    # Rename domain name
    def domain_name(self, rename={}):
        if self.DOMAIN_NAME in rename:
            return rename[self.DOMAIN_NAME]
        else:
            return self.DOMAIN_NAME

    # ====================================================================================================
    # Properties

    # ====================================================================================================
    # Methods

    # ----- Viewer

    def viewer(self, value=None):
        return self._node('Viewer', {'Value': value}, data_type=utils.get_data_type(value))

    # ----- Attribute statistic

    def attribute_statistic(self, attribute=None):
        data_type = utils.get_data_type(attribute, ['FLOAT_VECTOR', 'VECTOR', 'ROTATION', 'COLOR'], 'FLOAT')

        return self._node('Attribute Statistic', {'Attribute': attribute}, data_type=data_type, use_cache=False)

    # ----- Capture attribute

    def capture_attribute(self, attribute=None, **others):
        """ Node 'Capture Attribute' (GeometryNodeCaptureAttribute)

        [!Node] Capture Attribute

        This method return the capture of 'attribute' argument if not keyword arguments are provided,
        otherwise returns the node.

        ``` python
        with GeoNodes("Capture Attribute"):
            mesh = Mesh()

            # A single anonymous attribute
            p = mesh.points.capture_attribute(nd.position)
            assert(isinstance(p, Vector))

            # Only named attributes
            node = mesh.faces.capture_attribute(pos=nd.position, idx=nd.material_index)
            assert(isinstance(node, Node))
            assert(isinstance(node.pos, Vector))
            assert(isinstance(node.idx, Integer))

            # Anonymous attribute plus named attributes
            node = mesh.faces.capture_attribute(nd.position, idx=nd.material_index)
            assert(isinstance(node, Node))
            assert(isinstance(node.attribute, Vector))
            assert(isinstance(node.idx, Integer))
        ```

        Arguments
        ---------
        - attribute (DataSocket) : attribute to capture
        - **others (DataSockets): named attributes to capture

        Returns
        -------
        - DataSocket (no keyword arguments) or Node (when keyword arguments)
        """

        node = self._node('Capture Attribute')
        items = node._bnode.capture_items
        attributes = others if attribute is None else {'attribute': attribute, **others}
        for i, (attr_name, attr_value) in enumerate(attributes.items()):
            items.new(utils.get_input_type(attr_value), attr_name)
            node.plug_value_into_socket(attr_value, node.in_socket(1 + i))

        self._geo._jump(node._out)

        if len(attributes) == 0:
            return node
        elif len(others) == 0:
            return node.attribute
        else:
            return node

    def capture(self, attribute=None, **others):
        """ Node 'Capture Attribute' (GeometryNodeCaptureAttribute)

        [!Node] Capture Attribute

        synonym of 'capture_named_attribute'
        """
        return self.capture_attribute(attribute=attribute, **others)

    # ----- Store named attribute

    def store_named_attribute(self, name, value=None):
        """ Node 'Store Named Attribute' (GeometryNodeStoreNamedAttribute)

        [!Node] Store Named Attribute

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')


        Arguments
        ---------
        - name (String) : socket 'Name' (Name)
        - value (Float) : socket 'Value' (Value)

        Returns
        -------
        - Geometry
        """

        data_type   = utils.get_data_type(value)
        node = self._node('Store Named Attribute', {'Name': name, 'Value': value}, data_type=data_type)

        return self._geo._jump(node._out)

    def store(self, name, value=None):
        """ Node 'Store Named Attribute' (GeometryNodeStoreNamedAttribute)

        [!Node] Store Named Attribute

        Synonym of 'store_named_attribute'
        """
        return self.store_named_attribute(name, value=value)

    # ====================================================================================================
    # Sample nodes with domain

    def proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        """ Node 'Geometry Proximity' (GeometryNodeProximity)

        [!Node] Geometry Proximity

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sample_position (Vector) : socket 'Sample Position' (Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (Sample Group ID)

        Returns
        -------
        - Vector [distance_, is_valid_]
        """

        target = self.restrict_domain(['POINT', 'EDGE', 'FACE'], 'Proximity')
        position = Node('Geometry Proximity', {'Geometry': self._geo, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=self.DOMAIN_NAME + 'S')._out
        position.distance_ = position.node.distance
        position.is_valid_ = position.node.is_valid
        return position

    def sample_index(self, value=None, index=0, clamp=False):
        """ Node 'Sample Index' (GeometryNodeSampleIndex)

        [!Node] Sample Index

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - index (Integer) : socket 'Index' (Index)
        - clamp (bool): Node.clamp

        Returns
        -------
        - DataSocket
        """

        return self._node('Sample Index', {'Value': value, 'Index': index}, clamp=clamp, data_type=utils.get_data_type(value))._out

    def sample_nearest(self, sample_position=None):
        """ Node 'Sample Nearest' (GeometryNodeSampleNearest)

        [!Node] Sample Nearest

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER')

        Arguments
        ---------
        - sample_position (Vector) : socket 'Sample Position' (Sample Position)

        Returns
        -------
        - Integer
        """

        return self._node('Sample Nearest', {'Sample Position': sample_position})._out

    # ====================================================================================================
    # Geometry Operations

    def delete_geometry(self, mode='ALL'):
        """ Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

        [!Node] Delete Geometry

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - mode (str): Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - geometry (Geometry)
        """
        self.exclude_corner('delete_geometry')
        return self._geo_type(self._node('Delete Geometry', mode=mode)._out)

    def delete(self, mode='ALL'):
        """ Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

        [!Node] Delete Geometry

        Synonym of 'delete_geometry'
        """

        return self.delete_geometry(mode=mode)

    def delete_all(self):
        """ Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

        [!Node] Delete Geometry

        Shortcut for : ``` domain.delete_geometry(mode='ALL') ```
        """
        return self.delete_geometry(mode='ALL')

    def delete_faces(self):
        """ Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

        [!Node] Delete Geometry

        Shortcut for : ``` domain.delete_geometry(mode='ONLY_FACE') ```
        """
        return self.delete_geometry(mode='ONLY_FACE')

    def delete_edges_and_faces(self):
        """ Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

        [!Node] Delete Geometry

        Shortcut for : ``` domain.delete_geometry(mode='EDGE_FACE') ```
        """
        return self.delete_geometry(mode='EDGE_FACE')

    def duplicate_elements(self, amount=1):
        """ Node 'Duplicate Elements' (GeometryNodeDuplicateElements)

        [!Node] Duplicate Elements

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (Amount)

        Returns
        -------
        - Geometry [duplicate_index_]
        """

        self.exclude_corner('duplicate_elements')
        domain = self.domain_name(rename={'CURVE': 'SPLINE'})
        #geo = self._geo_type(self._node('Duplicate Elements', {'Amount': amount}, domain=domain)._out)
        geo =self._geo_type(Node('Duplicate Elements', {'Geometry': self._geo, 'Selection': self._sel, 'Amount': amount}, domain=domain)._out)
        geo.duplicate_index_= geo.node.duplicate_index
        return geo

    def sort_elements(self, group_id=None, sort_weight=None):
        """ Node 'Sort Elements' (GeometryNodeSortElements)

        [!Node] Sort Elements

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (Sort Weight)

        Returns
        -------
        - Geometry
        """

        self.exclude_corner('sort_elements')
        return self._geo_type(self._node('Sort Elements', {'Group ID': group_id, 'Sort Weight': sort_weight})._out)

    def separate(self):
        """ Node 'Separate Geometry' (GeometryNodeSeparateGeometry)

        [!Node] Separate Geometry

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Returns
        -------
        - Geometry [inverted_]
        """

        self.exclude_corner('separate')
        geo = self._geo_type(self._node('Separate Geometry')._out)
        geo.inverted_ = self._geo_type(geo.node.inverted)
        return geo

    def split_to_instances(self, group_id=None):
        """ Node 'Split to Instances' (GeometryNodeSplitToInstances)

        [!Node] Split to Instances

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)

        Returns
        -------
        - instances [group_id_]
        """

        self.exclude_corner('split_to_instances')
        instances = Instances(self._node('Split to Instances', {'Group ID': group_id})._out)
        instances.group_id_ = instances.node.group_id
        return instances

    # ----- Mesh conversion to points

    def to_points(self, position=None, radius=None):
        """ Node 'Mesh to Points' (GeometryNodeMeshToPoints)

        [!Node] Mesh to Points

        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Geometry
        """

        mode = self.plural_domain(['POINT', 'EDGE', 'FACE', 'CORNER'], 'Mesh to Point')
        return Cloud(Node('Mesh to Points', {'Mesh': self._geo, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode=mode)._out)

    # ----- Extrusion

    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ Node 'Extrude Mesh' (GeometryNodeExtrudeMesh)

        [!Node] Extrude Mesh

        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES')

        ``` python
        with GeoNodes("Extrusion"):
            cube = Mesh.Cube()

            cube = cube.faces.extrude(nd.normal, .5)
            cube = cube.faces[cube.top_].extrude(offset_scale=0)
            top = cube.top_
            cube = cube.faces[top].scale(scale=.8, uniform=False)
            cube = cube.faces[top].scale(scale=.6, uniform=True)
            cube = cube.faces[top].extrude(offset_scale=.5)
            cube = cube.faces[cube.top_].flip()

            cube.out()
        ```

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (Offset)
        - offset_scale (Float) : socket 'Offset Scale' (Offset Scale)
        - individual (Boolean) : socket 'Individual' (Individual)

        Returns
        -------
        - Geometry [top_, side_]
        """

        mode = self.plural_domain(['POINT', 'EDGE', 'FACE'], 'Extrude Mesh')
        node = Node('Extrude Mesh', {'Mesh': self._geo, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode = mode)

        mesh = Mesh(node.mesh)
        mesh.top_  = node.top
        mesh.side_ = node.side

        return mesh

    # ----- Field

    def accumulate_field(self, value=None, group_id=None, ):
        """ Node 'Accumulate Field' (GeometryNodeAccumulateField)

        [!Node] Accumulate Field

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - group_id (Integer) : socket 'Group ID' (Group Index)

        Returns
        -------
        - Node: [leading (Float), trailing (Float), total (Float)]
        """

        data_type = utils.get_data_type(value, ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'))
        return Node('Accumulate Field', {'Value': value, 'Group ID': group_id}, data_type=data_type, domain=self.DOMAIN_NAME)

    def evaluate_at_index(self, index=None, value=None):
        """ Node 'Evaluate at Index' (GeometryNodeFieldAtIndex)

        [!Node] Evaluate at Index

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - index (Integer) : socket 'Index' (Index)
        - value (Float) : socket 'Value' (Value)

        Returns
        -------
        - DataSocket
        """

        data_type = utils.get_data_type(value)
        return Node('Evaluate at Index', {'Index': index, 'Value': value}, data_type=data_type, domain=self.DOMAIN_NAME)._out

    def evaluate_on_domain(self, value=None):
        """ Node 'Evaluate on Domain' (GeometryNodeFieldOnDomain)

        [!Node] Evaluate on Domain

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)

        Returns
        -------
        - DataSocket
        """

        data_type = utils.get_data_type(value)
        return Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain=self.DOMAIN_NAME)._out


# =============================================================================================================================
# =============================================================================================================================
# Point Domain
# =============================================================================================================================
# =============================================================================================================================

class Point(Domain):
    DOMAIN_NAME = 'POINT'

    @property
    def count(self):
        """ Node 'Domain Size' (GeometryNodeAttributeDomainSize)

        [!Node] Domain Size

        Socket 'Point Count' of node 'Domain Size'

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.point_count

    # ----- Instance on points

    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Node 'Instance on Points' (GeometryNodeInstanceOnPoints)

        [!Node] Instance on Points

        Arguments
        ---------
        - instance (Geometry) : socket 'Instance' (Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (Instance Index)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)

        Returns
        -------
        - instances (Geometry)
        """

        return Instances(Node('Instance on Points', {'Points': self._geo, 'Selection': self._sel,
                'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index,
                'Rotation': rotation, 'Scale': scale})._out)

class Vertex(Point):

    # ----- Vertex neighbors

    @property
    def neighbors(self):
        """ Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

        [!Node] Vertex Neighbors

        Returns
        -------
        - Node: [vertex_count (Integer), face_count (Integer)]
        """

        return self._cache('Vertex Neighbors')

    @property
    def neighbors_vertex_count(self):
        """ Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

        [!Node] Vertex Neighbors

        Returns
        -------
        - Integer : Socket 'Vertex Count' of node 'Vertex Neighbors'
        """
        return self.neighbors.vertex_count

    @property
    def neighbors_face_count(self):
        """ Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

        [!Node] Vertex Neighbors

        Returns
        -------
        - Integer : Socket 'Face Count' of node 'Vertex Neighbors'
        """
        return self.neighbors.face_count

    # ----- Edge paths to selection

    def paths_to_selection(self, next_vertex_index):
        """ Node 'Edge Paths to Selection' (GeometryNodeEdgePathsToSelection)

        [!Node] Edge Paths to Selection

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (Next Vertex Index)

        Returns
        -------
        - Boolean
        """

        return Node('Edge Paths to Selection', {'Start Vertices': self._sel, 'Next Vertex Index': next_vertex_index})._out

    # ----- Edge paths to curves

    def edge_paths_to_curves(self, next_vertex_index=None):
        """ Node 'Edge Paths to Curves' (GeometryNodeEdgePathsToCurves)

        [!Node] Edge Paths to Curves

        Arguments
        ---------
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (Next Vertex Index)

        Returns
        -------
        - Curve
        """

        return Curve(Node('Edge Paths to Curves', {'Mesh': self._geo, 'Start Vertices': self._sel, 'Next Vertex Index': next_vertex_index})._out)

    # ----- Topology

    @classmethod
    def edge_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ Node 'Edges of Vertex' (GeometryNodeEdgesOfVertex)

        [!Node] Edges of Vertex

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (Vertex Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer [total_]
        """

        index = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

    @classmethod
    def corner_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ Node 'Corners of Vertex' (GeometryNodeCornersOfVertex)

        [!Node] Corners of Vertex

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (Vertex Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer [total_]
        """

        index = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

class SplinePoint(Point):

    # ----- Handle positions

    @classmethod
    def handle_positions(cls, relative=None):
        """ Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

        [!Node] Curve Handle Positions

        Arguments
        ---------
        - relative (Boolean) : socket 'Relative' (Relative)

        Returns
        -------
        - Node: [left (Vector), right (Vector)]
        """

        return Node('Curve Handle Positions', {'Relative': relative})

    def set_handle_positions(self, position=None, offset=None, mode=None):
        """ Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

        [!Node] Set Handle Positions

        ``` python
        with GeoNodes("Curve handles"):
            curve = Curve.Line(0, (20, 0, 0)).resample(20)

            curve.splines.type = 'BEZIER'

            with Layout("Set by str"):
                curve.points.left_handle_type = 'AUTO'
                curve.points.right_handle_type = 'AUTO'
                curve.points[(nd.index % 2).equal(0)].handle_type = 'ALIGN'

                curve.points[curve.points.handle_align].offset = (0, 0, 2)

            with Layout("Both set boolean"):
                curve.points[1].handle_auto = True
                curve.points[3].handle_free = True
                curve.points[5].handle_vector = True
                curve.points[7].handle_align = True

            with Layout("Left / right set boolean"):
                curve.points[9].left_handle_auto = True
                curve.points[9].right_handle_free = True
                curve.points[11].left_handle_free = True
                curve.points[11].right_handle_vector = True
                curve.points[13].left_handle_vector = True
                curve.points[13].right_handle_align = True
                curve.points[15].left_handle_align = True
                curve.points[15].right_handle_auto = True

            with Layout("Left selection"):
                curve.points[curve.points.left_handle_auto].offset = (0, 0.5, 0)
                curve.points[curve.points.left_handle_free].offset = (0, 1.0, 0)
                curve.points[curve.points.left_handle_vector].offset = (0, 1.5, 0)
                curve.points[curve.points.left_handle_align].offset = (0, 2.0, 0)

            with Layout("Right selection"):
                curve.points[curve.points.right_handle_auto].offset = (0, 0, 0.5)
                curve.points[curve.points.right_handle_free].offset = (0, 0, 1.0)
                curve.points[curve.points.right_handle_vector].offset = (0, 0, 1.5)
                curve.points[curve.points.right_handle_align].offset = (0, 0, 2.0)

            with Layout("Moving handles"):
                curve.points[curve.points.left_handle_free].left_handle_position = (5, 0, 0)
                curve.points[curve.points.right_handle_free].right_handle_position = (-5, 0, 0)

                curve.points[curve.points.left_handle_vector].left_handle_offset = (0, 5, 0)
                curve.points[curve.points.right_handle_vector].right_handle_offset = (0, -5, 0)

            curve.out()
        ```

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - offset (Vector) : socket 'Offset' (Offset)
        - mode (str): Node.mode in ('LEFT', 'RIGHT')

        Returns
        -------
        - curve (Geometry)
        """

        self._geo._jump(Node('Set Handle Positions', {'Curve': self._geo, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode=mode)._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Handle position properties

    @property
    def left_handle_position(self):
        """ Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

        [!Node] Curve Handle Positions

        Returns
        -------
        - DataSocket 'Left'
        """

        return self.handle_positions(relative=False).left

    @left_handle_position.setter
    def left_handle_position(self, value):
        """ Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

        [!Node] Set Handle Positions

        Arguments
        ---------
        - value (Vector) : socket 'Position' (Position)
        """
        self.set_handle_positions(position=value, mode='LEFT')

    @property
    def right_handle_position(self):
        """ Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

        [!Node] Curve Handle Positions

        Returns
        -------
        - DataSocket 'Right'
        """
        return self.handle_positions(relative=False).right

    @right_handle_position.setter
    def right_handle_position(self, value):
        """ Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

        [!Node] Set Handle Positions

        Arguments
        ---------
        - value (Vector) : socket 'Position' (Position)
        """
        self.set_handle_positions(position=value, mode='RIGHT')

    # Offset

    @property
    def left_handle_offset(self):
        """ Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

        [!Node] Curve Handle Positions

        Returns
        -------
        - DataSocket 'Left'
        """
        return self.handle_positions(relative=True).left

    @left_handle_offset.setter
    def left_handle_offset(self, value):
        """ Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

        [!Node] Set Handle Positions

        Arguments
        ---------
        - value (Vector) : socket 'Position' (Position)
        """
        self.set_handle_positions(offset=value, mode='LEFT')

    @property
    def right_handle_offset(self):
        """ Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

        [!Node] Curve Handle Positions

        Returns
        -------
        - DataSocket 'Right'
        """
        return self.handle_positions(relative=True).right

    @right_handle_offset.setter
    def right_handle_offset(self, value):
        """ Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

        [!Node] Set Handle Positions

        Arguments
        ---------
        - value (Vector) : socket 'Position' (Position)
        """
        self.set_handle_positions(offset=value, mode='RIGHT')

    # ----- Handle type

    @classmethod
    def handle_type_selection(cls, left=True, right=True, handle_type='AUTO'):
        """ Node 'Handle Type Selection' (GeometryNodeCurveHandleTypeSelection)

        [!Node] Handle Type Selection

        Arguments
        ---------
        - left (bool = True) : left handle
        - right (bool = True) : right handle
        - handle_type (str): Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Boolean
        """

        mode = set()
        if left:
            mode.add('LEFT')
        if right:
            mode.add('RIGHT')
        return Node('Handle Type Selection', mode=mode, handle_type=handle_type)._out

    def set_handle_type(self, left=True, right=True, handle_type='AUTO'):
        """ Node 'Set Handle Type' (GeometryNodeCurveSetHandles)

        [!Node] Set Handle Type

        ``` python
        with GeoNodes("Curve handles"):
            curve = Curve.Line(0, (20, 0, 0)).resample(20)

            curve.splines.type = 'BEZIER'

            with Layout("Set by str"):
                curve.points.left_handle_type = 'AUTO'
                curve.points.right_handle_type = 'AUTO'
                curve.points[(nd.index % 2).equal(0)].handle_type = 'ALIGN'

                curve.points[curve.points.handle_align].offset = (0, 0, 2)

            with Layout("Both set boolean"):
                curve.points[1].handle_auto = True
                curve.points[3].handle_free = True
                curve.points[5].handle_vector = True
                curve.points[7].handle_align = True

            with Layout("Left / right set boolean"):
                curve.points[9].left_handle_auto = True
                curve.points[9].right_handle_free = True
                curve.points[11].left_handle_free = True
                curve.points[11].right_handle_vector = True
                curve.points[13].left_handle_vector = True
                curve.points[13].right_handle_align = True
                curve.points[15].left_handle_align = True
                curve.points[15].right_handle_auto = True

            with Layout("Left selection"):
                curve.points[curve.points.left_handle_auto].offset = (0, 0.5, 0)
                curve.points[curve.points.left_handle_free].offset = (0, 1.0, 0)
                curve.points[curve.points.left_handle_vector].offset = (0, 1.5, 0)
                curve.points[curve.points.left_handle_align].offset = (0, 2.0, 0)

            with Layout("Right selection"):
                curve.points[curve.points.right_handle_auto].offset = (0, 0, 0.5)
                curve.points[curve.points.right_handle_free].offset = (0, 0, 1.0)
                curve.points[curve.points.right_handle_vector].offset = (0, 0, 1.5)
                curve.points[curve.points.right_handle_align].offset = (0, 0, 2.0)

            with Layout("Moving handles"):
                curve.points[curve.points.left_handle_free].left_handle_position = (5, 0, 0)
                curve.points[curve.points.right_handle_free].right_handle_position = (-5, 0, 0)

                curve.points[curve.points.left_handle_vector].left_handle_offset = (0, 5, 0)
                curve.points[curve.points.right_handle_vector].right_handle_offset = (0, -5, 0)

            curve.out()
        ```

        Arguments
        ---------
        - left (bool = True) : left handle
        - right (bool = True) : right handle
        - handle_type (str): Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - curve (Geometry)
        """

        mode = set()
        if left:
            mode.add('LEFT')
        if right:
            mode.add('RIGHT')
        self._geo._jump(Node('Set Handle Type', {'Curve': self._geo, 'Selection': self._sel}, mode=mode, handle_type=handle_type)._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Handle types as enum in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

    # ----- Left and Right

    @property
    def handle_type(self):
        raise NodeError(f"Property 'handle_type' is write only")

    @handle_type.setter
    def handle_type(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=True, handle_type=value)

    # ----- Left only

    @property
    def left_handle_type(self):
        raise NodeError(f"Property 'left_handle_type' is write only")

    @left_handle_type.setter
    def left_handle_type(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=False, handle_type=value)

    # ----- Right only

    @property
    def right_handle_type(self):
        raise NodeError(f"Property 'right_handle_type' is write only")

    @right_handle_type.setter
    def right_handle_type(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=False, right=True, handle_type=value)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Left and Right Handle types as boolean properties

    @property
    def handle_auto(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=True, handle_type='AUTO')

    @handle_auto.setter
    def handle_auto(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=True, handle_type='AUTO')

    @property
    def handle_free(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=True, handle_type='FREE')

    @handle_free.setter
    def handle_free(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=True, handle_type='FREE')

    @property
    def handle_vector(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=True, handle_type='VECTOR')

    @handle_vector.setter
    def handle_vector(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=True, handle_type='VECTOR')

    @property
    def handle_align(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=True, handle_type='ALIGN')

    @handle_align.setter
    def handle_align(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=True, handle_type='ALIGN')

    # -----------------------------------------------------------------------------------------------------------------------------
    # Left Handle types as boolean properties

    @property
    def left_handle_auto(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=False, handle_type='AUTO')

    @left_handle_auto.setter
    def left_handle_auto(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=False, handle_type='AUTO')

    @property
    def left_handle_free(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=False, handle_type='FREE')

    @left_handle_free.setter
    def left_handle_free(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=False, handle_type='FREE')

    @property
    def left_handle_vector(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=False, handle_type='VECTOR')

    @left_handle_vector.setter
    def left_handle_vector(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=False, handle_type='VECTOR')

    @property
    def left_handle_align(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=True, right=False, handle_type='ALIGN')

    @left_handle_align.setter
    def left_handle_align(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=True, right=False, handle_type='ALIGN')

    # -----------------------------------------------------------------------------------------------------------------------------
    # Right Handle types as boolean properties

    @property
    def right_handle_auto(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=False, right=True, handle_type='AUTO')

    @right_handle_auto.setter
    def right_handle_auto(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=False, right=True, handle_type='AUTO')

    @property
    def right_handle_free(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=False, right=True, handle_type='FREE')

    @right_handle_free.setter
    def right_handle_free(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=False, right=True, handle_type='FREE')

    @property
    def right_handle_vector(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=False, right=True, handle_type='VECTOR')

    @right_handle_vector.setter
    def right_handle_vector(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=False, right=True, handle_type='VECTOR')

    @property
    def right_handle_align(self):
        """ [!Node] Handle Type Selection
        """
        return self.handle_type_selection(left=False, right=True, handle_type='ALIGN')

    @right_handle_align.setter
    def right_handle_align(self, value):
        """ [!Node] Set Handle Type
        """
        self.set_handle_type(left=False, right=True, handle_type='ALIGN')



class CloudPoint(Point):

    # ----- Radius

    @property
    def radius(self):
        """ Node 'Radius' (GeometryNodeInputRadius)

        [!Node] Radius

        Returns
        -------
        - Float
        """
        return Node('Radius')._out

    @radius.setter
    def radius(self, value):
        """ Node 'Set Point Radius' (GeometryNodeSetPointRadius)

        [!Node] Set Point Radius

        Arguments
        ---------
        - value (Float) : socket 'Radius' (Radius)
        """
        self._geo._jump(Node('Set Point Radius', {'Points': self._geo, 'Selection': self._sel, 'Radius': value})._out)




# =============================================================================================================================
# =============================================================================================================================
# Face Domain
# =============================================================================================================================
# =============================================================================================================================

class Face(Domain):
    DOMAIN_NAME = 'FACE'

    @property
    def count(self):
        """ Node 'Domain Size' (GeometryNodeAttributeDomainSize)

        [!Node] Domain Size

        Socket 'Face Count' of node 'Domain Size'

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.face_count

    # =============================================================================================================================
    # Properties

    # ----- Smooth

    @property
    def smooth(self):
        """ Node 'Is Face Smooth' (GeometryNodeInputShadeSmooth)

        [!Node] Is Face Smooth

        Returns
        -------
        - Boolean
        """
        return Node('Is Face Smooth')._out

    @smooth.setter
    def smooth(self, value):
        """ Node 'Set Shade Smooth' (GeometryNodeSetShadeSmooth)

        [!Node] Set Shade Smooth

        - domain (str): Node.domain in ('EDGE', 'FACE')

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (Shade Smooth)
        """
        self._geo._jump(Node('Set Shade Smooth', {'Geometry': self._geo, 'Selection': self._sel, 'Shade Smooth': value}, domain='FACE')._out)

    @property
    def area(self):
        """ Node 'Face Area' (GeometryNodeInputMeshFaceArea)

        [!Node] Face Area

        Returns
        -------
        - Float
        """
        return Node('Face Area')._out

    def is_planar(self, threshold=None):
        """ Node 'Is Face Planar' (GeometryNodeInputMeshFaceIsPlanar)

        [!Node] Is Face Planar

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (Threshold)

        Returns
        -------
        - Boolean
        """
        return Node('Is Face Planar', {'Threshold': threshold})._out

    def group_boundaries(self, face_group_id=None):
        """ Node 'Face Group Boundaries' (GeometryNodeMeshFaceSetBoundaries)

        [!Node] Face Group Boundaries

        Arguments
        ---------
        - face_group_id (Integer) : socket 'Face Group ID' (Face Set)

        Returns
        -------
        - Boolean
        """
        return Node('Face Group Boundaries', {'Face Group ID': face_group_id})._out

    @property
    def neighbors(self):
        """ Node 'Face Neighbors' (GeometryNodeInputMeshFaceNeighbors)

        [!Node] Face Neighbors

        Returns
        -------
        - Node: [vertex_count (Integer), face_count (Integer)]
        """
        return self._cache('Face Neighbors')

    @property
    def neighbors_vertex_count(self):
        """ Node 'Face Neighbors' (GeometryNodeInputMeshVertexNeighbors)

        [!Node] Face Neighbors

        Returns
        -------
        - Integer : Socket 'Vertex Count' of node 'Vertex Neighbors'
        """
        return self.neighbors.vertex_count

    @property
    def neighbors_face_count(self):
        """ Node 'Face Neighbors' (GeometryNodeInputMeshVertexNeighbors)

        [!Node] Face Neighbors

        Returns
        -------
        - Integer : Socket 'Face Count' of node 'Vertex Neighbors'
        """
        return self.neighbors.face_count

    # ----- Flip

    def flip(self):
        """ Node 'Flip Faces' (GeometryNodeFlipFaces)

        [!Node] Flip Faces

        Returns
        -------
        - Mesh
        """
        return Node('Flip Faces', {'Mesh': self._geo, 'Selection': self._sel})._out

    # ----- Scale

    def scale(self, scale=None, center=None, uniform=True):
        """ Node 'Scale Elements' (GeometryNodeScaleElements)

        [!Node] Scale Elements

        - domain (str): Node.domain in ('FACE', 'EDGE')
        - scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - unifom (bool=True) : scale_mode = 'UNIFORM' (True) or 'SINGLE_AXIS' (False)

        Returns
        -------
        - Mesh
        """
        return self._geo._jump(Node('Scale Elements', {'Geometry': self._geo, 'Selection': self._sel, 'Scale': scale, 'Center': center},
            domain='FACE', scale_mode = 'UNIFORM' if uniform else 'SINGLE_AXIS')._out)

    # ----- Topology

    @classmethod
    def corner_index(cls, face_index=None, weights=None, sort_index=None):
        """ Node 'Corners of Face' (GeometryNodeCornersOfFace)

        [!Node] Corners of Face

        Arguments
        ---------
        - face_index (Integer) : socket 'Face Index' (Face Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer [total_]
        """
        index = Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

    # ----- Distribute

    def distribute_points(self, density=None, distance_min=None, density_max=None, density_factor=None, seed=None):
        """ Node 'Distribute Points on Faces' (GeometryNodeDistributePointsOnFaces)

        [!Node] Distribute Points on Faces

        if 'density' argument is not None, 'RANDOM' method is applied, 'POISSON' otherwise

        - distribute_method (str): Node.distribute_method in ('RANDOM', 'POISSON')
        - use_legacy_normal (bool): Node.use_legacy_normal

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)n 'RANDOM' method if not None 'POISSON' otherwise
        - distance_min (Float) : socket 'Distance Min'
        - density_max (Float) : socket 'Density Max'
        - density_factor (Float) : socket 'Density Factor'
        - seed (Integer) : socket 'Seed' (Seed)

        Returns
        -------
        - Points [normal_, rotation_
        """
        return self._geo[self._sel].distribute_points_on_faces(density=density, distance_min=distance_min, density_max=density_max,
            density_factor=density_factor, seed=seed)




# =============================================================================================================================
# =============================================================================================================================
# Edge Domain
# =============================================================================================================================
# =============================================================================================================================

class Edge(Domain):
    DOMAIN_NAME = 'EDGE'

    @property
    def count(self):
        """ Node 'Domain Size' (GeometryNodeAttributeDomainSize)

        [!Node] Domain Size

        Socket 'Edge Count' of node 'Domain Size'

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.edge_count

    # =============================================================================================================================
    # Properties

    # ----- Angle

    @property
    def angle(self):
        """ Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

        [!Node] Edge Angle

        Returns
        -------
        - Node: [unsigned_angle (Float), signed_angle (Float)]
        """
        return self._cache('Edge Angle')

    @property
    def unsigned_angle(self):
        """ Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

        [!Node] Edge Angle

        Returns
        -------
        - Float : socket 'Unsigned Angle'
        """
        return self.angle.unsigned_angle

    @property
    def signed_angle(self):
        """ Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

        [!Node] Edge Angle

        Returns
        -------
        - Float : socket 'Signed Angle'
        """
        return self.angle.signed_angle

    # ----- Neighbors

    @property
    def neighbors(self):
        """ Node 'Edge Neighbors' (GeometryNodeInputMeshEdgeNeighbors)

        [!Node] Edge Neighbors

        Returns
        -------
        - Integer
        """
        return Node('Edge Neighbors')._out

    # ----- Edge vertices

    @property
    def vertices(self):
        """ Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

        [!Node] Edge Vertices

        Returns
        -------
        - Node: [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """
        return self._cache('Edge Vertices')

    @property
    def vertex_index_1(self):
        """ Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

        [!Node] Edge Vertices

        Returns
        -------
        - Integer : socket 'Vertex Index 1'
        """
        return self.vertices.vertex_index_1

    @property
    def vertex_index_2(self):
        """ Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

        [!Node] Edge Vertices

        Returns
        -------
        - Integer : socket 'Vertex Index 2'
        """
        return self.vertices.vertex_index_2

    @property
    def position_1(self):
        """ Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

        [!Node] Edge Vertices

        Returns
        -------
        - Vector : socket 'Vertices Index 1'
        """
        return self.vertices.position_1

    @property
    def position_2(self):
        """ Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

        [!Node] Edge Vertices

        Returns
        -------
        - Vector : socket 'Vertices Index 1'
        """
        return self.vertices.position_2

    # ----- Smooth

    @property
    def smooth(self):
        """ Node 'Is Edge Smooth' (GeometryNodeInputEdgeSmooth)

        [!Node] Is Edge Smooth

        Returns
        -------
        - Boolean
        """
        return Node('Is Edge Smooth')._out

    @smooth.setter
    def smooth(self, value):
        """ Node 'Set Shade Smooth' (GeometryNodeSetShadeSmooth)

        [!Node] Set Shade Smooth

        - domain (str): Node.domain in ('EDGE', 'FACE')

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (Shade Smooth)
        """
        self._geo._jump(Node('Set Shade Smooth', {'Geometry': self._geo, 'Selection': self._sel, 'Shade Smooth': value}, domain='EDGE')._out)

    # ----- Shortest Edge Paths

    def shortest_paths(self, edge_cost=None):
        """ Node 'Shortest Edge Paths' (GeometryNodeInputShortestEdgePaths)

        [!Node] Shortest Edge Paths

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (Edge Cost)

        Returns
        -------
        - Integer [total_cost_]
        """

        index = Node('Shortest Edge Paths', {'End Vertex': self._sel, 'Edge Cost': edge_cost}).next_vertex_index
        index.total_cost_ = index.node.total_cost
        return index

    # ----- To face groups

    @property
    def to_face_groups(self):
        """ Node 'Edges to Face Groups' (GeometryNodeEdgesToFaceGroups)

        [!Node] Edges to Face Groups

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (Boundary Edges)

        Returns
        -------
        - Integer
        """
        return Node('Edges to Face Groups', {'Boundary Edges': self._sel})._out

    # ----- Split

    def split(self):
        """ Node 'Split Edges' (GeometryNodeSplitEdges)

        [!Node] Split Edges

        Returns
        -------
        - Mesh
        """
        return Node('Split Edges', {'Mesh': self._geo, 'Selection': self._sel})._out

    # ----- Scale

    def scale(self, scale=None, center=None, uniform=True):
        """ Node 'Scale Elements' (GeometryNodeScaleElements)

        [!Node] Scale Elements

        - domain (str): Node.domain in ('FACE', 'EDGE')
        - scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - unifom (bool=True) : scale_mode = 'UNIFORM' (True) or 'SINGLE_AXIS' (False)

        Returns
        -------
        - Mesh
        """
        return self._geo._jump(Node('Scale Elements', {'Geometry': self._geo, 'Selection': self._sel, 'Scale': scale, 'Center': center},
            domain='EDGE', scale_mode = 'UNIFORM' if uniform else 'SINGLE_AXIS')._out)

    # ----- Topology

    @classmethod
    def corner_index(cls, edge_index=None, weights=None, sort_index=None):
        """ Node 'Corners of Edge' (GeometryNodeCornersOfEdge)

        [!Node] Corners of Edge

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (Edge Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer [total_]
        """
        index = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

    # ----- Edge paths to curves

    def paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """ Node 'Edge Paths to Curves' (GeometryNodeEdgePathsToCurves)

        [!Node] Edge Paths to Curves

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (Next Vertex Index)

        Returns
        -------
        - Curve
        """

        return Curve(Node('Edge Paths to Curves', {'Mesh': self._geo, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})._out)


# =============================================================================================================================
# =============================================================================================================================
# Corner Domain
# =============================================================================================================================
# =============================================================================================================================

class Corner(Domain):
    DOMAIN_NAME = 'CORNER'

    @property
    def count(self):
        """ Node 'Domain Size' (GeometryNodeAttributeDomainSize)

        [!Node] Domain Size

        Socket 'Corner Count' of node 'Domain Size'

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.face_corner_count

    # ----- Topology

    @classmethod
    def next_edge_index(cls, corner_index=None):
        """ Node 'Edges of Corner' (GeometryNodeEdgesOfCorner)

        [!Node] Edges of Corner

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Integer [previous_edge_index_]
        """

        index = Node('Edges of Corner', {'Corner Index': corner_index})._out
        index.previous_edge_index_ = index.node.previous_edge_index
        return index

    @classmethod
    def face_index(cls, corner_index=None):
        """ Node 'Face of Corner' (GeometryNodeFaceOfCorner)

        [!Node] Face of Corner

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Integer [index_in_face_]
        """
        index = Node('Face of Corner', {'Corner Index': corner_index})._out
        index.index_in_face_ = index.node.index_in_face
        return index

    @classmethod
    def offset_in_face(cls, corner_index=None, offset=None):
        """ Node 'Offset Corner in Face' (GeometryNodeOffsetCornerInFace)

        [!Node] Offset Corner in Face

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)
        - offset (Integer) : socket 'Offset' (Offset)

        Returns
        -------
        - Integer
        """
        return Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})._out

    @classmethod
    def vertex_index(cls, corner_index=None):
        """ Node 'Vertex of Corner' (GeometryNodeVertexOfCorner)

        [!Node] Vertex of Corner

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Integer
        """
        return Node('Vertex of Corner', {'Corner Index': corner_index})._out




# =============================================================================================================================
# =============================================================================================================================
# Spline Domain
# =============================================================================================================================
# =============================================================================================================================

class Spline(Domain):

    DOMAIN_NAME = 'CURVE'

    @property
    def count(self):
        """ Node 'Domain Size' (GeometryNodeAttributeDomainSize)

        [!Node] Domain Size

        Socket 'Spline Count' of node 'Domain Size'

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.spline_count

    # ====================================================================================================
    # Properties

    # ----- Cyclic

    @property
    def is_cyclic(self):
        """ Node 'Is Spline Cyclic' (GeometryNodeInputSplineCyclic)

        [!Node] Is Spline Cyclic

        Returns
        -------
        - Boolean
        """
        return Node('Is Spline Cyclic')._out

    @is_cyclic.setter
    def is_cyclic(self, value):
        """ Node 'Set Spline Cyclic' (GeometryNodeSetSplineCyclic)

        [!Node] Set Spline Cyclic

        Arguments
        ---------
        - value (Boolean) : socket 'Cyclic' (Cyclic)
        """
        return self._geo._jump(Node('Set Spline Cyclic', {'Geometry': self._geo, 'Selection': self._sel, 'Cyclic': value})._out)

    # ----- Resolution

    @property
    def resolution(self):
        """ Node 'Spline Resolution' (GeometryNodeInputSplineResolution)

        [!Node] Spline Resolution

        Returns
        -------
        - Integer
        """
        return Node('Spline Resolution')._out

    @resolution.setter
    def resolution(self, value=None):
        """ Node 'Set Spline Resolution' (GeometryNodeSetSplineResolution)

        [!Node] Set Spline Resolution

        Arguments
        ---------
        - value (Integer) : socket 'Resolution' (Resolution)
        """
        self._geo._jump(Node('Set Spline Resolution', {'Geometry': self._geo, 'Resolution': value})._out)

    # ----- Spline type

    @property
    def type(self):
        raise NodeError(f"Curve.spline_type is write only.")

    @type.setter
    def type(self, value):
        """ Node 'Set Spline Type' (GeometryNodeCurveSplineType)

        [!Node] Set Spline Type

        Arguments
        ---------
        - value (str): Node.spline_type in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')
        """
        self._geo._jump(Node('Set Spline Type', {'Curve': self._geo, 'Selection': self._sel}, spline_type=value)._out)

    # ----- Read only

    @property
    def parameter(self):
        """ Node 'Spline Parameter' (GeometryNodeSplineParameter)

        [!Node] Spline Parameter

        Returns
        -------
        - Node: [factor (Float), length (Float), index (Integer)]
        """
        return self._cache('Spline Parameter')

    @classmethod
    @property
    def length(cls):
        """ Node 'Spline Length' (GeometryNodeSplineLength)

        [!Node] Spline Length

        Returns
        -------
        - Integer [point_count_]
        """
        length = Node('Spline Length')._out
        length.point_count_ = length.node.point_count
        return length

    @classmethod
    @property
    def point_count(cls):
        """ Node 'Spline Length' (GeometryNodeSplineLength)

        [!Node] Spline Length

        Returns
        -------
        - Integer [length_]
        """
        node = Node('Spline Length')
        point_count = node.point_count
        point_count.length_ = node.length
        return point_count


# =============================================================================================================================
# =============================================================================================================================
# Instance Domain
# =============================================================================================================================
# =============================================================================================================================

class Instance(Domain):
    DOMAIN_NAME = 'INSTANCE'

    @property
    def count(self):
        return self._geo.domain_size.instance_count

    # ====================================================================================================
    # Properties

    # ----- Transform

    @property
    def transform(self):
        """ Node 'Instance Transform' (GeometryNodeInstanceTransform)

        [!Node] Instance Transform

        Returns
        -------
        - Matrix
        """
        return Node('Instance Transform')._out

    @transform.setter
    def transform(self, value):
        """ Node 'Set Instance Transform' (GeometryNodeSetInstanceTransform)

        [!Node] Set Instance Transform

        Arguments
        ---------
        - value (Matrix) : socket 'Transform' (Transform)
        """
        return self._geo._jump(Node('Set Instance Transform', {'Instances': self._geo, 'Selection': self._sel, 'Transform': value})._out)

    # ----- Translate

    def translate(self, translation=None, local_space=None):
        """ Node 'Translate Instances' (GeometryNodeTranslateInstances)

        [!Node] Translate Instances

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - self
        """
        return self._geo._jump(Node('Translate Instances', {'Instances': self._geo, 'Selection': self._sel, 'Translation': translation, 'Local Space': local_space})._out)

    # ----- Scale

    @property
    def scale(self):
        """ Node 'Instance Scale' (GeometryNodeInputInstanceScale)

        [!Node] Instance Scale

        Returns
        -------
        - Vector
        """
        return Node('Instance Scale')._out

    @scale.setter
    def scale(self, value):
        """ Node 'Scale Instances' (GeometryNodeScaleInstances)

        [!Node] Scale Instances

        scale can be set either by a Vector argument or by a dict with keys in ('Scale', 'Center', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.scale = (1, 2, 3)
        instances.insts.scale = {'Scale': (1, 2, 3), 'Center': (10, 11, 12), 'Local Space': True}
        ```

        Arguments
        ---------
        - value (Vector or dict) : socket 'Scale' (Scale)

        Returns
        -------
        - instances (Geometry)
        """
        keys = ['Scale', 'Center', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys is None:
                    raise NodeError(f"Node 'Scale Instances' error: invalid key '{k}' to set instance scale.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Scale'] = value

        return self._geo._jump(Node('Scale Instances', sockets)._out)

    # ----- Rotation

    @property
    def rotation(self):
        """ Node 'Instance Rotation' (GeometryNodeInputInstanceRotation)

        [!Node] Instance Rotation

        Returns
        -------
        - Rotation
        """
        return Node('Instance Rotation')._out

    @rotation.setter
    def rotation(self, value):
        keys = ['Rotation', 'Pivot Point', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys:
                    raise NodeError(f"Node 'Rotate Instances' error: invalid key '{k}' to set instance rotation.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Rotation'] = value

        return self._geo._jump(Node('Rotate Instances', sockets)._out)



# =============================================================================================================================
# =============================================================================================================================
# Mesh
# =============================================================================================================================
# =============================================================================================================================

class Mesh(Geometry):

    def _reset(self):

        super()._reset()

        self.points  = Vertex(self)
        self.edges   = Edge(self)
        self.faces   = Face(self)
        self.corners = Corner(self)

    # =============================================================================================================================
    # Constructors

    @classmethod
    def FromCurve(cls, curve=None, profile_curve=None, fill_caps=None):
        """ Constructor Node 'Curve to Mesh' (GeometryNodeCurveToMesh)

        [!Node] Curve to Mesh

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - profile_curve (Geometry) : socket 'Profile Curve' (Profile Curve)
        - fill_caps (Boolean) : socket 'Fill Caps' (Fill Caps)

        Returns
        -------
        - Mesh
        """
        return cls(Node('Curve to Mesh', {'Curve': curve, 'Profile Curve': profile_curve, 'Fill Caps': fill_caps})._out)

    @classmethod
    def FromPoints(cls, points):
        """ Constructor Node 'Points to Vertices' (GeometryNodePointsToVertices)

        [!Node] Points to Vertices

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)

        Returns
        -------
        - Mesh
        """
        return Cloud(points)[points._sel].to_vertices()

    @classmethod
    def FromVolume(cls, volume, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ Constructor Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

        [!Node] Volume to Mesh

        Arguments
        ---------
        - volume (Geometry) : socket 'Volume' (Volume)
        - voxel_size (Float) : socket 'Voxel Size'
        - voxel_amount (Float) : socket 'Voxel Amount'
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)
        - resolution_mode (str): Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Mesh
        """
        return Volume(volume).to_mesh(voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode)

    # =============================================================================================================================
    # Properties

    @property
    def island(self):
        """ Node 'Mesh Island' (GeometryNodeInputMeshIsland)

        [!Node] Mesh Island

        Returns
        -------
        - Node: [island_index (Integer), island_count (Integer)]
        """
        return self._cache('Mesh Island')

    @property
    def island_index(self):
        """ Node 'Mesh Island' (GeometryNodeInputMeshIsland)

        [!Node] Mesh Island

        Returns
        -------
        - Integer : socket 'Island Index'
        """
        return self.island.island_index

    @property
    def island_count(self):
        """ Node 'Mesh Island' (GeometryNodeInputMeshIsland)

        [!Node] Mesh Island

        Returns
        -------
        - Integer : socket 'Island Count'
        """
        return self.island.island_count

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='MESH')

    @classmethod
    def Cube(self, size=(1, 1, 1), vertices_x=2, vertices_y=2, vertices_z=2):
        """ Constructor Node 'Cube' (GeometryNodeMeshCube)

        [!Node] Cube

        Arguments
        ---------
        - size (Vector) : socket 'Size' (Size)
        - vertices_x (Integer) : socket 'Vertices X' (Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (Vertices Y)
        - vertices_z (Integer) : socket 'Vertices Z' (Vertices Z)

        Returns
        -------
        - Mesh [uv_map_]
        """
        node = Node('Cube', {'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, end_location=None, resolution=None):
        """ Constructor Node 'Mesh Line' (GeometryNodeMeshLine)

        [!Node] Mesh Line

        - count_mode (str): Node.count_mode in ('TOTAL', 'RESOLUTION')
        - mode (str): Node.mode in ('OFFSET', 'END_POINTS')

        If end_location is not None or resolution is not None, mode is set to 'END_POINTS',
        otherwise it iset to 'OFFSET'.
        If resolution is None, count_mode is set to 'TOTAL' else to 'RESOLUTION'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (Count)
        - start_location (Vector) : socket 'Start Location' (Start Location)
        - end_location (Vector) : socket 'End Location' (End Location)
        - offset (Vector) : socket 'Offset' (Offset)
        - resolution (Float) : socket 'Resolution' (Resolution)

        Returns
        -------
        - Mesh
        """
        if end_location is not None or resolution is not None:
            count_mode = 'TOTAL' if resolution is None else 'RESOLUTION'
            return Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': end_location},
                mode='END_POINTS', count_mode=count_mode)._out
        else:
            return Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': offset},
                mode='OFFSET')._out

    @classmethod
    def LineTo(cls, start_location=None, end_location=None, count=None, resolution=None):
        """ Constructor Node 'Mesh Line' (GeometryNodeMeshLine)

        [!Node] Mesh Line

        Line from start to end point

        Arguments
        ---------
        - start_location (Vector) : socket 'Start Location' (Start Location)
        - end_location (Vector) : socket 'End Location' (End Location)
        - count (Integer) : socket 'Count' (Count)
        - resolution (Float) : socket 'Resolution' (Resolution)

        Returns
        -------
        - Mesh
        """
        return cls.Line(count=count, start_location=start_location, end_location=end_location, resolution=resolution)

    @classmethod
    def LineOffset(cls, start_location=None, offset=None, count=None):
        """ Constructor Node 'Mesh Line' (GeometryNodeMeshLine)

        [!Node] Mesh Line

        Line from start to end point

        Arguments
        ---------
        - start_location (Vector) : socket 'Start Location' (Start Location)
        - offset (Vector) : socket 'Offset' (Offset)
        - count (Integer) : socket 'Count' (Count)

        Returns
        -------
        - Mesh
        """
        return cls.Line(count=count, start_location=start_location, offset=offset)

    @classmethod
    def Cone(cls, vertices=32, side_segments=1, fill_segments=1, radius_top=0.0, radius_bottom=1.0, depth=2.0, fill_type='NGON'):
        """ Constructor Node 'Cone' (GeometryNodeMeshCone)

        [!Node] Cone

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - side_segments (Integer) : socket 'Side Segments' (Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (Fill Segments)
        - radius_top (Float) : socket 'Radius Top' (Radius Top)
        - radius_bottom (Float) : socket 'Radius Bottom' (Radius Bottom)
        - depth (Float) : socket 'Depth' (Depth)
        - fill_type (str): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Mesh [top_, bottom_, side_, uv_map_]
        """

        node = Node('Cone', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments,
            'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        mesh = Mesh(node.mesh)
        mesh.top_ = node.top
        mesh.bottom_ = node.bottom
        mesh.side_ = node.side
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def Cylinder(cls, vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0, fill_type='NGON'):
        """ Constructor Node 'Cylinder' (GeometryNodeMeshCylinder)

        [!Node] Cylinder

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - side_segments (Integer) : socket 'Side Segments' (Side Segments)
        - fill_segments (Integer) : socket 'Fill Segments' (Fill Segments)
        - radius (Float) : socket 'Radius' (Radius)
        - depth (Float) : socket 'Depth' (Depth)
        - fill_type (str): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Mesh [top_, side_, bottom_, uv_map_]
        """
        node = Node('Cylinder', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments,
            'Radius': radius, 'Depth': depth}, fill_type=fill_type)
        mesh = Mesh(node.mesh)
        mesh.top_ = node.top
        mesh.bottom_ = node.bottom
        mesh.side_ = node.side
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def Circle(cls, vertices=32, radius=1.0, fill_type='NONE'):
        """ Constructor Node 'Mesh Circle' (GeometryNodeMeshCircle)

        [!Node] Mesh Circle

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - radius (Float) : socket 'Radius' (Radius)
        - fill_type (str = 'NONE'): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Mesh
        """
        node = Node('Mesh Circle', {'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        mesh = Mesh(node.mesh)
        return mesh

    @classmethod
    def Disk(cls, vertices=32, radius=1.0, fill_type='NGON'):
        """ Constructor Node 'Mesh Circle' (GeometryNodeMeshCircle)

        [!Node] Mesh Circle

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - radius (Float) : socket 'Radius' (Radius)
        - fill_type (str = 'NGON'): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Mesh
        """
        return cls.Circle(vertices=vertices, radius=radius, fill_type=fill_type)

    @classmethod
    def Grid(cls, size_x=1.0, size_y=1.0, vertices_x=3, vertices_y=3):
        """ Constructor Node 'Grid' (GeometryNodeMeshGrid)

        [!Node] Grid

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (Size X)
        - size_y (Float) : socket 'Size Y' (Size Y)
        - vertices_x (Integer) : socket 'Vertices X' (Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (Vertices Y)

        Returns
        -------
        - Mesh [uv_map_]
        """
        node = Node('Grid', {'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def Plane(cls, size_x=1.0, size_y=1.0):
        """ Constructor Node 'Grid' (GeometryNodeMeshGrid)

        [!Node] Grid

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (Size X)
        - size_y (Float) : socket 'Size Y' (Size Y)

        Returns
        -------
        - Mesh [uv_map_]
        """
        return cls.Grid(size_x=size_x, size_y=size_y, vertices_x=2, vertices_y=2)


    @classmethod
    def IcoSphere(cls, radius=1.0, subdivisions=1):
        """ Constructor Node 'Ico Sphere' (GeometryNodeMeshIcoSphere)

        [!Node] Ico Sphere

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (Radius)
        - subdivisions (Integer) : socket 'Subdivisions' (Subdivisions)

        Returns
        -------
        - Mesh [uv_map_]
        """
        node = Node('Ico Sphere', {'Radius': radius, 'Subdivisions': subdivisions})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def UVSphere(cls, segments=32, rings=16, radius=1.0):
        """ Node 'UV Sphere' (GeometryNodeMeshUVSphere)

        [!Node] UV Sphere

        Arguments
        ---------
        - segments (Integer) : socket 'Segments' (Segments)
        - rings (Integer) : socket 'Rings' (Rings)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Mesh [uv_map_]
        """
        node = Node('UV Sphere', {'Segments': segments, 'Rings': rings, 'Radius': radius})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    # =============================================================================================================================
    # Sample

    def sample_nearest_surface(self, value=None, group_id=None, sample_position=None, sample_group_id=None):
        """ Node 'Sample Nearest Surface' (GeometryNodeSampleNearestSurface)

        [!Node] Sample Nearest Surface

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sample_position (Vector) : socket 'Sample Position' (Sample Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (Sample Group ID)

        Returns
        -------
        - Float [is_valid_]
        """
        data_type = utils.get_data_type(value)
        res = Node('Sample Nearest Surface', {'Mesh': self, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)._out
        res.is_valid_ = res.node.is_valid
        return res

    def sample_uv_surface(self, value=None, uv_map=None, sample_uv=None):
        """ Node 'Sample UV Surface' (GeometryNodeSampleUVSurface)

        [!Node] Sample UV Surface

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - uv_map (Vector) : socket 'UV Map' (Source UV Map)
        - sample_uv (Vector) : socket 'Sample UV' (Sample UV)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Returns
        -------
        - Float [is_valid_]
        """
        data_type = utils.get_data_type(value)
        res = Node('Sample UV Surface', {'Mesh': self, 'Value': value, 'UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)._out
        res.is_valid_ = res.node.is_valid
        return res

    # =============================================================================================================================
    # Conversion

    def to_curve(self):
        """ Node 'Mesh to Curve' (GeometryNodeMeshToCurve)

        [!Node] Mesh to Curve

        Returns
        -------
        - Curve
        """
        return Curve(Node('Mesh to Curve', {'Mesh': self, 'Selection': self._sel})._out)

    def to_volume(self, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True):
        """ Node 'Mesh to Volume' (GeometryNodeMeshToVolume)

        [!Node] Mesh to Volume

        - resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (Voxel Amount)
        - interior_band_width (Float) : socket 'Interior Band Width' (Interior Band Width)
        - voxel_size (Float) : socket 'Voxel Size'
        - amount (bool = True) : resolution_mode is set to 'VOXEL_AMOUNT' (True) or 'VOXEL_SIZE' (False)

        Returns
        -------
        - Volume
        """
        if amount:
            return Volume(Node('Mesh to Volume', {'Mesh': self, 'Density': density, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width}, resolution_mode='VOXEL_AMOUNT')._out)
        else:
            return Volume(Node('Mesh to Volume', {'Mesh': self, 'Density': density, 'Voxel Size': voxel_size, 'Interior Band Width': interior_band_width}, resolution_mode='VOXEL_SIZE')._out)

    # =============================================================================================================================
    # Operations

    def dual(self, keep_boundaries=None):
        """ Node 'Dual Mesh' (GeometryNodeDualMesh)

        [!Node] Dual Mesh

        Arguments
        ---------
        - keep_boundaries (Boolean) : socket 'Keep Boundaries' (Keep Boundaries)

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Dual Mesh', {'Mesh': self, 'Keep Boundaries': keep_boundaries})._out)

    def subdivide(self, level=None):
        """ Node 'Subdivide Mesh' (GeometryNodeSubdivideMesh)

        [!Node] Subdivide Mesh

        Arguments
        ---------
        - level (Integer) : socket 'Level' (Level)

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Subdivide Mesh', {'Mesh': self, 'Level': level})._out)

    def triangulate(self, minimum_vertices=None, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY'):
        """ Node 'Triangulate' (GeometryNodeTriangulate)

        [!Node] Triangulate


        Arguments
        ---------
        - minimum_vertices (Integer) : socket 'Minimum Vertices' (Minimum Vertices)
        - ngon_method (str): Node.ngon_method in ('BEAUTY', 'CLIP')
        - quad_method (str): Node.quad_method in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Triangulate', {'Mesh': self, 'Selection': self._sel, 'Minimum Vertices': minimum_vertices},
            quad_method=quad_method, ngon_method=ngon_method)._out)

    def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL'):
        """ Node 'Subdivision Surface' (GeometryNodeSubdivisionSurface)

        [!Node] Subdivision Surface

        Arguments
        ---------
        - level (Integer) : socket 'Level' (Level)
        - edge_crease (Float) : socket 'Edge Crease' (Edge Crease)
        - vertex_crease (Float) : socket 'Vertex Crease' (Vertex Crease)
        - boundary_smooth (str): Node.boundary_smooth in ('PRESERVE_CORNERS', 'ALL')
        - uv_smooth (str): Node.uv_smooth in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Subdivision Surface', {'Mesh': self, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease},
            uv_smooth=uv_smooth, boundary_smooth=boundary_smooth)._out)

    #def smooth_by_angle(self, angle=None, ignore_sharpness=None):
    #    return Mesh(Node('Smooth by Angle', {'Mesh': self, 'Angle': angle, 'Ignore Sharpness': ignore_sharpness})._out)

    # ----- Mesh Boolean

    def boolean(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT', operation='DIFFERENCE'):
        """ Node 'Mesh Boolean' (GeometryNodeMeshBoolean)

        [!Node] Mesh Boolean

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - operation (str): Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh [intersecting_edges_]
        """
        if operation == 'DIFFERENCE':
            sockets = {'Mesh 1': self, 'Mesh 2': list(meshes)}
        else:
            sockets = {'Mesh 2': [self] + list(meshes)}
        sockets = {**sockets, 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}
        return Mesh(Node('Mesh Boolean', sockets, solver=solver, operation=operation)._out)

    def difference(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ Node 'Mesh Boolean' (GeometryNodeMeshBoolean)

        [!Node] Mesh Boolean

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh [intersecting_edges_]
        """
        return self.boolean(*meshes, self_intersection=self_intersection, hole_tolerant=hole_tolerant, solver=solver, operation='DIFFERENCE')

    def intersect(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ Node 'Mesh Boolean' (GeometryNodeMeshBoolean)

        [!Node] Mesh Boolean

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh [intersecting_edges_]
        """
        return self.boolean(*meshes, self_intersection=self_intersection, hole_tolerant=hole_tolerant, solver=solver, operation='INTERSECT')

    def union(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ Node 'Mesh Boolean' (GeometryNodeMeshBoolean)

        [!Node] Mesh Boolean

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh [intersecting_edges_]
        """
        return self.boolean(*meshes, self_intersection=self_intersection, hole_tolerant=hole_tolerant, solver=solver, operation='UNION')


    # ----- UV

    def pack_uv_islands(self, uv=None, margin=None, rotate=None):
        """ Node 'Pack UV Islands' (GeometryNodeUVPackIslands)

        [!Node] Pack UV Islands

        Arguments
        ---------
        - uv (Vector) : socket 'UV' (UV)
        - margin (Float) : socket 'Margin' (Margin)
        - rotate (Boolean) : socket 'Rotate' (Rotate)

        Returns
        -------
        - Vector
        """
        return Node('Pack UV Islands', {'UV': uv, 'Selection': self._sel, 'Margin': margin, 'Rotate': rotate})._out

    def uv_unwrap(self, seam=None, margin=None, fill_holes=False, method='ANGLE_BASED'):
        """ Node 'UV Unwrap' (GeometryNodeUVUnwrap)

        [!Node] UV Unwrap

        Arguments
        ---------
        - seam (Boolean) : socket 'Seam' (Seam)
        - margin (Float) : socket 'Margin' (Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (Fill Holes)
        - method (str): Node.method in ('ANGLE_BASED', 'CONFORMAL')

        Returns
        -------
        - uv (Vector)
        """
        return Node('UV Unwrap', {'Selection': self._sel, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)._out

    # ----- Distribute points

    def distribute_points_on_faces(self, density=None, distance_min=None, density_max=None, density_factor=None, seed=None):#, poisson=False):
        """ Node 'Distribute Points on Faces' (GeometryNodeDistributePointsOnFaces)

        [!Node] Distribute Points on Faces

        if 'density' argument is not None, 'RANDOM' method is applied, 'POISSON' otherwise

        - distribute_method (str): Node.distribute_method in ('RANDOM', 'POISSON')
        - use_legacy_normal (bool): Node.use_legacy_normal

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)n 'RANDOM' method if not None 'POISSON' otherwise
        - distance_min (Float) : socket 'Distance Min'
        - density_max (Float) : socket 'Density Max'
        - density_factor (Float) : socket 'Density Factor'
        - seed (Integer) : socket 'Seed' (Seed)

        Returns
        -------
        - Points [normal_, rotation_
        """

        # Poisson
        if density is None:
            node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self._sel,
                'Distance Min': distance_min, 'Density Max': density_max,
                'Density Factor': density_factor, 'Seed': seed}, distribute_method = 'POISSON')

        # Random
        else:
            node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self._sel,
                'Density': density, 'Seed': seed}, distribute_method = 'RANDOM')

        points = Cloud(node._out)
        points.normal_   = node.normal
        points.rotation_ = node.rotation
        return points


# =============================================================================================================================
# =============================================================================================================================
# Curve
# =============================================================================================================================
# =============================================================================================================================

class Curve(Geometry):

    def _reset(self):

        super()._reset()

        self.points  = SplinePoint(self)
        self.splines = Spline(self)

    # =============================================================================================================================
    # Constructors

    # ----- Circle

    @classmethod
    def Circle(cls, resolution=None, radius=None, point_1=None, point_2=None, point_3=None):
        """ Node 'Curve Circle' (GeometryNodeCurvePrimitiveCircle)

        [!Node] Curve Circle

        'mode' is set to 'POINTS' if one in (point_1, point_2, point_) is not None, 'RADIUS' otherwise

        - mode (str): Node.mode in ('POINTS', 'RADIUS')

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - radius (Float) : socket 'Radius' (Radius)
        - point_1 (Vector) : socket 'Point 1' (Point 1)
        - point_2 (Vector) : socket 'Point 2' (Point 2)
        - point_3 (Vector) : socket 'Point 3' (Point 3)

        Returns
        -------
        - Curve [center_]
        """

        if point_1 is not None or point_2 is not None or point_3 is not None:
            curve = cls(Node('Curve Circle', {'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3}, mode='POINTS')._out)
            curve.center_ = curve.node.center
            return curve
        else:
            return cls(Node('Curve Circle', {'Resolution': resolution, 'Radius': radius}, mode='RADIUS')._out)

    # ----- Arc
    #
    @classmethod
    def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None,
                 start=None, middle=None, end=None, offset_angle=None,
                 connect_center=None, invert_arc=None):
        """ Node 'Arc' (GeometryNodeCurveArc)

        [!Node] Arc

        'mode' is set to 'POINTS' if one in (start, middle, end, offset_angle) is not None, 'RADIUS' otherwise.

        - mode (str): Node.mode in ('POINTS', 'RADIUS')

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - radius (Float) : socket 'Radius' (Radius)
        - start_angle (Float) : socket 'Start Angle' (Start Angle)
        - sweep_angle (Float) : socket 'Sweep Angle' (Sweep Angle)
        - start (Vector) : socket 'Start' (Start)
        - middle (Vector) : socket 'Middle' (Middle)
        - end (Vector) : socket 'End' (End)
        - offset_angle (Float) : socket 'Offset Angle' (Offset Angle)
        - connect_center (Boolean) : socket 'Connect Center' (Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (Invert Arc)

        Returns
        -------
        - Curve [center_, normal_, radius_]
        """


        if start is not None or middle is not None or end is not None or offset_angle is not None:
            curve = cls(Node('Arc', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end, 'Offset Angle': offset_angle,
                            'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='POINTS')._out)
            curve.center_ = curve.node.center
            curve.normal_ = curve.node.normal
            curve.radius_ = curve.node.radius
            return curve

        else:
            return cls(Node('Arc', {'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle,
                            'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='RADIUS')._out)

    # ----- Line

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None):
        """ Node 'Curve Line' (GeometryNodeCurvePrimitiveLine)

        [!Node] Curve Line

        'mode' is set to 'DIRECTION' if one in (direction, length) is not None, 'POINTS' otherwise.

        - mode (str): Node.mode in ('POINTS', 'DIRECTION')

        Arguments
        ---------
        - start (Vector) : socket 'Start' (Start)
        - end (Vector) : socket 'End' (End)

        Returns
        -------
        - Curve
        """
        if direction is not None or length is not None:
            return cls(Node('Curve Line', {'Start': start, 'Direction': direction, 'Length': length}, mode='DIRECTION')._out)
        else:
            return cls(Node('Curve Line', {'Start': start, 'End': end}, mode='POINTS')._out)

    # ----- Beziers

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ Node 'Bézier Segment' (GeometryNodeCurvePrimitiveBezierSegment)

        [!Node] Bézier Segment

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - start (Vector) : socket 'Start' (Start)
        - start_handle (Vector) : socket 'Start Handle' (Start Handle)
        - end_handle (Vector) : socket 'End Handle' (End Handle)
        - end (Vector) : socket 'End' (End)
        - mode (str): Node.mode in ('POSITION', 'OFFSET')

        Returns
        -------
        - Curve
        """
        return cls(Node('Bézier Segment', {'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end,
                'Resolution': resolution}, mode=mode)._out)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ Node 'Quadratic Bézier' (GeometryNodeCurveQuadraticBezier)

        [!Node] Quadratic Bézier

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - start (Vector) : socket 'Start' (Start)
        - middle (Vector) : socket 'Middle' (Middle)
        - end (Vector) : socket 'End' (End)

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadratic Bézier', {'Resolution': resolution, 'Start': start, 'End': end})._out)

    # ----- Special

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ Node 'Spiral' (GeometryNodeCurveSpiral)

        [!Node] Spiral

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (Resolution)
        - rotations (Float) : socket 'Rotations' (Rotations)
        - start_radius (Float) : socket 'Start Radius' (Start Radius)
        - end_radius (Float) : socket 'End Radius' (End Radius)
        - height (Float) : socket 'Height' (Height)
        - reverse (Boolean) : socket 'Reverse' (Reverse)

        Returns
        -------
        - Curve
        """
        return cls(Node('Spiral', {'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius,
            'End Radius': end_radius, 'Height': height, 'Reverse': reverse})._out)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ Node 'Star' (GeometryNodeCurveStar)

        [!Node] Star

        Arguments
        ---------
        - points (Integer) : socket 'Points' (Points)
        - inner_radius (Float) : socket 'Inner Radius' (Inner Radius)
        - outer_radius (Float) : socket 'Outer Radius' (Outer Radius)
        - twist (Float) : socket 'Twist' (Twist)

        Returns
        -------
        - Curve [outer_points_]
        """
        curve = cls(Node('Star', {'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})._out)
        curve.outer_points_ = curve.node.outer_points
        return curve

    # ----- Quadrilateral
    # mode in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')
    @classmethod
    def Quadrilateral(cls, width=None, height=None):
        """ Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

        [!Node] Quadrilateral

        Arguments
        ---------
        - width (Float) : socket 'Width' (Width)
        - height (Float) : socket 'Height' (Height)
        - mode (str): Node.mode in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadrilateral', {'Width': width, 'Height': height}, mode='RECTANGLE')._out)

    @classmethod
    def Rectangle(cls, width=None, height=None):
        """ Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

        [!Node] Quadrilateral

        Arguments
        ---------
        - width (Float) : socket 'Width' (Width)
        - height (Float) : socket 'Height' (Height)

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadrilateral', {'Width': width, 'Height': height}, mode='RECTANGLE')._out)

    @classmethod
    def Parallelogram(cls, width=None, height=None, offset=None):
        """ Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

        [!Node] Quadrilateral

        Arguments
        ---------
        - width (Float) : socket 'Width' (Width)
        - height (Float) : socket 'Height' (Height)

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadrilateral', {'Width': width, 'Height': height, 'Offset': offset}, mode='PARALLELOGRAM')._out)

    @classmethod
    def Trapezoid(cls, height=None, bottom_width=None, top_width=None, offset=None):
        """ Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

        [!Node] Quadrilateral

        Arguments
        ---------
        - height (Float) : socket 'Height' (Height)
        - bottom_width (Float) : socket 'Bottom Width' (Bottom Width)
        - top_width (Float) : socket 'Top Width' (Top Width)
        - offset (Float) : socket 'Offset' (Offset)

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadrilateral', {'Height': height, 'Bottom Width': bottom_width, 'Top Width': top_width, 'Offset': offset}, mode='TRAPEZOID')._out)

    @classmethod
    def Kite(cls, width=None, bottom_height=None, top_height=None):
        """ Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

        [!Node] Quadrilateral

        Arguments
        ---------
        - width (Float) : socket 'Width' (Width)
        - height (Float) : socket 'Height' (Height)

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadrilateral', {'Width': width, 'Bottom Height': bottom_height, 'Top Height': top_height}, mode='KITE')._out)

    @classmethod
    def Points(cls, point_1=None, point_2=None, point_3=None, point_4=None):
        """ Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

        [!Node] Quadrilateral

        Arguments
        ---------
        - width (Float) : socket 'Width' (Width)
        - height (Float) : socket 'Height' (Height)

        Returns
        -------
        - Curve
        """
        return cls(Node('Quadrilateral', {'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Point 4': point_4}, mode='POINTS')._out)

    # ----- From

    @classmethod
    def FromMesh(cls, mesh):
        """ Node 'Mesh to Curve' (GeometryNodeMeshToCurve)

        [!Node] Mesh to Curve

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)

        Returns
        -------
        - Curve
        """
        return Mesh(mesh)[mesh._sel].to_curve()

    @classmethod
    def FromEdgePaths(cls, mesh, next_vertex_index=None):
        """ Node 'Edge Paths to Curves' (GeometryNodeEdgePathsToCurves)

        [!Node] Edge Paths to Curves

        Arguments
        ---------
        - mesh (Geometry) : socket 'Mesh' (Mesh)
        - start_vertices (Boolean) : socket 'Start Vertices' (Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (Next Vertex Index)

        Returns
        -------
        - Curve
        """
        return Mesh(mesh).points[mesh._sel].edge_paths_to_curves(next_vertex_index=next_vertex_index)

    @classmethod
    def FromPoints(cls, points, curve_group_id=None, weight=None):
        """ Node 'Points to Curves' (GeometryNodePointsToCurves)

        [!Node] Points to Curves

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - curve_group_id (Integer) : socket 'Curve Group ID' (Curve Group ID)
        - weight (Float) : socket 'Weight' (Weight)

        Returns
        -------
        - Curve
        """
        return Cloud(points).to_curves(curve_group_id=curve_group_id, weight=weight)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='CURVE')

    # ----- Radius

    @property
    def radius(self):
        """ Node 'Radius' (GeometryNodeInputRadius)

        [!Node] Radius

        Returns
        -------
        - Float
        """

        return Node('Radius')._out

    @radius.setter
    def radius(self, value):
        """ Node 'Set Curve Radius' (GeometryNodeSetCurveRadius)

        [!Node] Set Curve Radius

        Arguments
        ---------
        - value (Float) : socket 'Radius' (Radius)
        """

        self._jump(Node('Set Curve Radius', {'Curve': self, 'Selection': self._sel, 'Radius': value})._out)

    # ----- Tilt

    @property
    def tilt(self):
        """ Node 'Curve Tilt' (GeometryNodeInputCurveTilt)

        [!Node] Curve Tilt

        Returns
        -------
        - Float
        """

        return Node('Curve Tilt')._out

    @tilt.setter
    def tilt(self, value):
        """ Node 'Set Curve Tilt' (GeometryNodeSetCurveTilt)

        [!Node] Set Curve Tilt

        Arguments
        ---------
        - tilt (Float) : socket 'Tilt' (Tilt)
        """

        self._jump(Node('Set Curve Tilt', {'Curve': self, 'Selection': self._sel, 'Tilt': value})._out)

    # ----- Curve normal

    @property
    def normal(self):
        raise NodeError(f"Curve.normal property is write only")

    @normal.setter
    def normal(self, value):
        """ Node 'Set Curve Normal' (GeometryNodeSetCurveNormal)

        [!Node] Set Curve Normal

        Arguments
        ---------
        - mode (str): Node.mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')
        """

        return self._jump(Node('Set Curve Normal', {'Curve': self, 'Selection': self._sel}, mode=value)._out)


    @classmethod
    @property
    def tangent(cls):
        """ Node 'Curve Tangent' (GeometryNodeInputTangent)

        [!Node] Curve Tangent

        Returns
        -------
        - Vector
        """
        return Node('Curve Tangent')._out

    @property
    def length(self):
        """ Node 'Curve Length' (GeometryNodeCurveLength)

        [!Node] Curve Length

        Returns
        -------
        - Float
        """
        return Node('Curve Length', {'Curve': self})._out

    @classmethod
    def endpoint_selection(cls, start_size=None, end_size=None):
        """ Node 'Endpoint Selection' (GeometryNodeCurveEndpointSelection)

        [!Node] Endpoint Selection

        Arguments
        ---------
        - start_size (Integer) : socket 'Start Size' (Start Size)
        - end_size (Integer) : socket 'End Size' (End Size)

        Returns
        -------
        - Boolean
        """
        return Node('Endpoint Selection', {'Start Size': start_size, 'End Size': end_size})._out

    # =============================================================================================================================
    # Topology

    @classmethod
    def curve_of_point(cls, point_index=None):
        """ Node 'Curve of Point' (GeometryNodeCurveOfPoint)

        [!Node] Curve of Point

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (Point Index)

        Returns
        -------
        - Node: [curve_index (Integer), index_in_curve (Integer)]
        """
        return Node('Curve of Point', {'Point Index': point_index})

    @classmethod
    def offset_point_in_curve(cls, point_index=None, offset=None):
        """ Node 'Offset Point in Curve' (GeometryNodeOffsetPointInCurve)

        [!Node] Offset Point in Curve

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (Point Index)
        - offset (Integer) : socket 'Offset' (Offset)

        Returns
        -------
        - Node: [is_valid_offset (Boolean), point_index (Integer)]
        """
        return Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset})

    @classmethod
    def points_of_curve(cls, curve_index=None, weights=None, sort_index=None):
        """ Node 'Points of Curve' (GeometryNodePointsOfCurve)

        [!Node] Points of Curve

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (Curve Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Node: [point_index (Integer), total (Integer)]
        """
        return Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})

    # =============================================================================================================================
    # Methods

    def set_normal(self, mode='MINIMUM_TWIST'):
        """ Node 'Set Curve Normal' (GeometryNodeSetCurveNormal)

        [!Node] Set Curve Normal

        Arguments
        ---------
        - mode (str): Node.mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')

        Returns
        -------
        - Curve
        """
        return Curve(Node('Set Curve Normal', {'Curve': self, 'Selection': self._sel}, mode=mode)._out)

    def set_normal_z_up(self):
        """ Node 'Set Curve Normal' (GeometryNodeSetCurveNormal)

        [!Node] Set Curve Normal

        Returns
        -------
        - Curve
        """
        return self.set_normal(mode='Z_UP')

    def set_normal_free(self):
        """ Node 'Set Curve Normal' (GeometryNodeSetCurveNormal)

        [!Node] Set Curve Normal

        Returns
        -------
        - Curve
        """
        return self.set_normal(mode='FREE')

    def sample(self, value=None, factor=None, length=None, curve_index=None, all_curves=False):
        """ Node 'Sample Curve' (GeometryNodeSampleCurve)

        [!Node] Sample Curve

        'mode' is set to 'LENGTH' if factor is None, else 'FACTOR'

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - mode (str): Node.mode in ('FACTOR', 'LENGTH')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - factor (Float) : socket 'Factor' (Factor)
        - length (Float) : socket 'Length' (Length)
        - curve_index (Integer) : socket 'Curve Index' (Curve Index)
        - all_curves (bool): Node.use_all_curves

        Returns
        -------
        - DataSocket [position_, tangent_, normal_]
        """

        sockets = {'Curves': self, 'Value': value, 'Curve Index': curve_index}
        if length is None:
            mode = 'FACTOR'
            sockets['Factor'] = factor
        else:
            mode = 'LENGTH'
            sockets['Length'] = length

        res = Node('Sample Curve', sockets, data_type=utils.get_data_type(value), mode=mode, use_all_curves=all_curves)._out
        res.position_ = res.node.position
        res.tangent_  = res.node.tangent
        res.normal_   = res.node.normal
        return res

    # =============================================================================================================================
    # Operations

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ Node 'Curve to Mesh' (GeometryNodeCurveToMesh)

        [!Node] Curve to Mesh

        Arguments
        ---------
        - profile_curve (Geometry) : socket 'Profile Curve' (Profile Curve)
        - fill_caps (Boolean) : socket 'Fill Caps' (Fill Caps)

        Returns
        -------
        - Mesh
        """
        return Mesh.FromCurve(self, profile_curve=profile_curve, fill_caps=fill_caps)

    def to_points(self, count=None, length=None, mode='EVALUATED'):
        """ Node 'Curve to Points' (GeometryNodeCurveToPoints)

        [!Node] Curve to Points

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - count (Integer) : socket 'Count' (Count)
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Cloud [tangent_, normal_, rotation_]
        """
        return Cloud.FromCurve(curve=self, count=count, length=length, mode='EVALUATED')

    def deform_on_surface(self):
        """ Node 'Deform Curves on Surface' (GeometryNodeDeformCurvesOnSurface)

        [!Node] Deform Curves on Surface

        Returns
        -------
        - Curve
        """
        return Curve(Node('Deform Curves on Surface', {'Curves': self})._out)

    # ----- Fill curve

    def fill(self, group_id=None, mode='TRIANGLES'):
        """ Node 'Fill Curve' (GeometryNodeFillCurve)

        [!Node] Fill Curve

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - mode (str): Node.mode in ('TRIANGLES', 'NGONS')

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Fill Curve', {'Curve': self, 'Group ID': group_id}, mode=mode)._out)

    # ----- Fillet curve

    def fillet(self, radius=None, limit_radius=None, count=None, mode='BEZIER'):
        """ Node 'Fillet Curve' (GeometryNodeFilletCurve)

        [!Node] Fillet Curve

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (Limit Radius)
        - count (Integer) : socket 'Integer' (Integer)
        - mode (str): Node.mode in ('BEZIER', 'POLY')

        Returns
        -------
        - Curve
        """
        return Curve(Node('Fillet Curve', {'Curve': self, 'Count': count, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)._out)

    # ----- Interpolate curves

    def interpolate(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ Node 'Interpolate Curves' (GeometryNodeInterpolateCurves)

        [!Node] Interpolate Curves

        Arguments
        ---------
        - guide_up (Vector) : socket 'Guide Up' (Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (Guide Group ID)
        - points (Geometry) : socket 'Points' (Points)
        - point_up (Vector) : socket 'Point Up' (Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (Max Neighbors)

        Returns
        -------
        - Curve [closest_index_, closest_weight_]
        """
        curve = Curve(Node('Interpolate Curves', {'Guide Curves': self, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id,
            'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})._out)
        curve.closest_index_  = curve.node.closest_index
        curve.closest_weight_ = curve.node.closest_weight
        return curve

    # ----- Resample

    def resample(self, count=None, length=None):
        """ Node 'Resample Curve' (GeometryNodeResampleCurve)

        [!Node] Resample Curve

        Parameter 'mode'
        ---------------
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')
        - if 'count' is not None : 'COUNT'
        - elif 'length' is not None : 'LENGTH'
        - else : 'EVALUATED'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (Count)

        Returns
        -------
        - Curve
        """
        sockets = {'Curve': self, 'Selection': self._sel}
        if count is not None:
            mode = 'COUNT'
            sockets['Count'] = count
        elif length is not None:
            mode = 'LENGTH'
            sockets['Length'] = length
        else:
            mode = 'EVALUATED'

        return Curve(Node('Resample Curve', sockets, mode=mode)._out)

    # ----- Trim

    def trim(self, start=None, end=None, mode='FACTOR'):
        """ Node 'Trim Curve' (GeometryNodeTrimCurve)

        [!Node] Trim Curve

        Arguments
        ---------
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)
        - mode (str): Node.mode in ('FACTOR', 'LENGTH')

        Returns
        -------
        - Curve
        """
        return Curve(Node('Trim Curve', {'Curve': self, 'Selection': self._sel, 'Start': start, 'End': end}, mode=mode)._out)

    def trim_factor(self, start=None, end=None):
        """ Node 'Trim Curve' (GeometryNodeTrimCurve)

        [!Node] Trim Curve

        Arguments
        ---------
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)

        Returns
        -------
        - Curve
        """
        return self.trim(start=start, end=end, mode='FACTOR')

    def trim_length(self, start=None, end=None):
        """ Node 'Trim Curve' (GeometryNodeTrimCurve)

        [!Node] Trim Curve

        Arguments
        ---------
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)

        Returns
        -------
        - Curve
        """
        return self.trim(start=start, end=end, mode='LENGTH')

    # ----- Various

    def reverse(self):
        """ Node 'Reverse Curve' (GeometryNodeReverseCurve)

        [!Node] Reverse Curve

        Returns
        -------
        - Curve
        """
        return Curve(Node('Reverse Curve', {'Curve': self, 'Selection': self._sel})._out)

    def subdivide(self, cuts=None):
        """ Node 'Subdivide Curve' (GeometryNodeSubdivideCurve)

        [!Node] Subdivide Curve

        Arguments
        ---------
        - cuts (Integer) : socket 'Cuts' (Cuts)

        Returns
        -------
        - Curve
        """
        return Curve(Node('Subdivide Curve', {'Curve': self, 'Cuts': cuts})._out)


# =============================================================================================================================
# =============================================================================================================================
# Cloud Points
# =============================================================================================================================
# =============================================================================================================================

class Cloud(Geometry):

    def _reset(self):

        super()._reset()

        self.points  = CloudPoint(self)

    # =============================================================================================================================
    # Constructors

    @classmethod
    def Points(cls, count=1, position=None, radius=None):
        """ Node 'Points' (GeometryNodePoints)

        [!Node] Points

        Arguments
        ---------
        - count (Integer) : socket 'Count' (Count)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """
        return cls(Node('Points', {'Count': count, 'Position': position, 'Radius': radius})._out)

    # ----- Curve to points

    @classmethod
    def FromCurve(cls, curve, count=None, length=None, mode='COUNT'):
        """ Node 'Curve to Points' (GeometryNodeCurveToPoints)

        [!Node] Curve to Points

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - count (Integer) : socket 'Count' (Count)
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Cloud [tangent_, normal_, rotation_]
        """
        points = Node('Curve to Points', {'Curve': curve, 'Count': count, 'Length': length}, mode=mode)._out
        points.tangent_ = points.node.tangent
        points.normal_ = points.node.normal
        points.rotation_ = points.node.rotation
        return points

    # ----- Instances to points

    @classmethod
    def FromInstances(cls, instances, position=None, radius=None):
        """ Node 'Instances to Points' (GeometryNodeInstancesToPoints)

        [!Node] Instances to Points

        Arguments
        ---------
        - instances (Geometry) : socket 'Instances' (Instances)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """
        return Cloud(Node('Instances to Points', {'Instances': instances, 'Selection': instances._sel, 'Position': position, 'Radius': radius})._out)

    # ----- Mesh to points

    @classmethod
    def FromMesh(cls, mesh, position=None, radius=None, mode='POINTS'):
        """ Node 'Mesh to Points' (GeometryNodeMeshToPoints)

        [!Node] Mesh to Points

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (Mesh)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)
        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

        Returns
        -------
        - Cloud
        """
        mesh = Mesh(mesh)[mesh._sel]
        if mode == 'CORNERS':
            return mesh.corners.to_points(position=position, radius=radius)
        elif mode == 'EDGES':
            return mesh.edges.to_points(position=position, radius=radius)
        elif mode == 'FACES':
            return mesh.faces.to_points(position=position, radius=radius)
        else:
            return mesh.points.to_points(position=position, radius=radius)

    @classmethod
    def FromVertices(cls, mesh, position=None, radius=None):
        return Mesh(mesh)[mesh._sel].points.to_points(position=position, radius=radius)

    @classmethod
    def FromFaces(cls, mesh, position=None, radius=None):
        return Mesh(mesh)[mesh._sel].faces.to_points(position=position, radius=radius)

    @classmethod
    def FromCorners(cls, mesh, position=None, radius=None):
        return Mesh(mesh)[mesh._sel].corners.to_points(position=position, radius=radius)

    @classmethod
    def FromEdges(cls, mesh, position=None, radius=None):
        return Mesh(mesh)[mesh._sel].edges.to_points(position=position, radius=radius)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='POINTCLOUD')

    # =============================================================================================================================
    # Methods

    # ----- to curves

    def to_curves(self, curve_group_id=None, weight=None):
        """ Node 'Points to Curves' (GeometryNodePointsToCurves)

        [!Node] Points to Curves

        Arguments
        ---------
        - curve_group_id (Integer) : socket 'Curve Group ID' (Curve Group ID)
        - weight (Float) : socket 'Weight' (Weight)

        Returns
        -------
        - Curve
        """
        return Curve(Node('Points to Curves', {'Points': self, 'Curve Group ID': curve_group_id, 'Weight': weight})._out)

    # ----- to mesh

    def to_vertices(self):
        """ Node 'Points to Vertices' (GeometryNodePointsToVertices)

        [!Node] Points to Vertices

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Points to Vertices', {'Points': self, 'Selection': self._sel})._out)

    # ----- to volume

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ Node 'Points to Volume' (GeometryNodePointsToVolume)

        [!Node] Points to Volume

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (Voxel Amount)
        - radius (Float) : socket 'Radius' (Radius)
        - resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Volume
        """
        return Volume(Node('Points to Volume', {'Points': self, 'Density': density, 'Voxel Size': voxel_size,
            'Voxel Amount': voxel_amount, 'Radius': radius}, resolution_mode=resolution_mode)._out)

# =============================================================================================================================
# =============================================================================================================================
# Instances
# =============================================================================================================================
# =============================================================================================================================

class Instances(Geometry):

    def _reset(self):

        super()._reset()

        self.insts  = Instance(self)

    # =============================================================================================================================
    # Constructors

    @classmethod
    def FromGeometry(cls, *geometries):
        """ Node 'Geometry to Instance' (GeometryNodeGeometryToInstance)

        [!Node] Geometry to Instance

        Arguments
        ---------
        - *geometries (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Instances
        """
        return cls(Node('Geometry to Instance', {'Geometry': list(geometries)})._out)

    @classmethod
    def FromString(cls, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None,
                overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT'):
        """ Node 'String to Curves' (GeometryNodeStringToCurves)

        [!Node] String to Curves

        Arguments
        ---------
        - string (String) : socket 'String' (String)
        - size (Float) : socket 'Size' (Size)
        - character_spacing (Float) : socket 'Character Spacing' (Character Spacing)
        - word_spacing (Float) : socket 'Word Spacing' (Word Spacing)
        - line_spacing (Float) : socket 'Line Spacing' (Line Spacing)
        - text_box_width (Float) : socket 'Text Box Width' (Text Box Width)
        - text_box_height (Float) : socket 'Text Box Height' (Text Box Height)
        - align_x (str): Node.align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
        - align_y (str): Node.align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
        - font (VectorFont): Node.font
        - overflow (str): Node.overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
        - pivot_mode (str): Node.pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')

        Returns
        -------
        - Instances [remainder_, line_, pivot_point_]
        """
        node = Node('String to Curves', {'String': string, 'Size': size, 'Character Spacing': character_spacing,
            'Word Spacing': word_spacing, 'Line Spacing': line_spacing,
            'Text Box Width': text_box_width, 'Text Box Height': text_box_height},
            overflow=overflow, align_x=align_x, align_y=align_y, pivot_mode=pivot_mode)
        insts = cls(node._out)
        insts.remainder_ = node.remainder
        insts.line_ = node.line
        insts.pivot_point_ = node.pivot_point
        return insts

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='INSTANCES')

    # =============================================================================================================================
    # Operations

    def realize(self, realize_all=None, depth=None):
        """ Node 'Realize Instances' (GeometryNodeRealizeInstances)

        [!Node] Realize Instances

        Arguments
        ---------
        - realize_all (Boolean) : socket 'Realize All' (Realize All)
        - depth (Integer) : socket 'Depth' (Depth)

        Returns
        -------
        - Geometry
        """
        return Node('Realize Instances', {'Geometry': self, 'Selection': self._sel, 'Realize All': realize_all, 'Depth': depth})._out

    def to_points(self, position=None, radius=None):
        """ Node 'Instances to Points' (GeometryNodeInstancesToPoints)

        [!Node] Instances to Points

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Points
        """
        return Cloud(Node('Instances to Points', {'Instances': self, 'Selection': self._sel, 'Position': position, 'Radius': radius})._out)

    def on_points(self, points, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Node 'Instance on Points' (GeometryNodeInstanceOnPoints)

        [!Node] Instance on Points

        Arguments
        ---------
        - instance (Geometry) : socket 'Instance' (Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (Instance Index)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)

        Returns
        -------
        - Instances
        """
        if isinstance(points, Domain):
            points = Cloud(points._geo).points[points._sel]
        else:
            points = Cloud(points).points[points._sel]

        return points.instance_on(instance=self, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale)

    def translate(self, translation=None, local_space=None):
        """ Node 'Translate Instances' (GeometryNodeTranslateInstances)

        [!Node] Translate Instances

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances
        """
        return Instances(Node('Translate Instances', {'Instances': self, 'Selection': self._sel, 'Translation': translation, 'Local Space': local_space})._out)

    def scale(self, scale=None, center=None, local_space=None):
        """ Node 'Scale Instances' (GeometryNodeScaleInstances)

        [!Node] Scale Instances

        Arguments
        ---------
        - scale (Vector) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances
        """
        return Instances(Node('Scale Instances', {'Instances': self, 'Selection': self._sel, 'Scale': scale, 'Center': center, 'Local Space': local_space})._out)

        #self.insts.scale = {'scale': scale, 'center': center, 'local_space': local_space}
        #return self

    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """ Node 'Rotate Instances' (GeometryNodeRotateInstances)

        [!Node] Rotate Instances

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - pivot_point (Vector) : socket 'Pivot Point' (Pivot Point)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances
        """
        return Instances(Node('Rotate Instances', {'Instances': self, 'Selection': self._sel, 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})._out)
        #self.insts.rotation = {'rotation': rotation, 'pivot_point': pivot_point, 'local_space': local_space}
        #return self

# =============================================================================================================================
# =============================================================================================================================
# Volume
# =============================================================================================================================
# =============================================================================================================================

class Volume(Geometry):

    DOMAIN_NAME = 'VOLUME'

    def _reset(self):
        super()._reset()

    # =============================================================================================================================
    # Constructors

    @classmethod
    def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
        """ Node 'Volume Cube' (GeometryNodeVolumeCube)

        [!Node] Volume Cube

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)
        - background (Float) : socket 'Background' (Background)
        - min (Vector) : socket 'Min' (Min)
        - max (Vector) : socket 'Max' (Max)
        - resolution_x (Integer) : socket 'Resolution X' (Resolution X)
        - resolution_y (Integer) : socket 'Resolution Y' (Resolution Y)
        - resolution_z (Integer) : socket 'Resolution Z' (Resolution Z)

        Returns
        -------
        - Volume
        """
        return cls(Node('Volume Cube', {'Density': density, 'Background': background, 'Min': min, 'Max': max,
            'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})._out)

    @classmethod
    def FromMesh(cls, mesh, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True):
        """ Node 'Mesh to Volume' (GeometryNodeMeshToVolume)

        [!Node] Mesh to Volume

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (Mesh)
        - density (Float) : socket 'Density' (Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (Voxel Amount)
        - interior_band_width (Float) : socket 'Interior Band Width' (Interior Band Width)
        - resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Volume
        """
        return Mesh(mesh).to_volume(density=density, voxel_amount=voxel_amount, interior_band_width=interior_band_width, voxel_size=voxel_size, amount=amount)

    @classmethod
    def FromPoints(cls, points, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ Node 'Points to Volume' (GeometryNodePointsToVolume)

        [!Node] Points to Volume

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Points)
        - density (Float) : socket 'Density' (Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (Voxel Amount)
        - radius (Float) : socket 'Radius' (Radius)
        - resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Volume
        """
        return Cloud(points).to_volume(density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode)

    # =============================================================================================================================
    # Methods

    def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):
        """ Node 'Distribute Points in Volume' (GeometryNodeDistributePointsInVolume)

        [!Node] Distribute Points in Volume

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)
        - seed (Integer) : socket 'Seed' (Seed)
        - spacing (Vector) : socket 'Spacing' (Spacing)
        - threshold (Float) : socket 'Threshold' (Threshold)
        - mode (str): Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')

        Returns
        -------
        - Cloud
        """
        return Cloud(Node('Distribute Points in Volume', {'Volume': self, 'Density': density,
            'Seed': seed, 'Spacing': spacing, 'Threshold': threshold}, mode=mode)._out)

    def distribute_random(self, density=None, seed=None):
        """ Node 'Distribute Points in Volume' (GeometryNodeDistributePointsInVolume)

        [!Node] Distribute Points in Volume

        Arguments
        ---------
        - density (Float) : socket 'Density' (Density)
        - seed (Integer) : socket 'Seed' (Seed)

        Returns
        -------
        - Cloud
        """
        return self.distribute_points(density=density, seed=seed, mode='DENSITY_RANDOM')

    def distribute_grid(self, spacing=None, threshold=None):
        """ Node 'Distribute Points in Volume' (GeometryNodeDistributePointsInVolume)

        [!Node] Distribute Points in Volume

        Arguments
        ---------
        - spacing (Vector) : socket 'Spacing' (Spacing)
        - threshold (Float) : socket 'Threshold' (Threshold)

        Returns
        -------
        - Cloud
        """
        return self.distribute_points(spacing=spacing, threshold=threshold, mode='DENSITY_GRID')

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

        [!Node] Volume to Mesh

        Arguments
        ---------
        - voxel_size (Float) : socket 'Voxel Size'
        - voxel_amount (Float) : socket 'Voxel Amount'
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)
        - resolution_mode (str): Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Mesh
        """
        sockets = {'Volume': self, 'Adaptivity': adaptivity}
        if resolution_mode == 'GRID':
            sockets['Threshold'] = threshold
        elif resolution_mode == 'VOXEL_AMOUNT':
            sockets['Voxel Amount'] = voxel_amount
            sockets['Threshold'] = threshold
        elif resolution_mode == 'VOXEL_SIZE':
            sockets['Voxel Size'] = voxel_size
            sockets['Threshold'] = threshold

        return Mesh(Node('Volume to Mesh', sockets, resolution_mode=resolution_mode)._out)


    def to_mesh_grid(self, threshold=None, adaptivity=None):
        """ Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

        [!Node] Volume to Mesh

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)

        Returns
        -------
        - Mesh
        """
        return self.to_mesh(threshold=threshold, adaptivity=adaptivity, resolution_mode='GRID')

    def to_mesh_amount(self, voxel_amount=None, threshold=None, adaptivity=None):
        """ Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

        [!Node] Volume to Mesh

        Arguments
        ---------
        - voxel_amount (Float) : socket 'Voxel Amount'
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)

        Returns
        -------
        - Mesh
        """
        return self.to_mesh(voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode='VOXEL_AMOUNT')

    def to_mesh_size(self, voxel_size=None, threshold=None, adaptivity=None):
        """ Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

        [!Node] Volume to Mesh

        Arguments
        ---------
        - voxel_size (Float) : socket 'Voxel Size'
        - threshold (Float) : socket 'Threshold' (Threshold)
        - adaptivity (Float) : socket 'Adaptivity' (Adaptivity)

        Returns
        -------
        - Mesh
        """
        return self.to_mesh(voxel_size=voxel_size, threshold=threshold, adaptivity=adaptivity, resolution_mode='VOXEL_SIZE')
