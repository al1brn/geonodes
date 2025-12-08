"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : domain_class
------------------
- Root class for actual domains

This class shares the same root as geometry with implements the node cache
and the selection mechanisms

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


from inspect import Arguments
import bpy

from . import utils
from .sockettype import SocketType
from .treeclass import Tree, Layout
from .nodeclass import Node
from .nodezone import ZoneNode, ZoneIterator
from .socket_class import NodeCache, Socket
from .geom import Geom
from .geometry_class import Geometry

class Domain(Geom, NodeCache):

    __slots__ = NodeCache.__slots__ + ['_geo', '_selection']

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

        When a node as a ***Selection*** socket, the value can be set using the get item syntax:

        ``` python
            # Plug the value of 'my_selection` into Selection socket
            Mesh().points[my_selection].store_named_attribute("Name", value)
        ```

        > [!IMPORTANT]
        > Domains are never instantiated directly but created by geometries.

        The domain specific to geometries are the followings:
            - Mesh:
                - points (class <!Vertex>)
                - faces (class <!Face>)
                - edges (class <!Edge>)
                - corners (clas <!Corner>)
            - Curve:
                - points (class <!SplinePoint>)
                - splines (class <!Spline>)
            - GreasePencil:
                - layers (class <!Layer>)
            - Instances
                - insts (class <!Instance>)
            - Cloud
                - points (class <!CloudPoint>)
            - Volume

        All the domain classes are a subclass of <!Domain>.
        <!Vertex>, <!SplinePoint> and <!SplinePoint> classes are subclasses of <!Point>.

        > See: <!Vertex>, <!Face>, <!Edge>, <!Corner>, <!SplinePoint>, <!Spline>, <!CloudPoint>, <!Instance>

        Properties
        ----------
        - _geo (Geometry) : the geometry the domain belongs to
        """

        # ---------------------------------------------------------------------------
        # Geom interface initialization
        # ---------------------------------------------------------------------------

        self._geo = geometry
        self._selection = None

        # ---------------------------------------------------------------------------
        # Node cache interface initialization
        # ---------------------------------------------------------------------------

        self._cache_reset()

    # ====================================================================================================
    # str
    # ====================================================================================================

    def __str__(self):
        return f"<Domain {self.DOMAIN_NAME} of {self._geo}>"

    # ====================================================================================================
    # Jump
    # ====================================================================================================

    def _jump(self, socket, reset=True):
        return self._geo._jump(socket, reset=reset)
    
    # ====================================================================================================
    # To geometry
    # ====================================================================================================

    @property
    def _domain_to_geometry(self):
        return self._geo
    
    # ====================================================================================================
    # Overrides Geom selection
    # Selection can be done either on the geometry or on the domain (or both but strange !)
    # ====================================================================================================

    def get_selection(self):
        """ Get the selection from Gometry and/or from Domain
        """
        dom_sel = super().get_selection()        
        geo_sel = self._geo.get_selection()

        if dom_sel is None:
            return geo_sel
        elif geo_sel is None:
            return dom_sel
        else:
            return dom_sel & geo_sel

    # ====================================================================================================
    # Named attributes
    # ====================================================================================================

    def __setattr__(self, name, value):

        if name in Domain.__slots__:
            super().__setattr__(name, value)
            return
        
        user_name = name.replace("_", " ").strip()
        
        self.store_named_attribute(user_name, value)

    # ====================================================================================================
    # Sample index
    # ====================================================================================================

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

        return ForEachElement(geometry=self._geo, selection=self.get_selection(), domain=self.DOMAIN_NAME, sockets=sockets, **kwargs)

    # ====================================================================================================
    # Methods
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Capture attribute
    # ----------------------------------------------------------------------------------------------------

    def capture_attribute(self, attribute=None, **attributes):
        """ > Node <&Node Capture Attribute>

        [&JUMP]

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
        ```

        Arguments
        ---------
        - attribute (Socket) : first attribute to capture
        - **attributes (Sockets): named attributes to capture

        Returns
        -------
        - Node or Socket
        """
        if len(attributes) == 0:
            attrs = {'attribute': attribute}
        else:
            if attribute is None:
                attrs = attributes
            else:
                attrs = {'attribute': attribute, **attributes}

        node = Node('Capture Attribute', {'Geometry': self._geo, **attrs})

        #node._set_items('capture_items', **attrs)
        self._jump(node._out)
        return node.socket_by_index('OUTPUT', 1)

        if len(attrs) == 1:
            return node.socket_by_index(1)
        else:
            return node

    # ----------------------------------------------------------------------------------------------------
    # Capture a single attribute
    # ----------------------------------------------------------------------------------------------------

    def capture(self, attribute=None, **attributes):
        """ > Node <&Node Capture Attribute>

        [&JUMP]

        > Short name for <#capture_attribute>

        Arguments
        ---------
        - attribute (Socket) : first attribute to capture
        - **attributes (Sockets): named attributes to capture

        Returns
        -------
        - Node or Socket
        """
        return self.capture_attribute(attribute=attribute, **attributes)
    
    # ====================================================================================================
    # Loop
    # ====================================================================================================

    def for_each_element(self, named_sockets: dict={}, **sockets):
        """ Simulation zone

        Arguments
        ---------
        - named_socket (dict) : named sockets
        - sockets (dict) : other sockets

        Returns
        -------
        - ZoneIterator
        """

        # Selecton socket
        if "selection" not in [k.lower() for k in {**named_sockets, **sockets}.keys()]:
            named_sockets = {"Selection": self.get_selection(), **named_sockets}

        # Node Zone
        node = ZoneNode('For Each Element', self._geo, named_sockets=named_sockets, domain=self.DOMAIN_NAME, **sockets)

        return ZoneIterator(self, node)

    def for_each(self, named_sockets: dict={}, **sockets):
        return self.for_each_element(named_sockets=named_sockets, **sockets)
    
    def foreach(self, named_sockets: dict={}, **sockets):
        return self.for_each_element(named_sockets=named_sockets, **sockets)
    
    

            
