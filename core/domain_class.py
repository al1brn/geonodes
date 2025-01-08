"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : domainclass
----------------------
- Implement Domain

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

classes
-------
- Domain        : Domain base class
- Point         : POINT domain
- Vertex        : POINT domain for Mesh
- CloudPoint    : POINT domain for Points
- Face          : FACE domain
- Edge          : EDGE domain
- Corner        : CORNER domain
- Spline        : SPLINE domain
- Instance      : INSTANCE domain

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
- update : 2024/12/30
"""

from inspect import Arguments
import bpy
from bpy.types import Property, PythonConstraint, SmoothModifier

from .proplocker import PropLocker

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Tree, Node, Layout
from .socket_class import NodeCache, Socket
from .geometry_class import GeoBase, Geometry

class Domain(GeoBase, NodeCache, PropLocker):

    DOMAIN_NAME = None

    def __init__(self, geometry: Geometry):
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

        self._lock()

    def __str__(self):
        return f"<Domain {self.DOMAIN_NAME} of {self._geo}>"

    # ----- Jump

    def _jump(self, socket, reset=True):
        return self._geo._jump(socket, reset=reset)

    @property
    def _domain_to_geometry(self):
        return self._geo


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

    def _node_OLD(self, node_name, sockets={}, geometry='Geometry', selection='Selection', domain='domain', use_cache=False, **parameters):

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

    def restrict_domain_OLD(self, domains=(), title=""):
        if self.DOMAIN_NAME in domains:
            return True
        raise NodeError(f"{title} restricted to domains {domains}, not '{self.DOMAIN_NAME}'")

    def exclude_corner_OLD(self, title):
        return self.restrict_domain(['POINT', 'FACE', 'EDGE', 'CURVE', 'INSTANCE', 'LAYER'])

    def plural_domain_OLD(self, domains=None, title=""):
        PLURAL = {'POINT': 'VERTICES', 'EDGE': 'EDGES', 'FACE': 'FACES', 'CORNER': 'CORNERS', 'SPLINE': 'SPLINES', 'CURVE': 'SPLINES', 'LAYER': 'LAYERS'}
        if domains is not None:
            self.restrict_domain(domains=domains, title=title)
        return PLURAL[self.DOMAIN_NAME]

    # Rename domain name
    def domain_name_OLD(self, rename={}):
        if self.DOMAIN_NAME in rename:
            return rename[self.DOMAIN_NAME]
        else:
            return self.DOMAIN_NAME

    # ====================================================================================================
    # Named attributes

    def __getattr__(self, name):

        attr_name = utils.get_attr_name(name)
        if attr_name is None:
            raise NodeError(f"Domain '{type(self).__name__}' doesn't have attribute named '{name}'", keyword=name)
            #raise AttributeError(f"Domain '{type(self).__name__}' doesn't have attribute named '{name}'")

        return self._geo._tree.get_named_attribute(prop_name=name)

    def __setattr__(self, name, value):
        attr_name = utils.get_attr_name(name)
        if attr_name is None:
            return super().__setattr__(name, value)

        self.store_named_attribute(attr_name, value)

    # ====================================================================================================
    # Sample index

    def __call__(self, value, index=None):

        from geonodes import nd

        if index is None:
            index = nd.index

        return self.sample_index(value, index=index)

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
    # Methods

    # ----------------------------------------------------------------------------------------------------
    # Capture attribute

    def capture_attribute(self, attribute=None, **attributes):
        """ > Node <&Node Capture Attribute>

        [&JUMP]

        > [!NOTE]
        > Use <#capture> to capture one single attribute

        > [!CAUTION]
        > When there is only one attribute, the function returns the captured attribute,
        > otherwise returns the node.

        ``` python
        with GeoNodes("Capture Attribute"):
            # Capture several attributes
            node = mesh.points.capture_attribute(attr1 = attr1, attr2=attr2)
            captured_attr1 = node.attr1
            captured_attr2 = node.attr2

            # Capture one single attribute
            captured_attr = mesh.points.capture_attribute(my_attr=attr1)

            # Capture one attribute without key
            captured_attr3 = mesh.points.capture_attribute(attr3)

            # Equivalent to
            captured_attr3 = mesh.points.capture(attr3)
        ```

        Arguments
        ---------
        - attribute (Socket) : first attribute to capture
        - **attributes (Sockets): named attributes to capture

        Returns
        -------
        - Node
        """
        if len(attributes) == 0:
            attrs = {'attribute': attribute}
        else:
            if attribute is None:
                attrs = attributes
            else:
                attrs = {'attribute': attribute, **attributes}

        node = Node('Capture Attribute', sockets={'Geometry': self})
        node._set_items(**attrs)
        self._jump(node._out)
        if len(attrs) == 1:
            return node[1]
        else:
            return node

    # ----------------------------------------------------------------------------------------------------
    # Capture a single attribute

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
