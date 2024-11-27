"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : geometryclass
----------------------
- Implement geometry data socket

The Geometry base class for type 'GEOMETRY' has specialized children: Mesh, Curve, Cloud, Instances and Volume
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
    - GreasePencil:
        - layers
    - Instances
        - insts
    - Cloud
        - points
    - Volume

The components of a geometry can be separated with the following properties:

``` python
geo = Geometry()
mesh     = geo.mesh        # Node 'Separate Component', socket 'Mesh'
curve    = geo.curve       # Node 'Separate Component', socket 'Curve'
cloud    = geo.point_cloud # Node 'Separate Component', socket 'Point Cloud'
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
- Geometry      : Socket of type 'Geometry'
- Mesh          : Subclass of Geometry specific to Mesh
- Curve         : Subclass of Geometry specific to Curve
- Instances     : Subclass of Geometry specific to Instances
- Cloud         : Subclass of Geometry specific to Cloud Points
- Volume        : Subclass of Geometry specific to Points

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

from inspect import Arguments
import bpy
from bpy.types import Property, PythonConstraint, SmoothModifier

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Tree, Node, Layout
from .socketclass import NodeCache, Socket
from .booleanclass import Boolean
from .floatclass import Float
from .staticclass import nd

# =============================================================================================================================
# =============================================================================================================================
# Interface for Geometry and Domain
# =============================================================================================================================
# =============================================================================================================================


# =============================================================================================================================

class GeoBase:
    """ Base class for Geometry and Domain.

    Implement auto selection mechanism.
    """

    @property
    def _geo_type(self):
        return type(self._geo)

    # =============================================================================================================================
    # Properties

    # ----- Position

    @property
    def position(self):
        """ > Position property

        - getter : node <&Node Position>
        - setter : node <&Node Set Position>

        Returns
        -------
        - Vector
        """
        return Node('Position')._out

    @position.setter
    def position(self, value):
        node = Node('Set Position', {'Geometry': self._geo, 'Selection': self._sel, 'Position': value})
        return self._jump(node._out)

    @property
    def offset(self):
        """ > Offset write only property

        - getter : None
        - setter : <&Node Set Position>

        Returns
        -------
        - Error
        """
        raise NodeError(f"offset is write only property")

    @offset.setter
    def offset(self, value):
        node = Node('Set Position', {'Geometry': self._geo, 'Selection': self._sel, 'Offset': value})
        return self._jump(node._out)

    # ----- ID

    @property
    def id(self):
        """ > Id property

        - getter : <&Node ID>
        - setter : <&Node Set ID>

        Returns
        -------
        - Integer
        """
        return GeoBase.ID

    @id.setter
    def id(self, value):
        node = Node('Set ID', {'Geometry': self._geo, 'Selection': self._sel, 'ID': value})
        return self._jump(node._out)

    # ----- Material

    @property
    def material_index(self):
        """ > Material index property

        - getter : <&Node Material Index>
        - setter : <&Node Set Material Index>

        Returns
        -------
        - Integer
        """
        return Node('Material Index')._out

    @material_index.setter
    def material_index(self, value):
        self._jump(Node('Set Material Index', {'Geometry': self._geo, 'Selection': self._sel, 'Material Index': value})._out)

    @property
    def material(self):
        """ > Material write only property

        - getter : None
        - setter : <&Node Set Material>

        Returns
        -------
        - Error
        """
        raise NodeError(f"material is write only property")

    @material.setter
    def material(self, value):
        self._jump(Node('Set Material', {'Geometry': self._geo, 'Selection': self._sel, 'Material': value})._out)

    @classmethod
    def material_selection(cls, material=None):
        return Node('Material Selection', {'Material': material})._out

    # =============================================================================================================================
    # Methods

    def set_position(self, position=None, offset=None):
        """ > Node <&Node Set Position>

        [&JUMP]

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - offset (Vector) : socket 'Offset' (Offset)

        Returns
        -------
        - Geometry : self
        """
        node = Node('Set Position', {'Geometry': self._geo, 'Selection': self._sel, 'Position': position, 'Offset': offset})._out
        return self._jump(node._out)

    def set_id(self, id=None):
        """ > Node <&Node Set ID>

        [&JUMP]

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (Geometry)
        - selection (Boolean) : socket 'Selection' (Selection)
        - id (Integer) : socket 'ID' (ID)

        Returns
        -------
        - Geometry
        """
        node = Node('Set ID', {'Geometry': self._geo, 'Selection': self._sel, 'ID': id})
        return self._jump(node._out)

    def replace_material(self, old=None, new=None):
        """ > Node <&Node Replace Material>

        [&JUMP]

        Arguments
        ---------
        - old (Material) : socket 'Old' (Old)
        - new (Material) : socket 'New' (New)

        Returns
        -------
        - Geometry : self
        """
        node = Node('Replace Material', {'Geometry': self._geo, 'Old': old, 'New': new})
        return self._jump(node._out)

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


# =============================================================================================================================
# =============================================================================================================================
# Geometry
# =============================================================================================================================
# =============================================================================================================================

class Geometry(Socket, GeoBase):

    SOCKET_TYPE = 'GEOMETRY'

    def __init__(self, value=None, name=None, tip=None):
        """ Socket of type 'GEOMETRY'.

        If value is None, a Group Input socket of type Geometry is created.
        When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

        ``` python
        geometry = Geometry() # Default group input geometry
        geometry = Geometry(name="Mesh") # Input group geometry
        ```

        Arguments
        ---------
        - value (Socket = None) : initial value
        - name (str = None) : Create an Group Input socket with the provided str
        - tip (str = None) : User tip (for Group Input sockets)
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
    # Properties

    @property
    def name(self):
        """ > Name write only property

        Set the geometry name

        ``` python
        geometry.name = 'geo name'
        ```

        - getter : None, write only Property
        - setter : node <&Node Set Geometry Name>

        Returns
        -------
        - Error
        """
        raise NodeError(f"Property 'name' is write only")

    @name.setter
    def name(self, name=None):
        return self.set_name(name)

    def set_name(self, name=None):
        """ > Node <&Node Set Geometry Name>

        [&JUMP]

        Arguments
        ---------
        - name (String) : socket 'Name' (Name)

        Returns
        -------
        - Geometry
        """
        return self._jump(Node('Set Geometry Name', {'Geometry': self, 'Name': name})._out)


    # ====================================================================================================
    # Methods

    # ----- Viewer

    def viewer(self, value=None):
        """ > Node <&Node Viewer>

        Arguments
        ---------
        - value (Socket) : socket

        Returns
        -------
        - Node
        """
        return Node('Viewer', {'Geometry': self, 'Value': value}, data_type=utils.get_data_type(value))

    # ----- Operations

    def set_id(self, id=None):
        """ > Node <&Node Set ID>

        [&JUMP]

        Arguments
        ---------
        - id (Integer) : socket

        Returns
        -------
        - Geometry : self
        """
        return self._jump(Node("Set ID", {'Geometry': self, 'Selection': self._sel, 'ID': id})._out)

    def set_position(self, position=None, offset=None):
        """ > Node <&Node Set Position>

        [&JUMP]

        Arguments
        ---------
        - position (Vector) : socket

        Returns
        -------
        - Geometry : self
        """
        return self._jump(Node("Set Position", {'Geometry': self, 'Selection': self._sel, 'Position': position, 'Offset': offset})._out)

    def set_material(self, material=None):
        """ > Node <&Node Set Material>

        [&JUMP]

        Arguments
        ---------
        - material (Material) : socket

        Returns
        -------
        - Geometry = self
        """
        return self._jump(Node("Set Material", {'Geometry': self, 'Selection': self._sel, 'Material': material})._out)

    def set_shade_smooth(self, shade_smooth=True, edge=False):
        """ > Node <&Node Set Shade Smooth>

        [&JUMP]

        Arguments
        ---------
        - shade_smooth (Boolean) : socket

        Returns
        -------
        - Geometry : self
        """
        return self._jump(Node("Set Shade Smooth", {'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE' if edge else 'FACE')._out)

    # ----- Remove named attribute

    def remove_named_attribute(self, name, exact=True):
        """ > Node <&Node Remove Named Attribute>

        [&JUMP]

        Arguments
        ---------
        - name (String) : socket
        - exact (Boolean) : pattern_mode = 'EXACT' if True else 'WILDCARD'

        Returns
        -------
        - Geometry : self
        """
        return self._jump(Node('Remove Named Attribute', {'Geometry': self, 'Name': name}, pattern_mode = 'EXACT' if exact else 'WILDCARD')._out)

    # ====================================================================================================
    # Sample nodes without domain

    # ----- Index of nearest

    @staticmethod
    def index_of_nearest(position=None, group_id=None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - group_id (Integer) : socket 'Group ID' (Group ID)

        Returns
        -------
        - Integer, [has_neighbor_]
        """

        return Node('Index of Nearest', {'Position': position, 'Group ID': group_id})._out

    # ----- Raycast

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, interpolated=True):
        """ > Node <&Node Raycast>

        [&RETURN_NODE]

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (Attribute)
        - source_position (Vector) : socket 'Source Position' (Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (Ray Length)
        - interpolated (bool) : mapping = 'INTERPOLATED' if True, 'NEAREST' otherwise

        Returns
        -------
        - Node: 'RayCast' node
        """

        data_type = utils.get_data_type(attribute, restrict_to=['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4'])
        node = Node('Raycast', {'Target Geometry': self, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length},
            data_type=utils.get_data_type(attribute), mapping='INTERPOLATED' if interpolated else 'NEAREST')
        return node

    # ====================================================================================================
    # Geometry Operations

    def bake(self, **kwargs):
        """ Node <&Node Bake>

        [&JUMP]

        Returns
        -------
        - Geometry : self
        """

        node = Node('Bake', {'Geometry': self})

        items = node._bnode.bake_items
        for name, value in kwargs.items():
            items.new(utils.get_input_type(value), name)

        return self._jump(node._out)

    @property
    def bounding_box(self):
        """ > Bounding box read only property

        - getter : <&Node Bounding Box>
        - setter : None

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Bounding Box', {'Geometry': self})._out)

    @property
    def convex_hull(self):
        """ > Convex hull read only property

        - getter : <&Node Convex Hull>
        - setter : None

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Convex Hull', {'Geometry': self})._out)

    def merge_by_distance(self, distance=None, mode='ALL'):
        """ > Node <&Node Merge by Distance>

        [&JUMP]

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (Distance)
        - mode (str) : str in ('ALL', 'CONNECTED')

        Returns
        -------
        - Geometry : self
        """
        return self._geo_type(self._node('Merge by Distance', {'Distance': distance}, mode=mode)._out)

    def transform(self, translation=None, rotation=None, scale=None, matrix=None):
        """ > Node <&Node Transform Geometry>

        [&JUMP]

        > [!NOTE]
        > - If **matrix** argument is None, the mode 'COMPONENTS' is set.
        > - If **matrix** argument is not NOne, the mode 'MATRIX' is set and the other arguments are ignored.

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)
        - matrix (Matrix) : socket 'Transform' (Transform)

        Returns
        -------
        - Geometry = self
        """
        if matrix is None:
            return self._jump(Node('Transform Geometry', {'Geometry': self, 'Translation': translation, 'Rotation': rotation, 'Scale': scale}, mode='COMPONENTS')._out)
        else:
            return self._jump(Node('Transform Geometry', {'Geometry': self, 'Transform': matrix}, mode='MATRIX')._out)

    @property
    def separate_components(self):
        """ > Node <&Node Separate Components>

        > See <#mesh>, <#curve>, <#point_cloud>, <#instances> and <#volume> properties

        Returns
        -------
        - Node : 'Separate components node
        """
        return self._cache('Separate Components', {'Geometry': self})

    @property
    def mesh(self):
        """ > Socket 'Mesh' of node <&Node Separate Components>

        Returns
        -------
        - Mesh
        """
        return Mesh(self.separate_components.mesh)

    @property
    def curve(self):
        """ > Socket 'Curve' of node <&Node Separate Components>

        Returns
        -------
        - Curve
        """
        return Curve(self.separate_components.curve)

    @property
    def grease_pencil(self):
        """ > Socket 'Grease Pencil' of node <&Node Separate Components>

        Returns
        -------
        - GreasePencil
        """
        return GreasePencil(self.separate_components.grease_pencil)

    @property
    def point_cloud(self):
        """ > Socket 'Point Cloud' of node <&Node Separate Components>

        Returns
        -------
        - Cloud
        """
        return Cloud(self.separate_components.point_cloud)

    @property
    def volume(self):
        """ > Socket 'Volume' of node <&Node Separate Components>

        Returns
        -------
        - Volume
        """
        return Volume(self.separate_components.volume)

    @property
    def instances(self):
        """ > Socket Instances of node <&Node Separate Components>

        Returns
        -------
        - Instances
        """
        return Instances(self.separate_components.instances)

    @classmethod
    def Join(cls, *geometries):
        """ > Constructor node <&Node Join Geometry>

        Create a new geometry by joining the arguments geometry:

        ``` python
        geo = Geometry.Join(Mesh.Cube(), Curve.Circle())
        ```

        > See also <#join> method

        Arguments
        ---------
        Arguments
        ---------
        - *geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Geometry
        """
        if len(geometries) == 0:
            return cls(Node('Join Geometry')._out)

        ttype = cls
        if cls.__name__ == 'Geometry':
            ttype = type(geometries[0])
            for g in geometries[1:]:
                if not isinstance(g, ttype):
                    ttype = cls
                    break

        return ttype(Node('Join Geometry', {'Geometry': list(geometries)})._out)

    def join(self, *geometries):
        """ > Node <&Node Join Geometry>

        [&JUMP]

        > [!IMPORTANT]
        > 3 possibilities exist to join geometries
        > - Constructur <#Join> : create an new geometry from the input geometries
        > - Operator '+' : create a new geometry from the operands
        > - Method 'join' : join the input geometry to the calling geometry

        ``` python
        a = Mesh.Cube()
        b = Mesh.UVSphere()

        # Constructor Join
        c = Mesh.Join(a, b)

        # Equivalent to
        c = a + b

        # Method join
        # After the call, a is not anymore the cube but the result of the join operation
        a.join(b)

        # Equivalent to
        a += b
        ```

        Arguments
        ---------
        - *geometry (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Geometry : self
        """
        if len(geometries) == 0:
            return self
        return self._jump(Node('Join Geometry', {'Geometry': [self] + list(geometries)})._out)

    def __add__(self, other):
        if isinstance(other, tuple):
            return type(self).Join(self, *other)

        elif isinstance(other, type(self)):
            return type(self).Join(self, other)

        else:
            return Geometry.Join(self, other)


    # ====================================================================================================
    # Operations

    def to_instance(self, *geometries):
        """ > Node <&Node Geometry to Instance>

        [&NO_JUMP]

        Arguments
        ---------
        - geometries (Geometry) : socket 'Geometry' (Geometry)

        Returns
        -------
        - Instances
        """
        return Instances.FromGeometry([self] + list(geometries))


# =============================================================================================================================
# =============================================================================================================================
# Domain
# =============================================================================================================================
# =============================================================================================================================

class Domain(GeoBase, NodeCache):

    DOMAIN_NAME = None

    def __init__(self, geometry):
        """ > Base class for geometry domains

        A domain stores the default value to be set in node needing a **domain** parameter
        such as 'Store Named Attibute.

        All nodes requiring a domain parameter are implemented as domain method

        ``` python
        cube = Mesh.Cube()
        cube.faces.store_named_attribute() # doamin = 'FACE'
        ```

        > [!IMPORTANT]
        > Domains are never instantiated directly but created by geometries.

        > See: <!Vertex>, <!Face>, <!Edge>, <!Corner>, <!SplinePoint>, <!Spline>, <!CloudPoint>, <!Instance>

        Properties:
        - _geo (Geometry) : the geometry the domain belongs to
        """
        self._geo  = geometry
        self._cache_reset()

    def __str__(self):
        return f"<Domain {self.DOMAIN_NAME} of {self._geo}>"

    # ----- Jump

    def _jump(self, socket):
        return self._geo._jump(socket)

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
        return self.restrict_domain(['POINT', 'FACE', 'EDGE', 'CURVE', 'INSTANCE', 'LAYER'])

    def plural_domain(self, domains=None, title=""):
        PLURAL = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES', 'CORNER': 'CORNERS', 'SPLINE': 'SPLINES', 'CURVE': 'SPLINES', 'LAYER': 'LAYERS'}
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
    # ForEachElement loop

    def for_each(self, sockets={}, **kwargs):
        """ > Create a <!ForEachElement> zone on this domain

        The <!ForEachElement> zone is initialized with the domain, its geometry and
        the selection:

        ``` python
        ico = Mesh.IcoSphere(subdivisions=2)
        with ico.faces[(nd.index % 2).equal(0)].for_each(position=nd.position) as feel:
            face = Mesh(feel.element)
            face.points.offset = feel.position*1.1
            feel.generated.geometry = face

        feel.generated.geometry.out()
        ```

        Arguments
        ---------
        - sockets (dict) : input sockets
        - kwargs : input sockets

        Returns
        -------
        - ForEachElement zone
        """

        from geonodes import ForEachElement

        return ForEachElement(geometry=self._geo, selection=self._sel, domain=self.DOMAIN_NAME, sockets=sockets, **kwargs)

    # ====================================================================================================
    # Properties

    # ====================================================================================================
    # Methods

    # ----- Viewer

    def viewer(self, value=None):
        """ > Node <&Node Viewer>

        Arguments
        ---------
        - value (Socket = None) : value to view
        """
        return self._node('Viewer', {'Value': value}, data_type=utils.get_data_type(value))

    # ----- Attribute statistic

    def attribute_statistic(self, attribute=None):
        """ > Node <&Node Attribute Statistic>

        [&RETURN_NODE]

        Arguments
        ---------
        - attribute (Socket = None) : attribute to compute statistic

        Returns
        -------
        - Node : 'Attribute Statistic Node'
        """
        data_type = utils.get_data_type(attribute, ['FLOAT_VECTOR', 'VECTOR', 'ROTATION', 'COLOR'], 'FLOAT')

        return self._node('Attribute Statistic', {'Attribute': attribute}, data_type=data_type, use_cache=False)

    # ----- Capture attribute

    def capture_attribute(self, **attributes):
        """ > Node <&Node Capture Attribute>

        [&JUMP]
        [&RETURN_NODE]

        > You can use two short names:
        > <#capture> : to capture only one attribute
        > <#capture> : same as **capture_attribute** to capture several named attributes

        ``` python
        with GeoNodes("Capture Attribute"):
            # Capture attributes
            node = mesh.points.capture_attribute(attr1 = attr1, attr2=attr2)
            captured_attr1 = node.attr1
            captured_attr2 = node.attr2

            # Capture one attribute
            captured_attr3 = mesh.points.capture(attr3)
        ```

        Arguments
        ---------
        - **attributes (Sockets): named attributes to capture

        Returns
        -------
        - Node
        """
        if len(attributes) == 0:
            return self

        node = self._node('Capture Attribute')
        node._set_items(**attributes)
        self._jump(node._out)
        return node

    def captures(self, **attributes):
        """ > Node <&Node Capture Attribute>

        [&JUMP]
        [&RETURN_NODE]

        > Short name for <#capture_attribute>

        ``` python
        with GeoNodes("Capture Attribute"):
            # Capture attributes
            node = mesh.points.captures(attr1 = attr1, attr2=attr2)
            captured_attr1 = node.attr1
            captured_attr2 = node.attr2

            # Capture one attribute
            captured_attr3 = mesh.points.capture(attr3)
        ```

        Arguments
        ---------
        - **attributes (Sockets): named attributes to capture

        Returns
        -------
        - Node
        """
        return self.capture_attribute(**attributes)

    def capture(self, attribute):
        """ > Node <&Node Capture Attribute>

        [&JUMP]

        > Short name for <#capture_attribute>

        ``` python
        with GeoNodes("Capture Attribute"):
            captured_attr = mesh.points.capture(attr)

            # If more than one attribute is to be captured
            node = mesh.points.captures(attr1 = attr1, attr2=attr2)
            captured_attr1 = node.attr1
            captured_attr2 = node.attr2
        ```

        Arguments
        ---------
        - attribute (Socket): the single attribute to capture

        Returns
        -------
        - Socket
        """
        return self.capture_attribute(attribute=attribute).attribute

    # ----- Store named attribute

    def store_named_attribute(self, name, value=None):
        """ > Node <&Node Store Named Attribute>

        [&JUMP]

        > You can use short name <#store>

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        > [!NOTE]
        > Use constructor method <!Attribute#NamedAttribute> to read stored attributes

        ``` python
        mesh = Mesh.Cube()
        mesh.points.store_named_attribute("An Integer", 123)
        i = Integer.NamedAttribute("An Integer")
        ```

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

        return self._jump(node._out)

    def store(self, name, value=None):
        """ > Node <&Node Store Named Attribute>

        [&JUMP]

        > Short name of <#store_named_attribute>

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        > [!NOTE]
        > Use constructor method <!Attribute#Named> to read stored attributes

        ``` python
        mesh = Mesh.Cube()
        mesh.points.store("An Integer", 123)
        i = Integer.Named("An Integer")
        ```

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

        return self._jump(node._out)

    # ====================================================================================================
    # Sample nodes with domain

    def proximity(self, group_id=None, sample_position=None, sample_group_id=None):
        """ > Node <&Node Geometry Proximity>

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sample_position (Vector) : socket 'Sample Position' (Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (Sample Group ID)

        Returns
        -------
        - Vector
        """

        target = self.restrict_domain(['POINT', 'EDGE', 'FACE'], 'Proximity')
        return Node('Geometry Proximity', {'Geometry': self._geo, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=self.DOMAIN_NAME + 'S')._out

    def sample_index(self, value=None, index=0, clamp=False):
        """ > Node <&Node Sample Index>

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - index (Integer) : socket 'Index' (Index)
        - clamp (bool): Node.clamp

        Returns
        -------
        - Vector
        """

        return self._node('Sample Index', {'Value': value, 'Index': index}, clamp=clamp, data_type=utils.get_data_type(value))._out

    def sample_nearest(self, sample_position=None):
        """ > Node <&Node Sample Nearest>

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
        """ > Node <&Node Delete Geometry>

        [&JUMP]

        > You can use short name <#delete>

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - mode (str): Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry : self
        """
        self.exclude_corner('delete_geometry')
        return self._jump(self._node('Delete Geometry', mode=mode)._out)

    def delete(self, mode='ALL'):
        """ > Node <&Node Delete Geometry>

        [&JUMP]

        > Short name for <#delete_geometry>

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - mode (str): Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry : self
        """
        return self.delete_geometry(mode=mode)

    def delete_all(self):
        """ > Node <&Node Delete Geometry>, mode = 'ALL'

        [&JUMP]

        Arguments
        ---------
        - mode (str): Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry : self
        """
        return self.delete_geometry(mode='ALL')

    def delete_faces(self):
        """ > Node <&Node Delete Geometry>, mode = 'ONLY_FACE'

        [&JUMP]

        Returns
        -------
        - Geometry : self
        """
        return self.delete_geometry(mode='ONLY_FACE')

    def delete_edges_and_faces(self):
        """ > Node <&Node Delete Geometry>, mode = 'EDGE_FACE'

        [&JUMP]

        Returns
        -------
        - Geometry : self
        """
        return self.delete_geometry(mode='EDGE_FACE')

    def duplicate_elements(self, amount=1):
        """ > Node <&Node Duplicate Elements>

        [&JUMP]

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (Amount)

        Returns
        -------
        - Geometry : self
        """

        self.exclude_corner('duplicate_elements')
        domain = self.domain_name(rename={'CURVE': 'SPLINE'})
        return self._jump(Node('Duplicate Elements', {'Geometry': self._geo, 'Selection': self._sel, 'Amount': amount}, domain=domain)._out)

    def sort_elements(self, group_id=None, sort_weight=None):
        """ > Node <&Node Sort Elements>

        [&JUMP]

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (Sort Weight)

        Returns
        -------
        - Geometry = self
        """
        self.exclude_corner('sort_elements')
        return self._jump(self._node('Sort Elements', {'Group ID': group_id, 'Sort Weight': sort_weight})._out)

    def separate(self):
        """ > Node <&Node Separate Geometry>

        [&NO_JUMP]

        > [!NOTE]
        > Use **peer socket** convention to get the inverted socket

        ``` python
        mesh = Mesh.Cube()
        selected = mesh.points.separate()
        inverted = selected.inverted_
        ```

        Returns
        -------
        - Geometry
        """

        self.exclude_corner('separate')
        return self._geo_type(self._node('Separate Geometry')._out)

    def split_to_instances(self, group_id=None):
        """ > Node <&Node Split to Instances>

        [&NO_JUMP]

        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (Group ID)

        Returns
        -------
        - Instances
        """

        self.exclude_corner('split_to_instances')
        return Instances(self._node('Split to Instances', {'Group ID': group_id})._out)

    # ----- Mesh conversion to points

    def to_points(self, position=None, radius=None):
        """ > Node <&Node Mesh to Points>

        [&NO_JUMP]

        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

        Arguments
        ---------
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """

        mode = self.plural_domain(['POINT', 'EDGE', 'FACE', 'CORNER'], 'Mesh to Point')
        return Cloud(Node('Mesh to Points', {'Mesh': self._geo, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode=mode)._out)

    # ----- Extrusion

    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ > Node <&Node Extrude Mesh>

        [&JUMP]

        - mode (str): Node.mode in ('VERTICES', 'EDGES', 'FACES')

        ``` python
        with GeoNodes("Extrusion"):
            cube = Mesh.Cube()

            cube.faces.extrude(nd.normal, .5)
            cube.faces[cube.top_].extrude(offset_scale=0)

            # Next cube extrusion will change top_
            top = cube.top_

            cube.faces[top].scale(scale=.8, uniform=False)
            cube.faces[top].scale(scale=.6, uniform=True)
            cube.faces[top].extrude(offset_scale=.5)
            cube.faces[cube.top_].flip()

            cube.out()
        ```

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (Offset)
        - offset_scale (Float) : socket 'Offset Scale' (Offset Scale)
        - individual (Boolean) : socket 'Individual' (Individual)

        Returns
        -------
        - Geometry : self
        """

        mode = self.plural_domain(['POINT', 'EDGE', 'FACE'], 'Extrude Mesh')
        node = Node('Extrude Mesh', {'Mesh': self._geo, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale, 'Individual': individual}, mode = mode)
        return self._jump(node._out)

    # ----- Field

    def accumulate_field(self, value=None, group_id=None, ):
        """ > Node <&Node Accumulate Field>

        [&RETURN_NODE]

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - group_id (Integer) : socket 'Group ID' (Group Index)

        Returns
        -------
        - Node : 'Accumulate Field'
        """
        data_type = utils.get_data_type(value, ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'))
        return Node('Accumulate Field', {'Value': value, 'Group ID': group_id}, data_type=data_type, domain=self.DOMAIN_NAME)

    def evaluate_at_index(self, index=None, value=None):
        """ > Node <&Node Evaluate at Index>

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - index (Integer) : socket 'Index' (Index)
        - value (Float) : socket 'Value' (Value)

        Returns
        -------
        - Socket
        """
        data_type = utils.get_data_type(value)
        return Node('Evaluate at Index', {'Index': index, 'Value': value}, data_type=data_type, domain=self.DOMAIN_NAME)._out

    def evaluate_on_domain(self, value=None):
        """ > Node <&Node Evaluate on Domain>

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - domain (str): Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)

        Returns
        -------
        - Socket
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
        """ > Socket 'Point Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.point_count

    # ----- Instance on points

    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Node <&Node Instance on Points>

        [&NO_JUMP]

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

        return Instances(Node('Instance on Points', {'Points': self._geo, 'Selection': self._sel,
                'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index,
                'Rotation': rotation, 'Scale': scale})._out)

class Vertex(Point):

    """ > Point domain of a <!Mesh>
    """

    # ----- Vertex neighbors

    @property
    def neighbors(self):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        - Node : 'Vertex Neighbors' node
        """
        return self._cache('Vertex Neighbors')

    @property
    def neighbors_vertex_count(self):
        """ > Socket 'Vertex Count' of node <&Node Vertex Neighbors>

        Returns
        -------
        - Integer
        """
        return self.neighbors.vertex_count

    @property
    def neighbors_face_count(self):
        """ > Socket 'Face Count' of node <&Node Vertex Neighbors>

        Returns
        -------
        - Integer
        """
        return self.neighbors.face_count

    # ----- Edge paths to selection

    def paths_to_selection(self, next_vertex_index):
        """ > Node <&Node Edge Paths to Selection>

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
        """ > Node <&Node Edge Paths to Curves>

        [&NO_JUMP]

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
        """ > Node <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (Vertex Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer
        """

        return Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out

    @classmethod
    def corner_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (Vertex Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer
        """
        return Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})._out

class SplinePoint(Point):
    """ > Point domain of a <!Curve>

    Methods of **SplinePoint** class are nodes which accept 'POINT' domain.

    In addition, the nodes <*Node Curve of Point> and <*Offset Point in Curve> are implemented
    in methods <#curve_index>, <#index_in_curve> and <#offset_in_curve>.
    """

    # ----- Handle positions

    @classmethod
    def handle_positions(cls, relative=None):
        """ > Node <&Node Curve Handle Positions>

        Arguments
        ---------
        - relative (Boolean) : socket 'Relative' (Relative)

        Returns
        -------
        - Node : 'Curve Handle Positions' node
        """

        return Node('Curve Handle Positions', {'Relative': relative})

    def set_handle_positions(self, position=None, offset=None, mode=None):
        """ > Node <&Node Set Handle Positions>

        [&JUMP]

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
        - Curve : self
        """
        return self._jump(Node('Set Handle Positions', {'Curve': self._geo, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode=mode)._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Handle position properties

    @property
    def left_handle_position(self):
        """ > Left handle property

        - getter : socket 'Left' of node <&Node Handle Positions>
        - setter : node <&Node Set Handle Positions>

        Returns
        -------
        - Vector
        """
        return self.handle_positions(relative=False).left

    @left_handle_position.setter
    def left_handle_position(self, value):
        self.set_handle_positions(position=value, mode='LEFT')

    @property
    def right_handle_position(self):
        """ > Right handle position property

        - getter : socket 'Right' of node <&Node Handle Positions>
        - setter : node <&Node Set Handle Positions>

        Returns
        -------
        - Vector
        """
        return self.handle_positions(relative=False).right

    @right_handle_position.setter
    def right_handle_position(self, value):
        self.set_handle_positions(position=value, mode='RIGHT')

    # Offset

    @property
    def left_handle_offset(self):
        """ > Left handle offset property

        - getter : socket 'Left' of node <&Node Handle Positions>, relative
        - setter : node <&Node Set Handle Positions>

        Returns
        -------
        - Vector
        """
        return self.handle_positions(relative=True).left

    @left_handle_offset.setter
    def left_handle_offset(self, value):
        self.set_handle_positions(offset=value, mode='LEFT')

    @property
    def right_handle_offset(self):
        """ > Right handle offset property

        - getter : socket 'Right' of node <&Node Handle Positions>, relative
        - setter : node <&Node Set Handle Positions>

        Returns
        -------
        - Vector
        """
        return self.handle_positions(relative=True).right

    @right_handle_offset.setter
    def right_handle_offset(self, value):
        self.set_handle_positions(offset=value, mode='RIGHT')

    # ----- Handle type

    @classmethod
    def handle_type_selection(cls, left=True, right=True, handle_type='AUTO'):
        """ > Node <&Node Handle Type Selection>

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
        """ > Node <&Node Set Handle Type>

        [&JUMP]

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
        - Curve : self
        """

        mode = set()
        if left:
            mode.add('LEFT')
        if right:
            mode.add('RIGHT')
        return self._jump(Node('Set Handle Type', {'Curve': self._geo, 'Selection': self._sel}, mode=mode, handle_type=handle_type)._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Handle types as enum in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

    # ----- Left and Right

    @property
    def handle_type(self):
        """ > Handle type write only property

        Set the curve handle type

        ``` python
        curve.handle_type = 'FREE'
        ```

        - getter : None, write only Property
        - setter : node <&Node Set Handle Type>

        Returns
        -------
        - Error
        """
        raise NodeError(f"Property 'handle_type' is write only")

    @handle_type.setter
    def handle_type(self, value):
        self.set_handle_type(left=True, right=True, handle_type=value)

    # ----- Left only

    @property
    def left_handle_type(self):
        """ > Left handle type write only property

        Set the curve handle type

        - getter : None, write only Property
        - setter : node <&Node Set Handle Type>

        Returns
        -------
        - Error
        """
        raise NodeError(f"Property 'left_handle_type' is write only")

    @left_handle_type.setter
    def left_handle_type(self, value):
        self.set_handle_type(left=True, right=False, handle_type=value)

    # ----- Right only

    @property
    def right_handle_type(self):
        """ > Right handle type write only property

        Set the curve handle type

        - getter : None, write only Property
        - setter : node <&Node Set Handle Type>

        Returns
        -------
        - Error
        """
        raise NodeError(f"Property 'right_handle_type' is write only")

    @right_handle_type.setter
    def right_handle_type(self, value):
        self.set_handle_type(left=False, right=True, handle_type=value)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Left and Right Handle types as boolean properties

    @property
    def handle_auto(self):
        """ > Handle auto property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'AUTO'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=True, handle_type='AUTO')

    @handle_auto.setter
    def handle_auto(self, value):
        self.set_handle_type(left=True, right=True, handle_type='AUTO')

    @property
    def handle_free(self):
        """ > Handle free property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'FREE'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=True, handle_type='FREE')

    @handle_free.setter
    def handle_free(self, value):
        self.set_handle_type(left=True, right=True, handle_type='FREE')

    @property
    def handle_vector(self):
        """ > Handle vector property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'VECTOR'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=True, handle_type='VECTOR')

    @handle_vector.setter
    def handle_vector(self, value):
        self.set_handle_type(left=True, right=True, handle_type='VECTOR')

    @property
    def handle_align(self):
        """ > Handle align property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'ALIGN'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=True, handle_type='ALIGN')

    @handle_align.setter
    def handle_align(self, value):
        self.set_handle_type(left=True, right=True, handle_type='ALIGN')

    # -----------------------------------------------------------------------------------------------------------------------------
    # Left Handle types as boolean properties

    @property
    def left_handle_auto(self):
        """ > Left handle auto property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'AUTO'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=False, handle_type='AUTO')

    @left_handle_auto.setter
    def left_handle_auto(self, value):
        self.set_handle_type(left=True, right=False, handle_type='AUTO')

    @property
    def left_handle_free(self):
        """ > Left handle free property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'FREE'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=False, handle_type='FREE')

    @left_handle_free.setter
    def left_handle_free(self, value):
        self.set_handle_type(left=True, right=False, handle_type='FREE')

    @property
    def left_handle_vector(self):
        """ > Left handle vector property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'VECTOR'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=False, handle_type='VECTOR')

    @left_handle_vector.setter
    def left_handle_vector(self, value):
        self.set_handle_type(left=True, right=False, handle_type='VECTOR')

    @property
    def left_handle_align(self):
        """ > Left handle auto property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'ALIGN'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=True, right=False, handle_type='ALIGN')

    @left_handle_align.setter
    def left_handle_align(self, value):
        self.set_handle_type(left=True, right=False, handle_type='ALIGN')

    # -----------------------------------------------------------------------------------------------------------------------------
    # Right Handle types as boolean properties

    @property
    def right_handle_auto(self):
        """ > Right handle auto property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'AUTO'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=False, right=True, handle_type='AUTO')

    @right_handle_auto.setter
    def right_handle_auto(self, value):
        self.set_handle_type(left=False, right=True, handle_type='AUTO')

    @property
    def right_handle_free(self):
        """ > Right handle free property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'FREE'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=False, right=True, handle_type='FREE')

    @right_handle_free.setter
    def right_handle_free(self, value):
        self.set_handle_type(left=False, right=True, handle_type='FREE')

    @property
    def right_handle_vector(self):
        """ > Right handle vector property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'VECTOR'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=False, right=True, handle_type='VECTOR')

    @right_handle_vector.setter
    def right_handle_vector(self, value):
        self.set_handle_type(left=False, right=True, handle_type='VECTOR')

    @property
    def right_handle_align(self):
        """ > Right handle align property

        - getter : node <&Node Handle Type Selection>
        - setter : node <&Node Set Handle Type>, **handle_type** = 'ALIGN'

        Returns
        -------
        - Boolean
        """
        return self.handle_type_selection(left=False, right=True, handle_type='ALIGN')

    @right_handle_align.setter
    def right_handle_align(self, value):
        self.set_handle_type(left=False, right=True, handle_type='ALIGN')

    # ----- Topology

    def curve_index(self, point_index=None):
        """ > Socket 'Curve Index' of node <&Curve of Point>

        Arguments
        ---------
        - point_index (Integer = None) : point index

        Returns
        -------
        - Integer
        """
        return Node('Curve of Point', {'Point Index': point_index}).curve_index

    def index_in_curve(self, point_index=None):
        """ > Socket 'Index in Curve' of node <&Curve of Point>

        Arguments
        ---------
        - point_index (Integer = None) : point index

        Returns
        -------
        - Integer
        """
        return Node('Curve of Point', {'Point Index': point_index}).index_in_curve

    def offset_in_curve(self, point_index=None, offset=None):
        """ > Socket 'Point Index' of node <&Offset Point in Curve>

        Arguments
        ---------
        - index (Integer = None) : point index

        Returns
        -------
        - Integer : spline index
        """
        return Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset}).point_index


class CloudPoint(Point):
    """ > Point domain of a <!Cloud>
    """

    # ----- Radius

    @property
    def radius(self):
        """ > Radius property

        - getter : node <&Node Radius>
        - setter : node <&Node Set Point Radius>

        Returns
        -------
        - Float
        """
        return Node('Radius')._out

    @radius.setter
    def radius(self, value):
        self._jump(Node('Set Point Radius', {'Points': self._geo, 'Selection': self._sel, 'Radius': value})._out)


# =============================================================================================================================
# =============================================================================================================================
# Face Domain
# =============================================================================================================================
# =============================================================================================================================

class Face(Domain):
    """ > Face domain of a <!Mesh>
    """

    DOMAIN_NAME = 'FACE'

    @property
    def count(self):
        """ > Socket 'Face Count' of node <&Node Domain Size>

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
        """ > Smooth property

        - getter : node <&Node Is Face Smooth>
        - setter : node <&Node Set Shade Smooth>

        Returns
        -------
        - Boolean
        """
        return Node('Is Face Smooth')._out

    @smooth.setter
    def smooth(self, value):
        self._jump(Node('Set Shade Smooth', {'Geometry': self._geo, 'Selection': self._sel, 'Shade Smooth': value}, domain='FACE')._out)

    @property
    def area(self):
        """ > Area read only property

        - getter : <&Node Face Area>
        - setter : None

        Returns
        -------
        - Float
        """
        return Node('Face Area')._out

    def is_planar(self, threshold=None):
        """ > Node <&Node Is Face Planar>

        Arguments
        ---------
        - threshold (Float) : socket 'Threshold' (Threshold)

        Returns
        -------
        - Boolean
        """
        return Node('Is Face Planar', {'Threshold': threshold})._out

    def group_boundaries(self, face_group_id=None):
        """ > Node <&Node Face Group Boundaries>

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
        """ > Node <&Node Face Neighbors>

        Returns
        -------
        - Node : node 'Face Neighbors'
        """
        return self._cache('Face Neighbors')

    @property
    def neighbors_vertex_count(self):
        """ > Socket 'Vertex Count' of node <&Node Face Neighbors>

        Returns
        -------
        - Integer
        """
        return self.neighbors.vertex_count

    @property
    def neighbors_face_count(self):
        """ > Socket 'Face Count' of node <&Node Face Neighbors>

        Returns
        -------
        - Integer
        """
        return self.neighbors.face_count

    # ----- Flip

    def flip(self):
        """ > Node <&Node Flip Faces>

        [&JUMP]

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Flip Faces', {'Mesh': self._geo, 'Selection': self._sel})._out)

    # ----- Scale

    def scale(self, scale=None, center=None, uniform=True):
        """ > Node <&Node Scale Elements>

        [&JUMP]

        - domain (str): Node.domain in ('FACE', 'EDGE')
        - scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - unifom (bool=True) : scale_mode = 'UNIFORM' (True) or 'SINGLE_AXIS' (False)

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Scale Elements', {'Geometry': self._geo, 'Selection': self._sel, 'Scale': scale, 'Center': center},
            domain='FACE', scale_mode = 'UNIFORM' if uniform else 'SINGLE_AXIS')._out)

    # ----- Topology

    @classmethod
    def corner_index(cls, face_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Face>

        Arguments
        ---------
        - face_index (Integer) : socket 'Face Index' (Face Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer
        """
        return Node('Corners of Face', {'Face Index': face_index, 'Weights': weights, 'Sort Index': sort_index})._out

    # ----- Distribute

    def distribute_points(self, density=None, distance_min=None, density_max=None, density_factor=None, seed=None):
        """ > Node <&Node Distribute Points on Faces>

        [&NO_JUMP]

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
        - Cloud
        """
        return self._geo[self._sel].distribute_points_on_faces(density=density, distance_min=distance_min, density_max=density_max,
            density_factor=density_factor, seed=seed)



# =============================================================================================================================
# =============================================================================================================================
# Edge Domain
# =============================================================================================================================
# =============================================================================================================================

class Edge(Domain):
    """ > Edge domain of a <!Mesh>
    """

    DOMAIN_NAME = 'EDGE'

    @property
    def count(self):
        """ > Socket 'Edge Count' of node <&Node Domain Size>

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
        """ > Node <&Node Edge Angle>

        > [!IMPORTANT]
        > This method return the node, use <#unsigned_angle> and <#signed_angle> to
        > get directly the sockets

        Returns
        -------
        - Node
        """
        return self._cache('Edge Angle')

    @property
    def unsigned_angle(self):
        """ > Socket 'Unsigned Angle' of node <&Node Edge Angle>

        Returns
        -------
        - Float
        """
        return self.angle.unsigned_angle

    @property
    def signed_angle(self):
        """ > Socket 'Signed Angle' of node <&Node Edge Angle>

        Returns
        -------
        - Float
        """
        return self.angle.signed_angle

    # ----- Neighbors

    @property
    def neighbors(self):
        """ > Neighbors read only property

        - getter : <&Node Edge Neighbors>
        - setter : None

        Returns
        -------
        - Integer
        """
        return Node('Edge Neighbors')._out

    # ----- Edge vertices

    @property
    def vertices(self):
        """ > Node <&Node Edge Vertices>

        [&RETURN_NODE]

        Returns
        -------
        - Node : Node 'Edge Vertices'
        """
        return self._cache('Edge Vertices')

    @property
    def vertex_index_1(self):
        """ > Socket 'Vertex Index 1' of node <&Node Edge Vertices>

        Returns
        -------
        - Integer
        """
        return self.vertices.vertex_index_1

    @property
    def vertex_index_2(self):
        """ > Socket 'Vertex Index 2' of node <&Node Edge Vertices>

        Returns
        -------
        - Integer
        """
        return self.vertices.vertex_index_2

    @property
    def position_1(self):
        """ > Socket 'Position 1' of node <&Node Edge Vertices>

        Returns
        -------
        - Vector
        """
        return self.vertices.position_1

    @property
    def position_2(self):
        """ > Socket 'Position 2' of node <&Node Edge Vertices>

        Returns
        -------
        - Vector
        """
        return self.vertices.position_2

    # ----- Smooth

    @property
    def smooth(self):
        """ > Smooth property

        - getter : node <&Node Is Edge Smooth>
        - setter : node <&Node Set Shade Smooth>

        Returns
        -------
        - Boolean
        """
        return Node('Is Edge Smooth')._out

    @smooth.setter
    def smooth(self, value):
        self._jump(Node('Set Shade Smooth', {'Geometry': self._geo, 'Selection': self._sel, 'Shade Smooth': value}, domain='EDGE')._out)

    # ----- Shortest Edge Paths

    def shortest_paths(self, edge_cost=None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (Edge Cost)

        Returns
        -------
        - Integer
        """

        return Node('Shortest Edge Paths', {'End Vertex': self._sel, 'Edge Cost': edge_cost})._out

    # ----- To face groups

    @property
    def to_face_groups(self):
        """ > Node <&Node Edges to Face Groups>

        Returns
        -------
        - Integer
        """
        return Node('Edges to Face Groups', {'Boundary Edges': self._sel})._out

    # ----- Split

    def split(self):
        """ > Node <&Node Split Edges>

        [&JUMP]

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Split Edges', {'Mesh': self._geo, 'Selection': self._sel})._out)

    # ----- Scale

    def scale(self, scale=None, center=None, uniform=True):
        """ > Node <&Node Scale Elements>

        [&JUMP]

        - domain (str): Node.domain in ('FACE', 'EDGE')
        - scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - unifom (bool=True) : scale_mode = 'UNIFORM' (True) or 'SINGLE_AXIS' (False)

        Returns
        -------
        - Mesh : self
        """
        node = Node('Scale Elements', {'Geometry': self._geo, 'Selection': self._sel, 'Scale': scale, 'Center': center},
            domain='EDGE', scale_mode = 'UNIFORM' if uniform else 'SINGLE_AXIS')
        return self._jump(node._out)

    # ----- Topology

    @classmethod
    def corner_index(cls, edge_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (Edge Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer
        """
        return Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})._out

    # ----- Edge paths to curves

    def paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Curves>

        [&NO_JUMP]

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
    """ > Corner domain of a <!Mesh>
    """

    DOMAIN_NAME = 'CORNER'

    @property
    def count(self):
        """ > Socket 'Corner Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.face_corner_count

    # ----- Topology

    @classmethod
    def next_edge_index(cls, corner_index=None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Integer
        """

        return Node('Edges of Corner', {'Corner Index': corner_index})._out

    @classmethod
    def face_index(cls, corner_index=None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (Corner Index)

        Returns
        -------
        - Integer
        """
        return Node('Face of Corner', {'Corner Index': corner_index})._out

    @classmethod
    def offset_in_face(cls, corner_index=None, offset=None):
        """ > Node <&Node Offset Corner in Face>

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
        """ > Node <&Node Vertex of Corner>

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
    """ > Curve, or Spline, domain of a <!Curve>

    Methods of **Spline** class are nodes which accept a SPLINE or CURVE domain.

    In addition, the node <*Node Points of Curve> is implemented as method <#points>.
    """

    DOMAIN_NAME = 'CURVE'

    @property
    def count(self):
        """ > Socket 'Spline Count' of node <&Node Domain Size>

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
        """ > Is cyclic property

        - getter : node <&Node Is Spline Cyclic>
        - setter : node <&Node Set Spline Cyclic>

        Returns
        -------
        - Boolean
        """
        return Node('Is Spline Cyclic')._out

    @is_cyclic.setter
    def is_cyclic(self, value):
        return self._jump(Node('Set Spline Cyclic', {'Geometry': self._geo, 'Selection': self._sel, 'Cyclic': value})._out)

    # ----- Resolution

    @property
    def resolution(self):
        """ > Resolution property

        - getter : node <&Node Spline Resolution>
        - setter : node <&Node Set Spline Resolution>

        Returns
        -------
        - Integer
        """
        return Node('Spline Resolution')._out

    @resolution.setter
    def resolution(self, value=None):
        self._jump(Node('Set Spline Resolution', {'Geometry': self._geo, 'Resolution': value})._out)

    # ----- Spline type

    @property
    def type(self):
        """ > Type wite only property

        > [!Note]
        > Write only property

        - getter : None, write only property
        - setter : node <&Node Set Spline Type>, value in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

        Returns
        -------
        - Error
        """
        raise NodeError(f"Curve.spline_type is write only.")

    @type.setter
    def type(self, value):
        self._jump(Node('Set Spline Type', {'Curve': self._geo, 'Selection': self._sel}, spline_type=value)._out)

    # ----- Read only

    @property
    def parameter(self):
        """ > Node <&Node Spline Parameter>

        ``` python
        factor = curve.parameter.factor
        length = curve.parameter.length
        index = curve.parameter.index
        ```

        Returns
        -------
        - Node : node 'Spline Parameter'
        """
        return self._cache('Spline Parameter')

    @classmethod
    @property
    def length(cls):
        """ > Socket 'Length' of node <&Node Spline Length>

        Returns
        -------
        - Float
        """
        return Node('Spline Length')._out

    @classmethod
    @property
    def point_count(cls):
        """ > Socket 'Point Count' of Node <&Node Spline Length>

        Returns
        -------
        - Integer
        """
        return Node('Spline Length').point_count

    # ----- Topology

    def points(self, curve_index=None, weights=None, sort_index=None):
        """ > Socket 'Point Index' of node <&Points of curve>

        Arguments
        ---------
        - curve_index (Integer = None) : socket 'Curve Index'
        - weights (Float = None) : socket 'Weights'
        - sort_index (Integer = None) : socket 'Sort Index'

        Returns
        -------
        - Integer
        """
        return Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index}).point_index


# =============================================================================================================================
# =============================================================================================================================
# Instance Domain
# =============================================================================================================================
# =============================================================================================================================

class Instance(Domain):
    """ > Instance domain of <!Instances>

    > [!NOTE]
    > The geometry has only one domain sharing the same name:
    > - <!Instances> : name of geometry class
    > - **Instance** : name of domain class
    > - <!Instances#insts> : name of the domain property of class <!Instances>
    """

    DOMAIN_NAME = 'INSTANCE'

    @property
    def count(self):
        """ > Socket 'Instance Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.instance_count

    # ====================================================================================================
    # Properties

    # ----- Transform

    @property
    def transform(self):
        """ > Transform property

        - getter : <&Node Instance Transform>
        - setter : <@Node Set Instance Transform>

        Returns
        -------
        - Matrix
        """
        return Node('Instance Transform')._out

    @transform.setter
    def transform(self, value):
        return self._jump(Node('Set Instance Transform', {'Instances': self._geo, 'Selection': self._sel, 'Transform': value})._out)

    # ----- Translate

    def translate(self, translation=None, local_space=None):
        """ > Node <&Node Translate Instances>

        [&JUMP]

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances : self
        """
        return self._jump(Node('Translate Instances', {'Instances': self._geo, 'Selection': self._sel, 'Translation': translation, 'Local Space': local_space})._out)

    # ----- Scale

    @property
    def scale(self):
        """ > Scale property

        - getter : <&Node Instance Scale>
        - setter : <&Node Scale Instances>

        Scale can be set either by a <!Vector> argument or by a dict with keys
        in ('Scale', 'Center', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.scale = (1, 2, 3)
        instances.insts.scale = {'Scale': (1, 2, 3), 'Center': (10, 11, 12), 'Local Space': True}
        ```

        Returns
        -------
        - Vector
        """
        return Node('Instance Scale')._out

    @scale.setter
    def scale(self, value):
        keys = ['Scale', 'Center', 'Local Space']
        sockets = {'Instances': self._geo, 'Selection': self._sel}
        if isinstance(value, dict):
            for k, v in value.items():
                if k not in keys is None:
                    raise NodeError(f"Node 'Scale Instances' error: invalid key '{k}' to set instance scale.", valid_keys=keys)
                sockets[k] = v
        else:
            sockets['Scale'] = value

        return self._jump(Node('Scale Instances', sockets)._out)

    # ----- Rotation

    @property
    def rotation(self):
        """ > Rotation property

       - getter : <&Node Instance Rotation>
       - setter : <&Node Rotate Instances>

        Rotation can be set either by a <!Rotation> argument or by a dict with keys
        in ('Rotation', 'Pivot Point', 'Local Space')

        ``` python
        instances = Instances()
        instances.insts.rotation = (1, 2, 3)
        instances.insts.rotation = {'Rotation': (1, 2, 3), 'Pivot Point': (10, 11, 12), 'Local Space': True}
        ```

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

        return self._jump(Node('Rotate Instances', sockets)._out)

