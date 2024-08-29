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
        return Node('Viewer', {'Geometry': self, 'Value': value}, data_type=utils.get_data_type(value))

    # ----- Operations

    def set_id(self, id=None):
        return Node("Set ID", {'Geometry': self, 'Selection': self._sel, 'ID': id})._out

    def set_position(self, position=None, offset=None):
        return Node("Set Position", {'Geometry': self, 'Selection': self._sel, 'Position': position, 'Offset': offset})._out

    def set_material(self, material=None):
        return Node("Set Material", {'Geometry': self, 'Selection': self._sel, 'Material': material})._out

    def set_shade_smooth(self, shade_smooth=True, edge=False):
        return Node("Set Shade Smooth", {'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE' if edge else 'FACE')._out

    # ----- Remove named attribute

    def remove_named_attribute(self, name, exact=True):
        node = Node('Remove Named Attribute', {'Geometry': self, 'Name': name}, pattern_mode = 'EXACT' if exact else 'WILDCARD')
        self._jump(node._out)

    # ====================================================================================================
    # Sample nodes without domain

    # ----- Index of nearest

    @staticmethod
    def index_of_nearest(position=None, group_id=None):
        index = Node('Index of Nearest', {'Position': position, 'Group ID': group_id})._out
        index.has_neighbor_ = index.node.has_neighbor
        return index

    # ----- Raycast

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, interpolated=True):
        data_type = utils.get_value_data_type_1(attribute)
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
        bb = Node('Bounding Box', {'Geometry': self})._out
        bb.min_ = bb.node.min
        bb.max_ = bb.node.max
        return Mesh(bb)

    @property
    def convex_hull(self):
        return Mesh(Node('Convex Hull', {'Geometry': self})._out)

    def merge_by_distance(self, distance=None, all=True):
        return self._geo_type(self._node('Merge by Distance', {'Distance': distance}, mode = 'ALL' if all else 'CONNECTED')._out)

    def transform(self, translation=None, rotation=None, scale=None, matrix=None):
        if matrix is None:
            return self._geo_type(Node('Transform Geometry', {'Geometry': self, 'Translation': translation, 'Rotation': rotation, 'Scale': scale}, mode='COMPONENTS')._out)
        else:
            return self._geo_type(Node('Transform Geometry', {'Geometry': self, 'Transform': matrix}, mode='MATRIX')._out)

    @property
    def separate_components(self):
        return self._cache('Separate Components', {'Geometry': self})

    @property
    def mesh(self):
        return Mesh(self.separate_components.mesh)

    @property
    def curve(self):
        return Curve(self.separate_components.curve)

    @property
    def point_cloud(self):
        return Cloud(self.separate_components.point_cloud)

    @property
    def volume(self):
        return Volume(self.separate_components.volume)

    @property
    def instances(self):
        return Instances(self.separate_components.instances)

    def join(self, *geometries):

        if False and self.node._bnode.bl_idname == 'GeometryNodeJoinGeometry':
            node = self.node
            node.set_input_sockets({'Geometry': list(geometries)})
        else:
            node = Node('Join Geometry', {'Geometry': [self] + list(geometries)})

        geo = node._out
        classes = set()
        for g in geometries:
            classes.add(type(g))
        if len(classes) == 1:
            return list(classes)[0](geo)
        else:
            return geo

    # ====================================================================================================
    # Operations

    def to_instance(self, *geometries):
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

    def capture_attribute(self, attribute, **others):
        node = self._node('Capture Attribute')
        items = node._bnode.capture_items
        for i, (attr_name, attr_value) in enumerate({'attribute': attribute, **others}.items()):
            items.new(utils.get_input_type(attr_value), attr_name)
            node.plug_value_into_socket(attr_value, node.in_socket(1 + i))

        self._geo._jump(node._out)

        if len(others) == 0:
            return node.attribute
        else:
            return node

    def capture(self, attribute, **others):
        return self.capture_attribute(attribute, **others)

    # ----- Store named attribute

    def store_named_attribute(self, name, value=None):

        data_type   = utils.get_data_type(value)
        node = self._node('Store Named Attribute', {'Name': name, 'Value': value}, data_type=data_type)

        return self._geo._jump(node._out)

    def store(self, name, value=None):
        return self.store_named_attribute(name, value=value)

    # ====================================================================================================
    # Sample nodes with domain

    def proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        target = self.restrict_domain(['POINT', 'EDGE', 'FACE'], 'Proximity')
        position = Node('Geometry Proximity', {'Geometry': self._geo, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=self.DOMAIN_NAME + 'S')._out
        position.distance_ = position.node.distance
        position.is_valid_ = position.node.is_valid
        return position

    def sample_index(self, value=None, index=0, clamp=None):
        return self._node('Sample Index', {'Value': value, 'Index': index}, clamp=clamp, data_type=utils.get_data_type(value))._out

    def sample_nearest(self, sample_position=None):
        return self._node('Sample Nearest', {'Sample Position': sample_position})._out

    # ====================================================================================================
    # Geometry Operations

    def delete_geometry(self, mode='ALL'):
        self.exclude_corner('delete_geometry')
        return self._geo_type(self._node('Delete Geometry', mode=mode)._out)

    def delete(self):
        return self.delete_geometry(mode='ALL')

    def delete_faces(self):
        return self.delete_geometry(mode='ONLY_FACE')

    def delete_edges_and_faces(self):
        return self.delete_geometry(mode='EDGE_FACE')

    def duplicate_elements(self, amount=1):
        self.exclude_corner('duplicate_elements')
        domain = self.domain_name(rename={'CURVE': 'SPLINE'})
        geo = self._geo_type(self._node('Duplicate Elements', {'Amount': amount}, domain=domain)._out)
        geo.duplicate_index_= geo.node.duplicate_index
        return geo

    def sort_elements(self, group_id=None, sort_weight=None):
        self.exclude_corner('sort_elements')
        return self._geo_type(self._node('Sort Elements', {'Group ID': group_id, 'Sort Weight': sort_weight})._out)

    def separate(self, group_id=None, sort_weight=None):
        self.exclude_corner('separate')
        geo = self._geo_type(self._node('Separate Geometry')._out)
        geo.inverted_ = self._geo_type(geo.node.inverted)
        return geo

    def split_to_instances(self, group_id=None):
        self.exclude_corner('split_to_instances')
        instances = Instances(self._node('Split to Instances', {'Group ID': group_id})._out)
        instances.group_id_ = instances.node.group_id
        return instances

    # ----- Mesh conversion to points

    def to_points(self, position=None, radius=None):
        mode = self.plural_domain(['POINT', 'EDGE', 'FACE', 'CORNER'], 'Mesh to Point')
        return Cloud(Node('Mesh to Points', {'Mesh': self._geo, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode=mode)._out)

    # ----- Extrusion

    def extrude(self, offset=None, offset_scale=None, individual=None):
        mode = self.plural_domain(['POINT', 'EDGE', 'FACE'], 'Extrude Mesh')
        node = Node('Extrude Mesh', {'Mesh': self._geo, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode = mode)

        mesh = Mesh(node.mesh)
        mesh.top_  = node.top
        mesh.side_ = node.side

        return mesh

    # ----- Field

    def accumulate_field(self, value=None, group_id=None, ):
        # data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
        data_type = utils.get_data_type(value, ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'))
        return Node('Accumulate Field', {'Value': value, 'Group ID': group_id}, data_type=data_type, domain=self.DOMAIN_NAME)

    def evaluate_at_index(self, index=None, value=None):
        data_type = utils.get_data_type(value)
        return Node('Evaluate at Index', {'Index': index, 'Value': value}, data_type=data_type, domain=self.DOMAIN_NAME)._out

    def evaluate_on_domain(self, value=None):
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
        return self._geo.domain_size.point_count

    # ----- Instance on points

    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        return Instances(Node('Instance on Points', {'Points': self._geo, 'Selection': self._sel,
                'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index,
                'Rotation': rotation, 'Scale': scale})._out)

class Vertex(Point):

    # ----- Vertex neighbors

    @property
    def neighbors(self):
        return self._cache('Vertex Neighbors')

    @property
    def neighbors_vertex_count(self):
        return self.neighbors.vertex_count

    @property
    def neighbors_face_count(self):
        return self.neighbors.face_count

    # ----- Edge paths to selection

    def paths_to_selection(self, next_vertex_index):
        return Node('Edge Paths to Selection', {'Start Vertices': self._sel, 'Next Vertex Index': next_vertex_index})._out

    # ----- Edge paths to curves

    def paths_to_curves(self, next_vertex_index=None):
        return Curve(Node('Edge Paths to Curves', {'Mesh': self._geo, 'Start Vertices': self._sel, 'Next Vertex Index': next_vertex_index})._out)

    # ----- Topology

    @classmethod
    def edge_index(cls, vertex_index=None,weights=None, sort_index=None):
        index = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

    @classmethod
    def corner_index(cls, vertex_index=None,weights=None, sort_index=None):
        index = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

class SplinePoint(Point):

    # ----- Radius

    @property
    def radius(self):
        return Node('Radius')._out

    @radius.setter
    def radius(self, value):
        self._geo._jump(Node('Set Curve Radius', {'Curve': self._geo, 'Selection': self._sel, 'Radius': value})._out)

    # ----- Tilt

    @property
    def tilt(self):
        return Node('Curve Tilt')._out

    @tilt.setter
    def tilt(self, value):
        self._geo._jump(Node('Set Curve Tilt', {'Curve': self._geo, 'Selection': self._sel, 'Tilt': value})._out)

    # ----- Curve normal

    @property
    def normal(self):
        raise NodeError(f"Curve.normal property is write only")

    @normal.setter
    def normal(self, value):
        # mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')
        return self._geo._jump(Node('Set Curve Normal', {'Curve': self._geo, 'Selection': self._sel}, mode=value)._out)

    # ----- Handle positions

    @classmethod
    def handle_positions(cls, relative=None):
        return Node('Curve Handle Positions', {'Relative': relative})

    def set_handle_positions(self, position=None, offset=None, mode=None):
        self._geo._jump(Node('Set Handle Positions', {'Curve': self._geo, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode=mode)._out)

    @property
    def left_handle_position(self):
        return self.handle_positions(relative=False).left

    @left_handle_position.setter
    def left_handle_position(self, value):
        self.set_handle_positions(position=value, mode='LEFT')

    @property
    def right_handle_position(self):
        return self.handle_positions(relative=False).right

    @right_handle_position.setter
    def right_handle_position(self, value):
        self.set_handle_positions(position=value, mode='RIGHT')

    # Offset

    @property
    def left_handle_offset(self):
        return self.handle_positions(relative=True).left

    @left_handle_offset.setter
    def left_handle_offset(self, value):
        self.set_handle_positions(offset=value, mode='LEFT')

    @property
    def right_handle_offset(self):
        return self.handle_positions(relative=True).right

    @right_handle_offset.setter
    def right_handle_offset(self, value):
        self.set_handle_positions(offset=value, mode='RIGHT')

    # ----- Handle type

    @classmethod
    def handle_type_selection(cls, left=True, right=True, handle_type='AUTO'):
        # handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        mode = set()
        if left:
            mode.add('LEFT')
        if right:
            mode.add('RIGHT')
        return Node('Endpoint Selection', mode=mode, handle_type=handle_type)._out

    def set_handle_type(self, left=True, right=True, handle_type='AUTO'):
        # handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        mode = set()
        if left:
            mode.add('LEFT')
        if right:
            mode.add('RIGHT')
        self._geo._jump(Node('Set Handle Type', {'Curve': self._geo, 'Selection': self._sel}, mode=mode, handle_type=handle_type)._out)





class CloudPoint(Point):

    # ----- Radius

    @property
    def radius(self):
        return Node('Radius')._out

    @radius.setter
    def radius(self, value):
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
        return self._geo.domain_size.face_count

    # =============================================================================================================================
    # Properties

    # ----- Smooth

    @property
    def smooth(self):
        return Node('Is Face Smooth')._out

    @smooth.setter
    def smooth(self, value):
        self._geo._jump(Node('Set Shade Smooth', {'Geometry': self._geo, 'Selection': self._sel, 'Shade Smooth': value}, domain='FACE')._out)

    @property
    def area(self):
        return Node('Face Area')._out

    def is_planar(self, threshold=None):
        return Node('Is Face Planar', {'Threshold': threshold})._out

    def group_boundaries(self, face_group_id=None):
        return Node('Face Group Boundaries', {'Face Group ID': face_group_id})._out

    @property
    def neighbors(self):
        return self._cache('Face Neighbors')

    @property
    def neighbors_vertex_count(self):
        return self.neighbors.vertex_count

    @property
    def neighbors_face_count(self):
        return self.neighbors.face_count

    # ----- Flip

    def flip(self):
        return Node('Flip Faces', {'Mesh': self._geo, 'Selection': self._sel})._out

    # ----- Scale

    def scale(self, scale=None, center=None, uniform=True):
        # scale_mode in ('UNIFORM', 'SINGLE_AXIS')
        return self._geo._jump(Node('Scale Elements', {'Mesh': self._geo, 'Selection': self._sel, 'Scale': scale, 'Center': center},
            domain='FACE', scale_mode = 'UNIFORM' if uniform else 'SINGLE_AXIS')._out)

    # ----- Topology

    @classmethod
    def corner_index(cls, vertex_index=None,weights=None, sort_index=None):
        index = Node('Corners of Face', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

    # ----- Distribute

    def distribute_points(self, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, poisson=False):
        return self._geo[self._sel].distribute_points_on_faces(distance_min=distance_min, density_max=density_max,
            density=density, density_factor=density_factor, seed=seed, poisson=poisson)

# =============================================================================================================================
# =============================================================================================================================
# Edge Domain
# =============================================================================================================================
# =============================================================================================================================

class Edge(Domain):
    DOMAIN_NAME = 'EDGE'

    @property
    def count(self):
        return self._geo.domain_size.edge_count

    # =============================================================================================================================
    # Properties

    # ----- Angle

    @property
    def angle(self):
        return self._cache('Edge Angle')

    @property
    def unsigned_angle(self):
        return self.angle.unsigned_angle

    @property
    def signed_angle(self):
        return self.angle.signed_angle

    # ----- Neighbors

    @property
    def neighbors(self):
        return Node('Edge Neighbpors')._out

    # ----- Edge vertices

    @property
    def vertices(self):
        return self._cache('Edge Vertices')

    @property
    def vertex_index_1(self):
        return self.vertices.vertex_index_1

    @property
    def vertex_index_2(self):
        return self.vertices.vertex_index_2

    @property
    def position_1(self):
        return self.vertices.position_1

    @property
    def position_2(self):
        return self.vertices.position_2

    # ----- Smooth

    @property
    def smooth(self):
        return Node('Is Edge Smooth')._out

    @smooth.setter
    def smooth(self, value):
        self._geo._jump(Node('Set Shade Smooth', {'Geometry': self._geo, 'Selection': self._sel, 'Shade Smooth': value}, domain='EDGE')._out)

    # ----- Shortest Edge Paths

    def shortest_paths(self, edge_cost=None):
        index = Node('Shortest Edge Paths', {'End Vertex': self._sel, 'Edge Cost': edge_cost}).next_vertex_index
        index.total_cost_ = index.node.total_cost
        return index

    # ----- To face groups

    @property
    def to_face_groups(self):
        return Node('Edges to Face Groups', {'Boundary Edges': self._sel})._out

    # ----- Split

    def split(self):
        return Node('Split Edges', {'Mesh': self._geo, 'Selection': self._sel})._out

    # ----- Scale

    def scale(self, scale=None, center=None, uniform=True):
        # scale_mode in ('UNIFORM', 'SINGLE_AXIS')
        return self._geo._jump(Node('Scale Elements', {'Mesh': self._geo, 'Selection': self._sel, 'Scale': scale, 'Center': center},
            domain='EDGE', scale_mode = 'UNIFORM' if uniform else 'SINGLE_AXIS')._out)

    # ----- Topology

    @classmethod
    def corner_index(cls, vertex_index=None,weights=None, sort_index=None):
        index = Node('Corners of Edge', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out
        index.total_ = index.node.total
        return index

# =============================================================================================================================
# =============================================================================================================================
# Corner Domain
# =============================================================================================================================
# =============================================================================================================================

class Corner(Domain):
    DOMAIN_NAME = 'CORNER'

    @property
    def count(self):
        return self._geo.domain_size.face_corner_count

    # ----- Topology

    @classmethod
    def next_edge_index(cls, corner_index=None):
        index = Node('Edges of Corner', {'Corner Index': corner_index})._out
        index.previous_edge_index_ = index.node.previous_edge_index
        return index

    @classmethod
    def face_index(cls, corner_index=None):
        index = Node('Face of Corner', {'Corner Index': corner_index})._out
        index.index_in_face_ = index.node.index_in_face
        return index

    @classmethod
    def offset_in_face(cls, corner_index=None, offset=None):
        return Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})._out

    @classmethod
    def vertex_index(cls, corner_index=None):
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
        return self._geo.domain_size.spline_count

    # ====================================================================================================
    # Properties

    # ----- Cyclic

    @property
    def is_cyclic(self):
        return Node('Is Spline Cyclic')._out

    @is_cyclic.setter
    def is_cyclic(self, value):
        return self._geo._jump(Node('Set Spline Cyclic', {'Geometry': self._geo, 'Selection': self._sel, 'Cyclic': value})._out)

    # ----- Resolution

    @property
    def resolution(self):
        return Node('Spline Resolution')._out

    @resolution.setter
    def resolution(self, value=None):
        self._geo._jump(Node('Set Spline Resolution', {'Geometry': self._geo, 'Resolution': value})._out)

    # ----- Spline type

    @property
    def type(self):
        raise NodeError(f"Curve.spline_type is write only.")

    @type.setter
    def type(self, value):
        # value in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')
        self._geo._jump(Node('Set Spline Type', {'Curve': self._geo, 'Selection': self._sel}, spline_type=value)._out)

    # ----- Read only

    @property
    def parameter(self):
        return self._cache('Spline Parameter')

    @classmethod
    @property
    def length(cls):
        length = Node('Spline Length')._out
        length.point_count_ = length.node.point_count
        return length


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
        return Node('Instance Transform')._out

    @transform.setter
    def transform(self, value):
        return self._geo._jump(Node('Set Instance Transform', {'Instances': self._geo, 'Selection': self._sel, 'Transform': value})._out)

    # ----- Translate

    def translate(self, translation=None, local_space=None):
        return self._geo._jump(Node('Translate Instances', {'Instances': self._geo, 'Selection': self._sel, 'Translation': translation, 'Local Space': local_space})._out)

    # ----- Scale

    @property
    def scale(self):
        return Node('Instance Scale')._out

    @scale.setter
    def scale(self, value):
        keys = {'scale': 'Scale', 'center': 'Center', 'local_space': 'Local Space'}
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                node_key = keys.get(k.lower(), None)
                if node_key is None:
                    raise NodeError(f"Node 'Scale Instances' error: invalid key '{k}' to set instance scale.", valid_keys=list(keys.keys()))
                sockets[node_key] = v
        else:
            sockets['Scale'] = value

        return self._geo._jump(Node('Scale Instances', sockets)._out)

    # ----- Rotation

    @property
    def rotation(self):
        return self.Node('Instance Rotation')._out

    @rotation.setter
    def rotation(self, value):
        keys = {'rotation': 'Rotation', 'pivot_point': 'Pivot Point', 'local_space': 'Local Space'}
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                node_key = keys.get(k.lower(), None)
                if node_key is None:
                    raise NodeError(f"Node 'Rotate Instances' error: invalid key '{k}' to set instance rotation.", valid_keys=list(keys.keys()))
                sockets[node_key] = v
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
        return cls(Node('Curve to Mesh', {'Curve': curve, 'Profile Curve': profile_curve, 'Fill Caps': fill_caps})._out)

    @classmethod
    def FromPoints(cls, points):
        return Cloud(points).to_vertices()

    @classmethod
    def FromVolume(cls, volume, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        return Volume(volume).to_mesh(voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode)

    # =============================================================================================================================
    # Properties

    @property
    def island(self):
        return self._cache('Mesh Island')

    @property
    def island_index(self):
        return self.island.island_index

    @property
    def island_count(self):
        return self.island.island_count

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='MESH')

    @classmethod
    def Cube(self, size=(1, 1, 1), vertices_x=2, vertices_y=2, vertices_z=2):
        node = Node('Cube', {'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def Line(cls, count=10, resolution=None, start_location=(0, 0, 0), offset=None, end_location=None):
        # mode in  ('OFFSET', 'END_POINTS')
        # count_mode in ('TOTAL', 'RESOLUTION')
        # if end_location is not None or resolution is not None:
        # - mode = 'END_POINTS'
        # - count_mode = 'TOTAL' if resolution is None
        # else
        # - mode = 'OFFSET'

        if end_location is not None or resolution is not None:
            count_mode = 'TOTAL' if resolution is None else 'RESOLUTION'
            return Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': end_location},
                mode='END_POINTS', count_mode=count_mode)._out
        else:
            return Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': offset},
                mode='OFFSET')._out

    @classmethod
    def LineEndPoints(cls, count=None, resolution=None, start_location=(0, 0, 0), end_location=None):
        # mode in  ('OFFSET', 'END_POINTS')
        # count_mode in ('TOTAL', 'RESOLUTION')
        if count is None:
            return Node('Mesh Line', {'Resolution': resolution, 'Start Location': start_location, 'Offset': end_location},
               mode='END_POINTS', count_mode='RESOLUTION')._out
        else:
            return Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': end_location},
               mode='END_POINTS', count_mode='TOTAL')._out

    @classmethod
    def Cone(cls, vertices=32, side_segments=1, fill_segments=1, radius_top=0.0, radius_bottom=1.0, depth=2.0,
        fill_type='NGON'):
        # fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')
        node = Node('Cone', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments,
            'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)
        mesh = Mesh(node.mesh)
        mesh.top_ = node.top
        mesh.bottom_ = node.bottom
        mesh.side_ = node.side
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def Cylinder(cls, vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0,
        fill_type='NGON'):
        # fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')
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
        # fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')
        node = Node('Mesh Circle', {'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)
        mesh = Mesh(node.mesh)
        return mesh

    @classmethod
    def Disk(cls, vertices=32, radius=1.0, fill_type='NGON'):
        # fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')
        return cls.Circle(vertices=vertices, radius=radius, fill_type=fill_type)

    @classmethod
    def Grid(cls, size_x=1.0, size_y=1.0, vertices_x=3, vertices_y=3):
        node = Node('Grid', {'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def IcoSphere(cls, radius=1.0, subdivisions=1):
        node = Node('Ico Sphere', {'Radius': radius, 'Subdivisions': subdivisions})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh

    @classmethod
    def UVSphere(cls, segments=32, rings=16, radius=1.0):
        node = Node('UV Sphere', {'Segments': segments, 'Rings': rings, 'Radius': radius})
        mesh = Mesh(node.mesh)
        mesh.uv_map_ = node.uv_map
        return mesh


    # =============================================================================================================================
    # Sample

    def sample_nearest_surface(self, value=None, group_id=None, sample_position=None, sample_group_id=None):
        input_type = utils.get_input_type(value)
        res = Node('Sample Nearest Surface', {'Mesh': self, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=input_type)._out
        res.is_valid_ = res.node.is_valid
        return res

    def sample_uv_surface(self, value=None, uv_map=None, sample_uv=None):
        input_type = utils.get_input_type(value)
        res = Node('Sample UV Surface', {'Mesh': self, 'Value': value, 'UV Map': uv_map, 'Sample UV': sample_uv}, data_type=input_type)._out
        res.is_valid_ = res.node.is_valid
        return res

    # =============================================================================================================================
    # Conversion

    def to_curve(self):
        return Curve(Node('Mesh to Curve', {'Mesh': self, 'Selection': self._sel})._out)

    def to_volume(self, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True):
        # resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        if amount:
            return Volume(Node('Mesh to Volume', {'Mesh': self, 'Density': density, 'Voxel Amount': voxel_amount, 'Interior Band Width': interior_band_width}, resolution_mode='VOXEL_AMOUNT')._out)
        else:
            return Volume(Node('Mesh to Volume', {'Mesh': self, 'Density': density, 'Voxel Size': voxel_size, 'Interior Band Width': interior_band_width}, resolution_mode='VOXEL_SIZE')._out)

    # =============================================================================================================================
    # Operations

    def dual(self, keep_boundaries=None):
        return Mesh(Node('Dual Mesh', {'Mesh': self, 'Keep Boundaries': keep_boundaries})._out)

    def subdivide(self, level=None):
        return Mesh(Node('Subdivide Mesh', {'Mesh': self, 'Level': level})._out)

    def triangulate(self, minimum_vertices=None, beauty=True, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY'):
        # quad_method in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
        # ngon_method in ('BEAUTY', 'CLIP')
        return Mesh(Node('Triangulate', {'Mesh': self, 'Selection': self._sel, 'Minimum Vertices': minimum_vertices},
            quad_method=quad_method, ngon_method=ngon_method)._out)

    def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL'):
        # uv_smooth in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
        # boundary_smooth in ('PRESERVE_CORNERS', 'ALL')
        return Mesh(Node('Subdivision Surface', {'Mesh': self, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease},
            uv_smooth=uv_smooth, boundary_smooth=boundary_smooth)._out)

    def smooth_by_angle(self, angle=None, ignore_sharpness=None):
        return Mesh(Node('Smooth by Angle', {'Mesh': self, 'Angle': angle, 'Ignore Sharpness': ignore_sharpness})._out)

    # ----- Mesh Boolean

    def difference(self, *other, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        # operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        # solver in  ('EXACT', 'FLOAT')
        return Mesh(Node('Mesh Boolean', {'Mesh 1': self, 'Mesh 2': list(other), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, solver=solver, operation='DIFFERENCE')._out)

    def intersect(self, *other, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        # operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        # solver in  ('EXACT', 'FLOAT')
        return Mesh(Node('Mesh Boolean', {'Mesh 2': [self] + list(other), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, solver=solver, operation='INTERSECT')._out)

    def union(self, *other, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        # operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        # solver in  ('EXACT', 'FLOAT')
        return Mesh(Node('Mesh Boolean', {'Mesh 2': [self] + list(other), 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}, solver=solver, operation='UNION')._out)

    # ----- UV

    def pack_uv_islands(self, uv=None, margin=None, rotate=None):
        return Node('Pack UV Islands', {'UV': uv, 'Selection': self._sel, 'Margin': margin, 'Rotate': rotate})._out

    def uv_unwrap(self, seam=None, margin=None, fill_holes=False, angle_based=True):
        # method in ('ANGLE_BASED', 'CONFORMAL')
        method = 'ANGLE_BASED' if angle_based else 'CONFORMAL'
        return Node('UV Unwrap', {'Selection': self._sel, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)._out

    # ----- Distribute points

    def distribute_points_on_faces(self, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, poisson=False):
        # distribute_method in ('RANDOM', 'POISSON')
        method = 'POISSON' if poisson else 'RANDOM'
        node = Node('Distribute Points on Faces', {'Mesh': self, 'Selection': self._sel,
            'Distance Min': distance_min, 'Density Max': density_max, 'Density': density,
            'Density Factor': density_factor, 'Seed': seed}, distribute_method = method)
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
    def Circle(cls, resolution=None, radius=None, point_1=None, point_2=None, point_3=None, mode='RADIUS'):
        # mode in ('POINTS', 'RADIUS')
        if point_1 is not None or point_2 is not None or point_3 is not None:
            curve = cls(Node('Curve Circle', {'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3}, mode='POINTS')._out)
            curve.center_ = curve.node.center
            return curve
        else:
            return cls(Node('Curve Circle', {'Resolution': resolution, 'Radius': radius}, mode='RADIUS')._out)

        if mode == 'RADIUS':
            return cls.CircleRadius(resolution=resolution, radius=radius, )
        else:
            return cls.CirclePoints(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3)

    # ----- Arc
    #
    @classmethod
    def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None,
                 start=None, middle=None, end=None, offset_angle=None,
                 connect_center=None, invert_arc=None):

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
        # mode in  ('POINTS', 'DIRECTION')
        if direction is not None or length is not None:
            return cls(Node('Curve Line', {'Start': start, 'Direction': direction, 'Length': length}, mode='DIRECTION')._out)
        else:
            return cls(Node('Curve Line', {'Start': start, 'End': end}, mode='POINTS')._out)

    # ----- Beziers

    @classmethod
    def BezierSegment(cls, start=None, start_handle=None, end_handle=None, end=None, resolution=None, offset=False):
        return cls(Node('Bézier Segment', {'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end,
                'Resolution': resolution}, mode='OFFSET' if offset else 'POSITION')._out)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        return cls(Node('Quadratic Bézier', {'Resolution': resolution, 'Start': start, 'End': end})._out)

    # ----- Special

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        return cls(Node('Spiral', {'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius,
            'End Radius': end_radius, 'Height': height, 'Reverse': reverse})._out)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        curve = cls(Node('Star', {'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})._out)
        curve.outer_points_ = curve.node.outer_points
        return curve

    # ----- Quadrilateral
    # mode in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

    @classmethod
    def Rectangle(cls, width=None, height=None):
        return cls(Node('Quadrilateral', {'Width': width, 'Height': height}, mode='RECTANGLE')._out)

    @classmethod
    def Parallelogram(cls, width=None, height=None, offset=None):
        return cls(Node('Quadrilateral', {'Width': width, 'Height': height, 'Offset': offset}, mode='PARALLELOGRAM')._out)

    @classmethod
    def Trapezoid(cls, width=None, bottom_width=None, top_width=None, offset=None):
        return cls(Node('Quadrilateral', {'Width': width, 'Bottom Width': bottom_width, 'Top Width': top_width, 'Offset': offset}, mode='TRAPEZOID')._out)

    @classmethod
    def Kite(cls, width=None, bottom_height=None, top_height=None):
        return cls(Node('Quadrilateral', {'Width': width, 'Bottom Height': bottom_height, 'Top Height': top_height}, mode='KITE')._out)

    @classmethod
    def Points(cls, point_1=None, point_2=None, point_3=None, point_4=None):
        return cls(Node('Quadrilateral', {'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Point 4': point_4}, mode='POINTS')._out)

    # ----- From

    @classmethod
    def FromMesh(cls, mesh):
        return Mesh(mesh).to_curve()

    @classmethod
    def FromEdgePaths(cls, mesh, next_vertex_index=None):
        return Mesh(mesh).points.paths_to_curves(next_vertex_index=next_vertex_index)

    @classmethod
    def FromPoints(cls, points, curve_group_id=None, weight=None):
        return Cloud(points).to_curves(curve_group_id=curve_group_id, weight=weight)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='CURVE')

    @classmethod
    @property
    def tangent(cls):
        return Node('Curve Tangent')._out

    @property
    def length(self):
        return Node('Curve Length', {'Curve': self})._out

    @classmethod
    def endpoint_selection(cls, start_size=None, end_size=None):
        return Node('Endpoint Selection', {'Start Size': start_size, 'End Size': end_size})._out

    # =============================================================================================================================
    # Topology

    @classmethod
    def curve_of_point(cls, point_index=None):
        return Node('Curve of Point', {'Point Index': point_index})

    @classmethod
    def offset_point_in_curve(cls, point_index=None, offset=None):
        return Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset})

    @classmethod
    def points_of_curve(cls, curve_index=None, weights=None, sort_index=None):
        return Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})

    # =============================================================================================================================
    # Methods

    def set_normal(self, mode='MINIMUM_TWIST'):
        # mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')
        self._jump(Node('Set Curve Normal', {'Curve': self, 'Selection': self._self}, mode=mode)._out)

    def set_normal_z_up(self):
        return self.set_normal(mode='Z_UP')

    def set_normal_free(self):
        return self.set_normal(mode='FREE')

    def sample(self, value=None, factor=None, length=None, curve_index=None, all_curves=False):
        # mode in ('FACTOR', 'LENGTH')
        # if factor argument is None, mode is LENGTH, FACTOR otherwise
        mode = 'FACTOR' if length is None else 'LENGTH'
        res = Node('Sample Curve', {'Curves': self, 'Value': value, 'Factor': factor, 'Length': length, 'Curve Index': curve_index},
            data_type=utils.get_data_type(value), mode=mode, use_all_curves=all_curves)._out
        res.position_ = res.node.position
        res.tangent_  = res.node.tangent
        res.normal_   = res.node.normal
        return res

    def sample_factor(self, value=None, factor=None, curve_index=None, all_curves=False):
        return self.sample(value=value, factor=factor, curve_index=curve_index, all_curves=all_curves)

    def sample_length(self, value=None, length=None, curve_index=None, all_curves=False):
        return self.sample(value=value, length=length, curve_index=curve_index, all_curves=all_curves)

    # =============================================================================================================================
    # Operations

    def to_mesh(self, profile_curve=None, fill_caps=None):
        return Mesh.FromCurve(self, profile_curve=profile_curve, fill_caps=fill_caps)

    def to_points(self, count=None, length=None, mode='EVALUATED'):
        return Cloud.FromCurve(curve=self, count=count, length=length, mode='EVALUATED')

    def to_points_evaluated(self):
        return Cloud.FromCurveEvaluated(curve=self)

    def to_points_count(self, count=None):
        return Cloud.FromCurveCount(curve=self, count=count)

    def to_points_length(self, length=None):
        return Cloud.FromCurve(curve=self, length=length)

    def deform_on_surface(self):
        return Curve(Node('Deform Curves on Surface', {'Curves': self})._out)

    # ----- Fill curve

    def fill(self, group_id=None, mode='TRIANGLES'):
        # mode in ('TRIANGLES', 'NGONS')
        return Mesh(Node('Fill Curve', {'Curve': self, 'Group ID': group_id}, mode=mode)._out)

    def fill_triangles(self, group_id=None):
        return self.fill(group_id=group_id, mode='TRIANGLES')

    def fill_ngons(self, group_id=None):
        return self.fill(group_id=group_id, mode='NGONS')

    # ----- Fillet curve

    def fillet(self, radius=None, limit_radius=None, count=None, mode='BEZIER'):
        # mode in ('BEZIER', 'POLY')
        return Curve(Node('Fillet Curve', {'Curve': self, 'Count': count, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)._out)

    def fillet_bezier(self, radius=None, limit_radius=None):
        return self.fillet(radius=radius, limit_radius=limit_radius, mode='BEZIER')

    def fillet_poly(self, count=None, radius=None, limit_radius=None):
        return self.fillet(radius=radius, limit_radius=limit_radius, count=count, mode='POLY')

    # ----- Interpolate curves

    def interpolate(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        curve = Curve(Node('Interpolate Curves', {'Guide Curves': self, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id,
            'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})._out)
        curve.closest_index_  = curve.node.closest_index
        curve.closest_weight_ = curve.node.closest_weight
        return curve

    # ----- Resample

    def resample(self, count=None, length=None):
        # mode in  ('EVALUATED', 'COUNT', 'LENGTH')
        # mode is based on count and length Nonety

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
        # mode in ('FACTOR', 'LENGTH')
        return Curve(Node('Trim Curve', {'Curve': self, 'Selection': self._sel, 'Start': start, 'End': end}, mode=mode)._out)

    def trim_factor(self, start=None, end=None):
        return self.trim(start=start, end=end, mode='FACTOR')

    def trim_length(self, start=None, end=None):
        return self.trim(start=start, end=end, mode='LENGTH')

    # ----- Various

    def reverse(self):
        return Curve(Node('Reverse Curve', {'Curve': self, 'Selection': self._sel})._out)

    def subdivide(self, cuts=None):
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
        return cls(Node('Points', {'Count': count, 'Position': position, 'Radius': radius})._out)

    # ----- Curve to points

    @classmethod
    def FromCurve(cls, curve, count=None, length=None, mode='COUNT'):
        # mode in ('EVALUATED', 'COUNT', 'LENGTH')
        points = Node('Curve to Points', {'Curve': curve, 'Count': count, 'Length': length}, mode=mode)._out
        points.tangent_ = points.node.tangent
        points.normal_ = points.node.normal
        points.rotation_ = points.node.rotation
        return points

    @classmethod
    def FromCurveEvaluated(cls, curve=None):
        return cls.FromCurve(curve=curve, mode='EVALUATED')

    @classmethod
    def FromCurveCount(cls, curve=None, count=None):
        return cls.FromCurve(curve=curve, count=count, mode='COUNT')

    @classmethod
    def FromCurveLength(cls, curve=None, length=None):
        return cls.FromCurve(curve=curve, length=length, mode='LENGTH')

    # ----- Instances to points

    @classmethod
    def FromInstances(cls, instances=None, position=None, radius=None):
        return Cloud(Node('Instances to Points', {'Instances': instances, 'Position': position, 'Radius': radius})._out)

    # ----- Mesh to points

    @classmethod
    def FromVertices(cls, mesh, position=None, radius=None):
        return Mesh(mesh).points.to_points(position=position, radius=radius)

    @classmethod
    def FromFaces(cls, mesh, position=None, radius=None):
        return Mesh(mesh).faces.to_points(position=position, radius=radius)

    @classmethod
    def FromCorners(cls, mesh, position=None, radius=None):
        return Mesh(mesh).corners.to_points(position=position, radius=radius)

    @classmethod
    def FromEdges(cls, mesh, position=None, radius=None):
        return Mesh(mesh).edges.to_points(position=position, radius=radius)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        return self._cache('Domain Size', {'Geometry': self}, component='POINTCLOUD')

    # =============================================================================================================================
    # Methods

    # ----- to curves

    def to_curves(self, curve_group_id=None, weight=None):
        return Curve(Node('Points to Curves', {'Points': self, 'Curve Group ID': curve_group_id, 'Weight': weight})._out)

    # ----- to mesh

    def to_vertices(self):
        return Mesh(Node('Points to Vertices', {'Points': self, 'Selection': self._sel})._out)

    # ----- to volume

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, amount=True):
        # resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        resolution_mode = 'VOXEL_AMOUNT' if amount else 'VOXEL_SIZE'
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
        return cls(Node('Geometry to Instance', {'Geometry': list(geometries)})._out)

    @classmethod
    def FromString(cls, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None,
                overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT'):
        # overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
        # align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
        # align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
        # pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
        node = Node('String to Curves', {'String': string, 'Size': size, 'Character Spacing': character_spacing,
            'Word Spacing': word_spacing, 'Line Spacing': line_spacing,
            'Text Box Width': text_box_width, 'Text Box Height': text_box_height},
            overflow=overflow, align_x=align_x, align_y=align_y, pivot_mode=pivot_mode)
        insts = cls(node._out)
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
        return Node('Realize Instances', {'Geometry': self, 'Selection': self._sel, 'Realize All': realize_all, 'Depth': depth})._out

    def to_points(self, position=None, radius=None):
        return Cloud(Node('Instances to Points', {'Instances': self, 'Selection': self._sel, 'Position': position, 'Radius': radius})._out)

    def on_points(self, points, pick_instance=None, instance_index=None, rotation=None, scale=None):
        if isinstance(points, Geometry):
            if not hasattr(points, 'points'):
                raise NodeError(f"'Instance to Points' node needs a geometry with points, not '{type(points).__name__}'")
            points = points.points

        return points.instance_on(instance=self, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale)

    def translate_instances(self, translation=None, local_space=None):
        return self.insts.translate(translation=translation, local_space=local_space)

    def scale_instances(self, scale=None, center=None, local_space=None):
        self.insts.scale = {'scale': scale, 'center': center, 'local_space': local_space}
        return self

    def rotate_instances(self, rotation=None, pivot_point=None, local_space=None):
        self.insts.rotation = {'rotation': rotation, 'pivot_point': pivot_point, 'local_space': local_space}
        return self

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
        return cls(Node('Volume Cube', {'Density': density, 'Background': background, 'Min': min, 'Max': max,
            'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z})._out)

    @classmethod
    def FromMesh(cls, mesh, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True):
        return Mesh(mesh).to_volume(density=density, voxel_amount=voxel_amount, interior_band_width=interior_band_width, voxel_size=voxel_size, amount=amount)

    @classmethod
    def FromPoints(cls, points, density=None, voxel_size=None, voxel_amount=None, radius=None, amount=True):
        return Cloud(points).to_volume(density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, amount=amount)

    # =============================================================================================================================
    # Methods

    def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, grid=False):
        # mode in ('DENSITY_RANDOM', 'DENSITY_GRID')
        mode = 'DENSITY_GRID' if grid else 'DENSITY_RANDOM'
        return Cloud(Node('Distribute Points in Volume', {'Volume': self, 'Density': density,
            'Seed': seed, 'Spacing': spacing, 'Threshold': threshold}, mode=mode)._out)

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        # resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
        if resolution_mode == 'GRID':
            return self.to_mesh_grid(threshold=threshold, adaptivity=adaptivity)
        elif resolution_mode == 'VOXEL_AMOUNT':
            return self.to_mesh_amount(voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity)
        elif resolution_mode == 'VOXEL_SIZE':
            return self.to_mesh_size(voxel_size=voxel_size, threshold=threshold, adaptivity=adaptivity)

    def to_mesh_grid(self, threshold=None, adaptivity=None):
        # resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
        return Mesh(Node('Volume to Mesh', {'Volume': self, 'Threshold': threshold, 'Adaptivity': adaptivity},
            resolution_mode='GRID')._out)

    def to_mesh_amount(self, voxel_amount=None, threshold=None, adaptivity=None):
        # resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
        return Mesh(Node('Volume to Mesh', {'Volume': self, 'Voxel Amount': voxel_amount, 'Threshold': threshold, 'Adaptivity': adaptivity},
            resolution_mode='VOXEL_AMOUNT')._out)

    def to_mesh_size(self, voxel_size=None, threshold=None, adaptivity=None):
        # resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
        return Mesh(Node('Volume to Mesh', {'Volume': self, 'Voxel Size': voxel_size, 'Threshold': threshold, 'Adaptivity': adaptivity},
            resolution_mode='VOXEL_AMOUNT')._out)