# =============================================================================================================================
# =============================================================================================================================
# Layer Domain
# =============================================================================================================================
# =============================================================================================================================

class Layer(Domain):
    """ > Layer domain of <!GreasePencil>

    """

    DOMAIN_NAME = 'LAYER'

    @property
    def count(self):
        """ > Socket 'Instance Count' of node <&Node Domain Size>

        Returns
        -------
        - Integer
        """
        return self._geo.domain_size.layer_count


# =============================================================================================================================
# =============================================================================================================================
# Mesh
# =============================================================================================================================
# =============================================================================================================================

class Mesh(Geometry):
    """ > Mesh Geometry

    The **Mesh** exposes all methods specific to meshes.
    Since there is no ambiguity, the word **mesh** is omitted in the **snake_case** name of
    the methods:

    ``` python
    mesh = Mesh.Line() # Node 'Mesh Line'
    cloud = mesh.to_points() # Node 'Mesh to Points'
    ```

    Nodes requiring a domain parameter, are implemented in one of the four domains of Mesh: <#points>,
    <#faces>, <#edges> or <#corners>.

    Properties
    ----------
    - points (Vertex) : POINT domain
    - faces (Face) : FACE domain
    - edges (Edge) : EDGE domain
    - corners (Corner) : CORNER domain
    """

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
        """ > Constructor node <&Node Curve to Mesh>

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
        """ > Constructor node <&Node Points to Vertices>

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
        """ > Constructor node <&Node Volume to Mesh>

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
    # Load

    @classmethod
    def ImportOBJ(cls, path=None):
        """ > Node <&Node Import OBJ>

        Arguments
        ---------
        - path (String) : socket 'Path' (Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import OBJ', {'Path': path})
        return cls(node._out)

    @classmethod
    def ImportSTL(cls, path=None):
        """ > Node <&Node Import STL>

        Arguments
        ---------
        - path (String) : socket 'Path' (Path)

        Returns
        -------
        - Mesh
        """
        node = Node('Import STL', {'Path': path})
        return cls(node._out)

    # =============================================================================================================================
    # Properties

    @property
    def island(self):
        """ > Node <&Node Mesh Island>

        [&RETURN_NODE]

        Returns
        -------
        - Node : 'Mesh Island' node
        """
        return self._cache('Mesh Island')

    @property
    def island_index(self):
        """ > Socket 'Island Index' fo node <&Node Mesh Island>

        Returns
        -------
        - Integer
        """
        return self.island.island_index

    @property
    def island_count(self):
        """ > Socket 'Island Count' fo node <&Node Mesh Island>

        Returns
        -------
        - Integer
        """
        return self.island.island_count

    @property
    def domain_size(self):
        """ > Node <&Domain Size>, component = 'MESH'

        [&RETURN_NODE]

        Returns
        -------
        - Node : 'Domain Size" node
        """
        return self._cache('Domain Size', {'Geometry': self}, component='MESH')

    @classmethod
    def Cube(self, size=(1, 1, 1), vertices_x=2, vertices_y=2, vertices_z=2):
        """ > Constructor node <&Node Cube>

        Arguments
        ---------
        - size (Vector) : socket 'Size' (Size)
        - vertices_x (Integer) : socket 'Vertices X' (Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (Vertices Y)
        - vertices_z (Integer) : socket 'Vertices Z' (Vertices Z)

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Cube', {'Size': size, 'Vertices X': vertices_x, 'Vertices Y': vertices_y, 'Vertices Z': vertices_z})._out)

    @classmethod
    def Line(cls, count=None, start_location=None, offset=None, end_location=None, resolution=None):
        """ > Constructor node <&Node Mesh Line>

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
            return Mesh(Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': end_location},
                mode='END_POINTS', count_mode=count_mode)._out)
        else:
            return Mesh(Node('Mesh Line', {'Count': count, 'Start Location': start_location, 'Offset': offset},
                mode='OFFSET')._out)

    @classmethod
    def LineTo(cls, start_location=None, end_location=None, count=None, resolution=None):
        """ > Constructor node <&Node Mesh Line>

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
        """ > Constructor node <&Node Mesh Line>

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
        """ > Constructor node <&Node Cone>

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
        - Mesh
        """

        return Mesh(Node('Cone', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments,
            'Radius Top': radius_top, 'Radius Bottom': radius_bottom, 'Depth': depth}, fill_type=fill_type)._out)

    @classmethod
    def Cylinder(cls, vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0, fill_type='NGON'):
        """ > Constructor node <&Node Cylinder>

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
        - Mesh
        """
        return Mesh(Node('Cylinder', {'Vertices': vertices, 'Side Segments': side_segments, 'Fill Segments': fill_segments,
            'Radius': radius, 'Depth': depth}, fill_type=fill_type)._out)

    @classmethod
    def Circle(cls, vertices=32, radius=1.0, fill_type='NONE'):
        """ > Constructor node <&Node Mesh Circle>

        Arguments
        ---------
        - vertices (Integer) : socket 'Vertices' (Vertices)
        - radius (Float) : socket 'Radius' (Radius)
        - fill_type (str = 'NONE'): Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Mesh Circle', {'Vertices': vertices, 'Radius': radius}, fill_type=fill_type)._out)

    @classmethod
    def Disk(cls, vertices=32, radius=1.0, fill_type='NGON'):
        """ > Constructor node <&Node Mesh Circle>

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
        """ > Constructor node <&Node Grid>

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (Size X)
        - size_y (Float) : socket 'Size Y' (Size Y)
        - vertices_x (Integer) : socket 'Vertices X' (Vertices X)
        - vertices_y (Integer) : socket 'Vertices Y' (Vertices Y)

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Grid', {'Size X': size_x, 'Size Y': size_y, 'Vertices X': vertices_x, 'Vertices Y': vertices_y})._out)

    @classmethod
    def Plane(cls, size_x=1.0, size_y=1.0):
        """ > Constructor node <&Node Grid>

        Arguments
        ---------
        - size_x (Float) : socket 'Size X' (Size X)
        - size_y (Float) : socket 'Size Y' (Size Y)

        Returns
        -------
        - Mesh
        """
        return cls.Grid(size_x=size_x, size_y=size_y, vertices_x=2, vertices_y=2)


    @classmethod
    def IcoSphere(cls, radius=1.0, subdivisions=1):
        """ > Constructor node <&Node Ico Sphere>

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (Radius)
        - subdivisions (Integer) : socket 'Subdivisions' (Subdivisions)

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Ico Sphere', {'Radius': radius, 'Subdivisions': subdivisions})._out)

    @classmethod
    def UVSphere(cls, segments=32, rings=16, radius=1.0):
        """ > Constructor node <&Node UV Sphere>

        Arguments
        ---------
        - segments (Integer) : socket 'Segments' (Segments)
        - rings (Integer) : socket 'Rings' (Rings)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('UV Sphere', {'Segments': segments, 'Rings': rings, 'Radius': radius})._out)

    # =============================================================================================================================
    # Sample

    def sample_nearest_surface(self, value=None, group_id=None, sample_position=None, sample_group_id=None):
        """ > Node <&Node Sample Nearest Surface>

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - group_id (Integer) : socket 'Group ID' (Group ID)
        - sample_position (Vector) : socket 'Sample Position' (Sample Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (Sample Group ID)

        Returns
        -------
        - Socket
        """
        data_type = utils.get_data_type(value)
        return Node('Sample Nearest Surface', {'Mesh': self, 'Value': value, 'Group ID': group_id, 'Sample Position': sample_position, 'Sample Group ID': sample_group_id}, data_type=data_type)._out

    def sample_uv_surface(self, value=None, uv_map=None, sample_uv=None):
        """ > Node <&Node Sample UV Surface>

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - uv_map (Vector) : socket 'UV Map' (Source UV Map)
        - sample_uv (Vector) : socket 'Sample UV' (Sample UV)
        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

        Returns
        -------
        - Socket
        """
        data_type = utils.get_data_type(value)
        return Node('Sample UV Surface', {'Mesh': self, 'Value': value, 'UV Map': uv_map, 'Sample UV': sample_uv}, data_type=data_type)._out

    # =============================================================================================================================
    # Conversion

    def to_curve(self):
        """ > Node <&Node Mesh to Curve>

        [&NO_JUMP]

        Returns
        -------
        - Curve
        """
        return Curve(Node('Mesh to Curve', {'Mesh': self, 'Selection': self._sel})._out)

    def to_volume(self, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True):
        """ > Node <&Node Mesh to Volume>

        [&NO_JUMP]

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
        """ > Node <&Node Dual Mesh>

        [&JUMP]

        Arguments
        ---------
        - keep_boundaries (Boolean) : socket 'Keep Boundaries' (Keep Boundaries)

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Dual Mesh', {'Mesh': self, 'Keep Boundaries': keep_boundaries})._out)

    def subdivide(self, level=None):
        """ > Node <&Node Subdivide Mesh>

        [&JUMP]

        Arguments
        ---------
        - level (Integer) : socket 'Level' (Level)

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Subdivide Mesh', {'Mesh': self, 'Level': level})._out)

    def triangulate(self, minimum_vertices=None, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY'):
        """ > Node <&Node Triangulate>

        [&JUMP]

        Arguments
        ---------
        - minimum_vertices (Integer) : socket 'Minimum Vertices' (Minimum Vertices)
        - ngon_method (str): Node.ngon_method in ('BEAUTY', 'CLIP')
        - quad_method (str): Node.quad_method in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Triangulate', {'Mesh': self, 'Selection': self._sel, 'Minimum Vertices': minimum_vertices},
            quad_method=quad_method, ngon_method=ngon_method)._out)

    def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL'):
        """ > Node <&Node Subdivision Surface>

        [&JUMP]

        Arguments
        ---------
        - level (Integer) : socket 'Level' (Level)
        - edge_crease (Float) : socket 'Edge Crease' (Edge Crease)
        - vertex_crease (Float) : socket 'Vertex Crease' (Vertex Crease)
        - boundary_smooth (str): Node.boundary_smooth in ('PRESERVE_CORNERS', 'ALL')
        - uv_smooth (str): Node.uv_smooth in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')

        Returns
        -------
        - Mesh : self
        """
        return self._jump(Node('Subdivision Surface', {'Mesh': self, 'Level': level, 'Edge Crease': edge_crease, 'Vertex Crease': vertex_crease},
            uv_smooth=uv_smooth, boundary_smooth=boundary_smooth)._out)

    # ----- Mesh Boolean

    @classmethod
    def Boolean(cls, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT', operation='DIFFERENCE'):
        """ > Constructor node <&Node Mesh Boolean>

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - operation (str): Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh
        """
        if len(meshes)==0:
            return None
        elif len(meshes) == 1:
            return meshes[0]

        if operation == 'DIFFERENCE':
            sockets = {'Mesh 1': meshes[0], 'Mesh 2': list(meshes[1:])}
        else:
            sockets = {'Mesh 2': list(meshes)}
        sockets = {**sockets, 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}

        return cls(Node('Mesh Boolean', sockets, solver=solver, operation=operation)._out)

    @classmethod
    def Difference(cls, mesh, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Constructor node <&Node Mesh Boolean>, operation = 'DIFFERENCE'

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh 1' (Mesh 1)
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh
        """
        if len(meshes)==0:
            return mesh

        return cls.Boolean(*([mesh] + list(meshes)), self_intersection=self_intersection,
            hole_tolerant=hole_tolerant, solver=solver, operation='DIFFERENCE')

    @classmethod
    def Intersect(cls, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Constructor node <&Node Mesh Boolean>, operation = 'INTERSECT'

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh
        """
        return cls.Boolean(*meshes, self_intersection=self_intersection,
            hole_tolerant=hole_tolerant, solver=solver, operation='INTERSECT')

    @classmethod
    def Union(cls, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Constructor node <&Node Mesh Boolean>, operation = 'UNION'

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh
        """
        return cls.Boolean(*meshes, self_intersection=self_intersection,
            hole_tolerant=hole_tolerant, solver=solver, operation='UNION')


    def boolean(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT', operation='DIFFERENCE'):
        """ > Node <&Node Mesh Boolean>

        [&JUMP]

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - operation (str): Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh : self
        """
        if operation == 'DIFFERENCE':
            sockets = {'Mesh 1': self, 'Mesh 2': list(meshes)}
        else:
            sockets = {'Mesh 2': [self] + list(meshes)}
        sockets = {**sockets, 'Self Intersection': self_intersection, 'Hole Tolerant': hole_tolerant}
        return self._jump(Node('Mesh Boolean', sockets, solver=solver, operation=operation)._out)

    def difference(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>, operation = 'DIFFERENCE'

        [&JUMP]

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh : self
        """
        return self.boolean(*meshes, self_intersection=self_intersection, hole_tolerant=hole_tolerant,
            solver=solver, operation='DIFFERENCE')

    def intersect(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>, operation = 'INTERSECT'

        [&JUMP]

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh : self
        """
        return self.boolean(*meshes, self_intersection=self_intersection, hole_tolerant=hole_tolerant, solver=solver, operation='INTERSECT')

    def union(self, *meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT'):
        """ > Node <&Node Mesh Boolean>, operation = 'UNION'

        [&JUMP]

        Arguments
        ---------
        - *meshes (Mesh) : socket 'Mesh 2' (Mesh 2)
        - self_intersection (Boolean) : socket 'Self Intersection' (Self Intersection)
        - hole_tolerant (Boolean) : socket 'Hole Tolerant' (Hole Tolerant)
        - solver (str): Node.solver in ('EXACT', 'FLOAT')

        Returns
        -------
        - Mesh : self
        """
        return self.boolean(*meshes, self_intersection=self_intersection, hole_tolerant=hole_tolerant, solver=solver, operation='UNION')

    def __sub__(self, other):
        if isinstance(other, tuple):
            return Mesh.Difference(self, *other)
        else:
            return Mesh.Difference(self, other)

    def __truediv__(self, other):
        if isinstance(other, tuple):
            return Mesh.Intersect(self, *other)
        else:
            return Mesh.Intersect(self, other)

    def __mul__(self, other):
        if isinstance(other, tuple):
            return Mesh.Union(self, *other)
        else:
            return Mesh.Union(self, other)


    # ----- UV

    def pack_uv_islands(self, uv=None, margin=None, rotate=None):
        """ > Node <&Node Pack UV Islands>

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
        """ > Node <&Node UV Unwrap>

        Arguments
        ---------
        - seam (Boolean) : socket 'Seam' (Seam)
        - margin (Float) : socket 'Margin' (Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (Fill Holes)
        - method (str): Node.method in ('ANGLE_BASED', 'CONFORMAL')

        Returns
        -------
        - Vector
        """
        return Node('UV Unwrap', {'Selection': self._sel, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)._out

    # ----- Distribute points

    def distribute_points_on_faces(self, density=None, distance_min=None, density_max=None, density_factor=None, seed=None):#, poisson=False):
        """ > Node <&Node Distribute Points on Faces>

        [&NO_JUMP]

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
        - Cloud
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

        return Cloud(node._out)


# =============================================================================================================================
# =============================================================================================================================
# Curve
# =============================================================================================================================
# =============================================================================================================================

class Curve(Geometry):
    """ > Curve Geometry

    The **Curve** class exposes all methods specific to curves.
    Since there is no ambiguity, the word **curve** is omitted in the name of
    the methods:

    ``` python
    curve = Curve.Line() # Node 'Curve Line'
    mesh= curve.fill() # Node 'Fill Curve'
    ```

    Nodes requiring a domain parameter, are implemented in one of the two domains of **Curve** <#points>,
    <#splines>.

    Properties
    ----------
    - points (SplinePoint) : POINT domain
    - splines (Spline) : CURVE (or SPLINE) domain
    """

    def _reset(self):

        super()._reset()

        self.points  = SplinePoint(self)
        self.splines = Spline(self)

    # =============================================================================================================================
    # Constructors

    # ----- Circle

    @classmethod
    def Circle(cls, resolution=None, radius=None, point_1=None, point_2=None, point_3=None):
        """ > Constructor node <&Node Curve Circle>

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
            return cls(Node('Curve Circle', {'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3}, mode='POINTS')._out)
        else:
            return cls(Node('Curve Circle', {'Resolution': resolution, 'Radius': radius}, mode='RADIUS')._out)

    # ----- Arc
    #
    @classmethod
    def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None,
                 start=None, middle=None, end=None, offset_angle=None,
                 connect_center=None, invert_arc=None):
        """ > Constructor node <&Node Arc>

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
        - Curve
        """


        if start is not None or middle is not None or end is not None or offset_angle is not None:
            return cls(Node('Arc', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end, 'Offset Angle': offset_angle,
                            'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='POINTS')._out)

        else:
            return cls(Node('Arc', {'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle,
                            'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='RADIUS')._out)

    # ----- Line

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None):
        """ > Constructor node <&Node Curve Line>

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

    # ----- Bezier

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ > Constructor node <&Node Bézier Segment>

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
        """ > Constructor node <&Node Quadratic Bézier>

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
        """ > Constructor node <&Node Spiral>

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
        """ > Constructor node <&Node Star>

        Arguments
        ---------
        - points (Integer) : socket 'Points' (Points)
        - inner_radius (Float) : socket 'Inner Radius' (Inner Radius)
        - outer_radius (Float) : socket 'Outer Radius' (Outer Radius)
        - twist (Float) : socket 'Twist' (Twist)

        Returns
        -------
        - Curve
        """
        return cls(Node('Star', {'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})._out)

    # ----- Quadrilateral

    @classmethod
    def Quadrilateral(cls, width=None, height=None):
        """ > Constructor node <&Node Quadrilateral>

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
        """ > Constructor node <&Node Quadrilateral>

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
        """ > Constructor node <&Node Quadrilateral>

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
        """ > Constructor node <&Node Quadrilateral>

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
        """ > Constructor node <&Node Quadrilateral>

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
        """ > Constructor node <&Node Quadrilateral>

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
        """ > Constructor node <&Node Mesh to Curve>

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
        """ > Constructor Constructor node <&Node Edge Paths to Curves>

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
        """ > Constructor node <&Node Points to Curves>

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
        """ > Node <&Domain Size>, component = 'CURVE'

        Returns
        -------
        - Node : 'Domain Size" node
        """
        return self._cache('Domain Size', {'Geometry': self}, component='CURVE')

    # ----- Radius

    @property
    def radius(self):
        """ > Radius property

       - getter : <&Node Radius>
       - setter : <&Node Set Curve Radius>

        Returns
        -------
        - Float
        """
        return Node('Radius')._out

    @radius.setter
    def radius(self, value):
        self._jump(Node('Set Curve Radius', {'Curve': self, 'Selection': self._sel, 'Radius': value})._out)

    # ----- Tilt

    @property
    def tilt(self):
        """ > Tilt property

       - getter : <&Node Curve Tilt>
       - setter : <&Node Set Curve Tilt>

        Returns
        -------
        - Float
        """
        return Node('Curve Tilt')._out

    @tilt.setter
    def tilt(self, value):
        self._jump(Node('Set Curve Tilt', {'Curve': self, 'Selection': self._sel, 'Tilt': value})._out)

    # ----- Curve normal

    @property
    def normal(self):
        """ > Normal write only property, normal in ('MINIMUM_TWIST', 'Z_UP', 'FREE')



       - getter : None
       - setter : <&Node Set Curve Normal>

        Returns
        -------
        - Error
        """

        raise NodeError(f"Curve.normal property is write only")

    @normal.setter
    def normal(self, value):
        return self._jump(Node('Set Curve Normal', {'Curve': self, 'Selection': self._sel}, mode=value)._out)

    @classmethod
    @property
    def tangent(cls):
        """ > Tangent read only property

       - getter : <&Node Curve Tangent>
       - setter : None

        Returns
        -------
        - Vector
        """
        return Node('Curve Tangent')._out

    @property
    def length(self):
        """ > Length read only property

       - getter : <&Node Curve Length>
       - setter : None

        Returns
        -------
        - Float
        """
        return Node('Curve Length', {'Curve': self})._out

    @classmethod
    def endpoint_selection(cls, start_size=None, end_size=None):
        """ > Node <&Node Endpoint Selection>

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
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (Point Index)

        Returns
        -------
        - Integer
        """
        return Node('Curve of Point', {'Point Index': point_index})._out

    @classmethod
    def offset_point_in_curve(cls, point_index=None, offset=None):
        """ > Node <&Node Offset Point in Curve>

        > [!CAUTION]
        > This method doesn't return the top output socket which is the Boolean 'Is Valid Offset' but
        > the second one, the Integer 'Point Index'

        ``` python
        curve = Curve.Spiral()
        index = curve.offset_point(0, 3)
        is_valid = index.is_valid_offset_
        ```

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (Point Index)
        - offset (Integer) : socket 'Offset' (Offset)

        Returns
        -------
        - Integer
        """
        return Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset}).point_index

    @classmethod
    def points_of_curve(cls, curve_index=None, weights=None, sort_index=None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (Curve Index)
        - weights (Float) : socket 'Weights' (Weights)
        - sort_index (Integer) : socket 'Sort Index' (Sort Index)

        Returns
        -------
        - Integer
        """
        return Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})._out

    # =============================================================================================================================
    # Methods

    def set_normal(self, mode='MINIMUM_TWIST'):
        """ > Node <&Node Set Curve Normal>

        [&JUMP]

        Arguments
        ---------
        - mode (str): Node.mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')

        Returns
        -------
        - Curve : self
        """
        return self._jump(Node('Set Curve Normal', {'Curve': self, 'Selection': self._sel}, mode=mode)._out)

    def set_normal_z_up(self):
        """ > Node <&Node Set Curve Normal>

        [&JUMP]

        Returns
        -------
        - Curve : self
        """
        return self.set_normal(mode='Z_UP')

    def set_normal_free(self):
        """ > Node <&Node Set Curve Normal>

        [&JUMP]

        Returns
        -------
        - Curve : self
        """
        return self.set_normal(mode='FREE')

    def sample(self, value=None, factor=None, length=None, curve_index=None, all_curves=False):
        """ > Node <&Node Sample Curve>

        'mode' is set to 'LENGTH' if factor is None, else 'FACTOR'

        - data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
        - mode (str): Node.mode in ('FACTOR', 'LENGTH')

        > [!NOTE]
        > The method returns the value which is sampled.
        > To get other sockets, use the **peer sockets** naming convention:

        ``` python
        curve = Curve.Line()

        a = curve.sample()

        position = a.position_
        tangent = a.tangent_
        normal = a.normal_
        ```

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - factor (Float) : socket 'Factor' (Factor)
        - length (Float) : socket 'Length' (Length)
        - curve_index (Integer) : socket 'Curve Index' (Curve Index)
        - all_curves (bool): Node.use_all_curves

        Returns
        -------
        - Socket [position_, tangent_, normal_]
        """

        sockets = {'Curves': self, 'Value': value, 'Curve Index': curve_index}
        if length is None:
            mode = 'FACTOR'
            sockets['Factor'] = factor
        else:
            mode = 'LENGTH'
            sockets['Length'] = length

        return Node('Sample Curve', sockets, data_type=utils.get_data_type(value), mode=mode, use_all_curves=all_curves)._out

    # =============================================================================================================================
    # Operations

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ > Node <&Node Curve to Mesh>

        [&NO_JUMP]

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
        """ > Node <&Node Curve to Points>

        [&NO_JUMP]

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - count (Integer) : socket 'Count' (Count)
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Cloud
        """
        return Cloud.FromCurve(curve=self, count=count, length=length, mode='EVALUATED')

    def to_grease_pencil(self, instances_as_layers=None):
        """ Node 'Curves to Grease Pencil' (GeometryNodeCurvesToGreasePencil)

        <&NODE Curves to Grease Pencil>

        Arguments
        ---------
        - instances_as_layers (Boolean) : socket 'Instances as Layers' (Instances as Layers)

        Returns
        -------
        - grease_pencil (GreasePencil)
        """
        from geonodes import GreasePencil

        node = Node('Curves to Grease Pencil', {'Curves': self.to_instance(), 'Selection': self._sel, 'Instances as Layers': instances_as_layers})
        return GreasePencil(node._out)

    def deform_on_surface(self):
        """ > Node <&Node Deform Curves on Surface>

        [&JUMP]

        Returns
        -------
        - Curve : self
        """
        return self._jump(Node('Deform Curves on Surface', {'Curves': self})._out)

    # ----- Fill curve

    def fill(self, group_id=None, mode='TRIANGLES'):
        """ > Node <&Node Fill Curve>

        [&NO_JUMP]

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
        """ > Node <&Node Fillet Curve>

        [&JUMP]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (Limit Radius)
        - count (Integer) : socket 'Integer' (Integer)
        - mode (str): Node.mode in ('BEZIER', 'POLY')

        Returns
        -------
        - Curve : self
        """
        return self._jump(Node('Fillet Curve', {'Curve': self, 'Count': count, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)._out)

    # ----- Interpolate curves

    def interpolate(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Node <&Node Interpolate Curves>

        [&JUMP]

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
        - Curve : self
        """
        return self._jump(Node('Interpolate Curves', {'Guide Curves': self, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id,
            'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})._out)

    # ----- Resample

    def resample(self, count=None, length=None):
        """ > Node <&Node Resample Curve>

        [&JUMP]

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
        - Curve : self
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

        return self._jump(Node('Resample Curve', sockets, mode=mode)._out)

    # ----- Trim

    def trim(self, start=None, end=None, mode='FACTOR'):
        """ > Node <&Node Trim Curve>

        [&JUMP]

        Arguments
        ---------
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)
        - mode (str): Node.mode in ('FACTOR', 'LENGTH')

        Returns
        -------
        - Curve : self
        """
        return self._jump(Node('Trim Curve', {'Curve': self, 'Selection': self._sel, 'Start': start, 'End': end}, mode=mode)._out)

    def trim_factor(self, start=None, end=None):
        """ > Node <&Node Trim Curve>, mode = 'FACTOR'

        [&JUMP]

        Arguments
        ---------
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)

        Returns
        -------
        - Curve : self
        """
        return self.trim(start=start, end=end, mode='FACTOR')

    def trim_length(self, start=None, end=None):
        """ > Node <&Node Trim Curve>, mode = 'LENGTH'

        [&JUMP]

        Arguments
        ---------
        - start (Float) : socket 'Start' (Start)
        - end (Float) : socket 'End' (End)

        Returns
        -------
        - Curve : self
        """
        return self.trim(start=start, end=end, mode='LENGTH')

    # ----- Various

    def reverse(self):
        """ > Node <&Node Reverse Curve>

        [&JUMP]

        Returns
        -------
        - Curve : self
        """
        return self._jump(Node('Reverse Curve', {'Curve': self, 'Selection': self._sel})._out)

    def subdivide(self, cuts=None):
        """ > Node <&Node Subdivide Curve>

        [&JUMP]

        Arguments
        ---------
        - cuts (Integer) : socket 'Cuts' (Cuts)

        Returns
        -------
        - Curve : self
        """
        return self._jump(Node('Subdivide Curve', {'Curve': self, 'Cuts': cuts})._out)


# =============================================================================================================================
# =============================================================================================================================
# Cloud Points
# =============================================================================================================================
# =============================================================================================================================

class Cloud(Geometry):
    """ > Cloud of Points Geometry

    > [!NOTE]
    > In Blender, the name can vary between **Point Cloud** and **Points**.
    > In GeoNodes, the geometry is named **Cloud**.

    The **Cloud** exposes all methods specific to points cloud.
    Since there is no ambiguity, the word **points** is omitted in the name of
    the methods:

    ``` python
    curves = cloud.to_curves() # Node 'Points to Curves'
    ```

    Nodes requiring a domain parameter, are implemented in the domain <#points>.

    Properties
    ----------
    - points (CloudPoint) : POINT domain
    """

    def _reset(self):

        super()._reset()

        self.points  = CloudPoint(self)

    # =============================================================================================================================
    # Constructors

    @classmethod
    def Points(cls, count=1, position=None, radius=None):
        """ > Constructor node <&Node Points>

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
        """ > Constructor node <&Node Curve to Points>

        Arguments
        ---------
        - curve (Geometry) : socket 'Curve' (Curve)
        - count (Integer) : socket 'Count' (Count)
        - mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Cloud [tangent_, normal_, rotation_]
        """
        return Node('Curve to Points', {'Curve': curve, 'Count': count, 'Length': length}, mode=mode)._out

    # ----- Instances to points

    @classmethod
    def FromInstances(cls, instances, position=None, radius=None):
        """ > Constructor node <&Node Instances to Points>

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
        """ > Constructor node <&Node Mesh to Points>

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
        """ > Constructor node <&Node Mesh to Points>, mode VERTICES

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (Mesh)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """
        return Mesh(mesh)[mesh._sel].points.to_points(position=position, radius=radius)

    @classmethod
    def FromFaces(cls, mesh, position=None, radius=None):
        """ > Constructor node <&Node Mesh to Points>, mode FACES

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (Mesh)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """
        return Mesh(mesh)[mesh._sel].faces.to_points(position=position, radius=radius)

    @classmethod
    def FromCorners(cls, mesh, position=None, radius=None):
        """ > Constructor node <&Node Mesh to Points>, mode CORNERS

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (Mesh)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """
        return Mesh(mesh)[mesh._sel].corners.to_points(position=position, radius=radius)

    @classmethod
    def FromEdges(cls, mesh, position=None, radius=None):
        """ > Constructor node <&Node Mesh to Points>, mode EDGES

        Arguments
        ---------
        - mesh (Mesh) : socket 'Mesh' (Mesh)
        - position (Vector) : socket 'Position' (Position)
        - radius (Float) : socket 'Radius' (Radius)

        Returns
        -------
        - Cloud
        """
        return Mesh(mesh)[mesh._sel].edges.to_points(position=position, radius=radius)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        """ > Node <&Domain Size>, component = 'POINTCLOUD'

        Returns
        -------
        - Node : 'Domain Size" node
        """
        return self._cache('Domain Size', {'Geometry': self}, component='POINTCLOUD')

    # =============================================================================================================================
    # Methods

    # ----- to curves

    def to_curves(self, curve_group_id=None, weight=None):
        """ > Node <&Node Points to Curves>

        [&NO_JUMP]

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
        """ > Node <&Node Points to Vertices>

        [&NO_JUMP]

        Returns
        -------
        - Mesh
        """
        return Mesh(Node('Points to Vertices', {'Points': self, 'Selection': self._sel})._out)

    # ----- to volume

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Node <&Node Points to Volume>

        [&NO_JUMP]

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
    """ > Instances Geometry

    > [!NOTE]
    > The name of geometry class is plural : **Instances** when the name of the
    > domain is singular : <!Instance>. The named of the domain property is <#insts>.

    The **Instances** class exposes all methods specific to instances.
    Since there is no ambiguity, the word **instances** is omitted in the name of
    the methods:

    ``` python
    realized = instances.realize() # Node 'Realize Instances'
    ```
    Nodes requiring a domain parameter, are implemented in the domain <#insts>.

    Properties
    ----------
    - insts (Instance) : INSTANCES domain
    """

    def _reset(self):

        super()._reset()

        self.insts  = Instance(self)

    # =============================================================================================================================
    # Constructors

    @classmethod
    def FromGeometry(cls, *geometries):
        """ > Constructor node <&Node Geometry to Instance>

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
        """ > Constructor node <&Node String to Curves>

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
        return cls(Node('String to Curves', {'String': string, 'Size': size, 'Character Spacing': character_spacing,
            'Word Spacing': word_spacing, 'Line Spacing': line_spacing,
            'Text Box Width': text_box_width, 'Text Box Height': text_box_height},
            overflow=overflow, align_x=align_x, align_y=align_y, pivot_mode=pivot_mode)._out)

    @classmethod
    def ImportPLY(cls, path=None):
        """ > Node <&Node Import PLY>

        Arguments
        ---------
        - path (String) : socket 'Path' (Path)

        Returns
        -------
        - Instances
        """
        node = Node('Import PLY', {'Path': path})
        return cls(node._out)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        """ > Node <&Domain Size>, component = 'INSTANCES'

        Returns
        -------
        - Node : 'Domain Size" node
        """
        return self._cache('Domain Size', {'Geometry': self}, component='INSTANCES')

    # =============================================================================================================================
    # Operations

    def realize(self, realize_all=None, depth=None):
        """ > Node <&Node Realize Instances>

        [&NO_JUMP]

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
        """ > Node <&Node Instances to Points>

        [&NO_JUMP]

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
        """ > Node <&Node Instance on Points>

        [&JUMP]

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (Instance Index)
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - scale (Vector) : socket 'Scale' (Scale)

        Returns
        -------
        - Instances : self
        """
        if isinstance(points, Domain):
            points = Cloud(points._geo).points[points._sel]
        else:
            points = Cloud(points).points[points._sel]

        return self._jump(points.instance_on(instance=self, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale))

    def translate(self, translation=None, local_space=None):
        """ > Node <&Node Translate Instances>

        [&JUMP]

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (Translation)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances : self
        """
        return self._jump(Node('Translate Instances', {'Instances': self, 'Selection': self._sel, 'Translation': translation, 'Local Space': local_space})._out)

    def scale(self, scale=None, center=None, local_space=None):
        """ > Node <&Node Scale Instances>

        [&JUMP]

        Arguments
        ---------
        - scale (Vector) : socket 'Scale' (Scale)
        - center (Vector) : socket 'Center' (Center)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances : self
        """
        return self._jump(Node('Scale Instances', {'Instances': self, 'Selection': self._sel, 'Scale': scale, 'Center': center, 'Local Space': local_space})._out)

    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """ > Node <&Node Rotate Instances>

        [&JUMP]

        Arguments
        ---------
        - rotation (Rotation) : socket 'Rotation' (Rotation)
        - pivot_point (Vector) : socket 'Pivot Point' (Pivot Point)
        - local_space (Boolean) : socket 'Local Space' (Local Space)

        Returns
        -------
        - Instances : self
        """
        return self._jump(Node('Rotate Instances', {'Instances': self, 'Selection': self._sel, 'Rotation': rotation, 'Pivot Point': pivot_point, 'Local Space': local_space})._out)

    def to_grease_pencil(self, instances_as_layers=None):
        """ Node 'Curves to Grease Pencil' (GeometryNodeCurvesToGreasePencil)

        <&NODE Curves to Grease Pencil>

        Arguments
        ---------
        - instances_as_layers (Boolean) : socket 'Instances as Layers' (Instances as Layers)

        Returns
        -------
        - grease_pencil (Geometry)
        """

        node = Node('Curves to Grease Pencil', {'Curves': self, 'Selection': self._sel, 'Instances as Layers': instances_as_layers})
        return node._out


# =============================================================================================================================
# =============================================================================================================================
# Volume
# =============================================================================================================================
# =============================================================================================================================

class Volume(Geometry):
    """ > Volume Geometry

    The **Volume** class exposes all methods specific to volume.
    Since there is no ambiguity, the word **volume** is omitted in the name of
    the methods:

    ``` python
    cube = Volume.Cube() # Node 'Volume Cube'
    ```
    """

    def _reset(self):
        super()._reset()

    # =============================================================================================================================
    # Constructors

    @classmethod
    def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
        """ > Constructor node <&Node Volume Cube>

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
        """ > Constructor node <&Node Mesh to Volume>

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
        """ > Node <&Node Points to Volume>

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
        """ > Node <&Node Distribute Points in Volume>

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
        """ > Node <&Node Distribute Points in Volume>

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
        """ > Node <&Node Distribute Points in Volume>

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
        """ > Node <&Node Volume to Mesh>

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
        """ > Node <&Node Volume to Mesh>

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
        """ > Node <&Node Volume to Mesh>

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
        """ > Node <&Node Volume to Mesh>

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



# =============================================================================================================================
# =============================================================================================================================
# Grease Pencil
# =============================================================================================================================
# =============================================================================================================================

class GreasePencil(Geometry):
    """ > Grease Pencil Geometry

    Properties
    ----------
    - layers (Layer) : LAYER domain

    """

    def _reset(self):

        super()._reset()

        self.layers  = Layer(self)

    # =============================================================================================================================
    # Properties

    @property
    def domain_size(self):
        """ > Node <&Domain Size>, component = 'GREASEPENCIL'

        [&RETURN_NODE]

        Returns
        -------
        - Node : 'Domain Size" node
        """
        return self._cache('Domain Size', {'Geometry': self}, component='GREASEPENCIL')

    # =============================================================================================================================
    # Constructors

    @classmethod
    def FromCurve(cls, curves=None, selection=None, instances_as_layers=True):
        """ > Constructor node <&Node Curves to Grease Pencil>

        Arguments
        ---------
        - curves (Geometry) : socket 'Curves' (Curves)
        - selection (Boolean) : socket 'Selection' (Selection)
        - instances_as_layers (Boolean = True) : socket 'Instances as Layers' (Instances as Layers)

        Returns
        -------
        - GreasePencil
        """
        return cls(Node('Curves to Grease Pencil', {'Curves': curves, 'selectin': selection, 'Instances as Layers': instances_as_layers})._out)

    # =============================================================================================================================
    # to Curves

    def to_curves(self, layers_as_instances=None):
        """ Node 'Grease Pencil to Curves' (GeometryNodeGreasePencilToCurves)

        <&NODE Grease Pencil to Curves>

        Arguments
        ---------
        - grease_pencil (Geometry) : socket 'Grease Pencil' (Grease Pencil)
        - layers_as_instances (Boolean) : socket 'Layers as Instances' (Layers as Instances)

        Returns
        -------
        - curves (Curve)
        """

        node = Node('Grease Pencil to Curves', {'Grease Pencil': self._geo, 'Selection': self._sel, 'Layers as Instances': layers_as_instances})
        return node._out

    # =============================================================================================================================
    # Methods

    def merge_layers(self, mode='MERGE_BY_NAME'):
        """ > Node <&Node Merge Layers>

        [&JUMP]

        Arguments
        ---------
        - mode (str): Node.mode in ('MERGE_BY_NAME', 'MERGE_BY_ID')

        Returns
        -------
        - Grease Pencil
        """
        return self._jump(Node('Merge Layers', {'Grease Pencil': self, 'Selection': self._sel}, mode=mode)._out)

    def merge_layers_by_name(self):
        """ > Node <&Node Merge Layers>

        [&JUMP]

        Returns
        -------
        - Geometry
        """
        return self.merge_layers(mode='MERGE_BY_NAME')

    def merge_layers_by_group_id(self):
        """ > Node <&Node Merge Layers>

        [&JUMP]

        Returns
        -------
        - Grease Pencil
        """
        return self.merge_layers(mode='MERGE_BY_ID')
