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

module : socket_class
---------------------
- Socket

This class is the base class for all data socket actually used in ***geonodes***.

The primary purpose of a socket is to maintain a reference to the output socket of
a node.

It implements fundamental mechanisms such as:
- caching nodes
- jump
- access to node
- node label and color
- access to interface tree for input socket

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


from .scripterror import NodeError
from .import constants
from .import utils
from .utils import Break
from .sockettype import SocketType
from .treeinterface import TreeInterface
from .treeclass import Tree
from .nodeclass import Node
from .nodezone import ZoneNode,ZoneIterator

# =============================================================================================================================
# =============================================================================================================================
# Node cache interface
# =============================================================================================================================
# =============================================================================================================================

class NodeCache:

    __slots__ = ['_cached_nodes']

    # ====================================================================================================
    # Cache mechanism
    # Nodes can be directly created or created through a cache mechanism
    # - node = Node(...)
    # - node = self._cache(...)
    # The cache is erased with _reset
    # The cache is optionnally erased when a jump occurs
    # It is up to the true class to call _cache_reset

    def _cache_reset(self):
        self._cached_nodes = {}

    def _cache(self, name, sockets={}, cache_name=None, **parameters):

        # build a node if not in cache

        if cache_name is None:
            cache_name = name

        # ----- Is the node already in cache
        node = self._cached_nodes.get(cache_name)
        if node is not None:
            return node

        # ----- No : we create it and put is in cache
        node = Node(name, sockets, **parameters)
        self._cached_nodes[cache_name] = node

        return node

# =============================================================================================================================
# =============================================================================================================================
# Data Socket root
# =============================================================================================================================
# =============================================================================================================================

class Socket(NodeCache):

    __slots__ = NodeCache.__slots__ + ['_tree', '_bsocket', '_socket_type', '_layout', '_use_layout']

    SOCKET_TYPE = None

    # ====================================================================================================
    # Initialization
    # ====================================================================================================

    def __init__(self, socket):
        """ > The output socket of a <!Node>

        **Socket** is the base class for data classes such as <!Float>, <!Image> or <!Geometry>.

        It refers to an **output** socket of a <!Node>. A socket can be set to the **input** socket
        of another <!Node> to create a link between the two nodes:

        ``` python
        # cube is the output socket 'Mesh' of the node 'Cube'
        cube = Node("Cube").mesh

        # cube is set the to socket 'geometry' of node 'Set Position'
        node = Node("Set Position")
        node.geometry = cube
        ```

        > [!IMPORTANT]
        > You can access to the other output sockets of the node in two different ways:
        > - using <#node> attribute
        > - using ***peer socket** naming convention where the **snake_case** name of
        >.  the other sockets is suffixed by '_'

        The example below shows how to access the to 'UV Map' socket of node <*Node Cube>:

        ``` python
        # cube is the output socket 'Mesh' of the node 'Cube'
        cube = Mesh.Cube()

        # Getting 'UV Map' through the node
        uv_map = cube.node.uv_map

        # Or using the 'peer socket' naming convention
        uv_map = cuve.uv_map_
        ```

        Arguments
        ---------
        - socket (NodeSocket) : the output socket to wrap
        """

        # ---------------------------------------------------------------------------
        # Layout
        # ---------------------------------------------------------------------------

        self._layout      = None
        self._use_layout  = True

        # ---------------------------------------------------------------------------
        # Tree
        # ---------------------------------------------------------------------------
        
        self._tree = Tree.current_tree()

        # ---------------------------------------------------------------------------
        # Socket
        # ---------------------------------------------------------------------------

        # Attribute initiliazd by name

        if isinstance(socket, str):
            raise NodeError(f"Socket '{type(self).__name__}' is not an attribute. Impossible to create a named attribute '{socket}'")

        # Socket is a socket :-)

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Impossible to initialize Socket with a non socket argument: {socket}", socket_type=self.SOCKET_TYPE)

        self._bsocket = bsocket

        # Initialize socket type frpm socket if the same types
        # otherwise it is a socket transtypage

        stype = SocketType(bsocket)
        if stype == self.SOCKET_TYPE:
            self._socket_type = stype
        else:
            self._socket_type = SocketType(self.SOCKET_TYPE)

        self._reset()

    # ====================================================================================================
    # Utilities
    # ====================================================================================================

    def __str__(self):
        stype = self._socket_type.class_name if hasattr(self, '_socket_type') else "Node Type"
        node = self.node
        if node is None:
            snode_name = "No Node"
            sname      = "No Socket"
        else:
            snode_name = self.node._bnode.name
            sname      = self._bsocket.name

        return f"<{stype} [{snode_name}].'{sname}'>"

    # ----------------------------------------------------------------------------------------------------
    # Reset cache
    # ----------------------------------------------------------------------------------------------------

    def _reset(self):
        self._cache_reset()

    # ----------------------------------------------------------------------------------------------------
    # Jump to another output socket
    # ----------------------------------------------------------------------------------------------------

    def _jump(self, socket, reset=True):

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Socket error: Impossible to jump to socket {socket}")
        
        self._bsocket = bsocket
        if reset:
            self._reset()

        return self
    
    # ----------------------------------------------------------------------------------------------------
    # Geometry from domain
    # ----------------------------------------------------------------------------------------------------

    @property
    def _domain_to_geometry(self):
        return self

    # ----------------------------------------------------------------------------------------------------
    # Get the interface socket (for Group node or tree input / output)
    # ----------------------------------------------------------------------------------------------------

    @property
    def _interface_socket(self):
        """ Return the interface socket if exists

        An interface socket exists when the socket a tree input or output socket or
        when it is the socket of a group

        Returns
        -------
        - Interface Socket
        """
        if self.node.use_interface:
            return self.node._interface._use_interface(self._bsocket.identifier)
        
        return None

    # ----------------------------------------------------------------------------------------------------
    # Name or label
    # ----------------------------------------------------------------------------------------------------

    @property
    def node(self):

        # Not yet initialized
        if not hasattr(self, '_bsocket'):
            return None
        
        for node in self._tree._nodes:
            if node._bnode == self._bsocket.node:
                return node
            
        assert False, f"Shouldn't happen, {self._bsocket=}, {self._bsocket.node=}"

    # ----------------------------------------------------------------------------------------------------
    # Name or label
    # ----------------------------------------------------------------------------------------------------

    @property
    def _name(self):
        """ Return the name or the label

        Returns
        -------
        - str : default is ""
        """
        return utils.get_socket_name(self._bsocket)

    # ----------------------------------------------------------------------------------------------------
    # Get the panel name
    # ----------------------------------------------------------------------------------------------------

    @property
    def _panel_name(self):
        """ Return the name of the panel

        Returns
        -------
        - str : default is ""
        """
        i_socket = self._interface_socket
        if i_socket is None:
            return ""
        
        names = []
        cur = i_socket
        while True:
            if cur.parent.name == "":
                break
            names.append(cur.parent.name)
            cur = cur.parent

        return " > ".join(reversed(names))

    # ====================================================================================================
    # Default value property
    # ====================================================================================================

    @property
    def default_value(self):
        if not hasattr(self._bsocket, 'default_value'):
            raise NodeError(f"Socket {self} has not default value.")
        
        return self._bsocket.default_value
    
    @default_value.setter
    def default_value(self, value):
        if not hasattr(self._bsocket, 'default_value'):
            raise NodeError(f"Socket {self} has not default value.")
        
        self._bsocket.default_value = value

        # ----- Interface
        i_socket = self._interface_socket
        if i_socket is not None:
            i_socket.default_value = value

    # ====================================================================================================
    # Get a group input from its name and panel
    # ====================================================================================================

    @classmethod
    def Input(cls, name: str, panel: str = ""):
        """ Get an group input from its name and panel

        This constructor is used to get a tree input socket which has been previously created.

        This is typically used after connecting a group node to the tree inputs:

        ``` python
        with GeoNodes("Geometry Nodes"):
            # Create an input socket

            param = Float(1., "My Parameter")

            # Call a group, the 'link_from' argument creates the necessary inputs in "Geometry Nodes"

            node = Group("Function Group", link_from='TREE')

            # Let's suppose that the 'Function Group' has created an Integer socket named "Int Parameter"
            # If we need it, we can get it with

            int_parameter =  Integer.Input("Int Parameter")
        ```

        Raises
        ------
        - NodeError if socket is not found

        Arguments
        ---------
        - name : socket name
        - panel : panel name

        Returns
        -------
        - Socket
        """
        return cls(Tree.current_tree().get_in_socket(name=name, panel=panel))


    # ====================================================================================================
    # Grid
    # ====================================================================================================

    @property
    def is_grid(self):
        """ bool property
        
        Returns True if socket is a grid (inferred_structure_type == 'GRID').
        """
        return self._bsocket.inferred_structure_type == 'GRID'

    # ====================================================================================================
    # Owning node
    # ====================================================================================================

    @property
    def node_color(self):
        """ Node color

        Returns
        -------
        - mathutils.Color
        """
        return self.node._color

    @node_color.setter
    def node_color(self, value):
        self.node._color = value

    @property
    def node_label(self):
        """ Node Label

        Returns
        -------
        - str
        """
        return self.node._label

    @node_label.setter
    def node_label(self, value):
        self.node._label = value

    # To chain in a short way
    def _lc(self, label=None, color=None):
        """ Set node label and color.

        This method returns self to be chained to as socket:

        ``` python
        with GeoNodes("Node label and color"):
            Geometry().out()

            a = Float(10)._lc("Var a")
            b = Float(10)._lc("Var b")
            c = (a + b)._lc("a + b", (1, 0, 0))
        ```

        Arguments
        ---------
        - label (str = None) : node label
        - color (color = None) : node color

        Returns
        -------
        - self
        """

        node = self.node
        node._label = label
        node._color = color
        return self

    def _lcop(self, label=None):
        return self._lc(label=label, color='OPERATION')

    # =============================================================================================================================
    # Link node from
    # =============================================================================================================================

    def link_from(self, **params):
        self.node.link_from(**params)
        return self

    # =============================================================================================================================
    # Gizmo
    # =============================================================================================================================

    @property
    def pin_gizmo(self):
        return self._bsocket.pin_gizmo

    @pin_gizmo.setter
    def pin_gizmo(self, value):
        self._bsocket.pin_gizmo = value

    # ====================================================================================================
    # Dynamic attributes
    # Can be either a named attribute or a sibling socket
    # - peer socket: _ and a name starting with a Capital
    # - sibling socket : the socket name or socket named ended with _
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Get attr
    # ----------------------------------------------------------------------------------------------------

    def __getattr__TEST(self, name):

        print("SOCKET GET ATTR", name)

        # ---------------------------------------------------------------------------
        # Named attribute : _ followed by a capital, e.g. : socket._Attribute
        # ---------------------------------------------------------------------------

        attr_name = utils.get_attr_name(name)
        if attr_name is not None:
            if self.SOCKET_TYPE == 'GEOMETRY':
                return self._tree.get_named_attribute(prop_name=name)
            else:
                raise AttributeError(f"Class '{type(self)}' doesn't support Named Attributes: impossible to get named attribute '{attr_name}' ({name}).")

        # ---------------------------------------------------------------------------
        # Could by a sibling output socket
        # ---------------------------------------------------------------------------

        #out_socket = self.node.by_name('OUTPUT', name, as_argument=True, halt=False)
        #if out_socket is not None:
        #    return out_socket

        # ---------------------------------------------------------------------------
        # Sibling socket : ends with _, e.g. : socket.value_
        # ---------------------------------------------------------------------------

        if len(name) > 1 and name[-2] != '_' and name[-1] == '_':
            return getattr(self.node, name[:-1])

        # ---------------------------------------------------------------------------
        # Specific error message for '_out'
        # ---------------------------------------------------------------------------

        if name == '_out':
            msg = "Node / Socket confusion: you tried to access to the default output socket of a node, "
            msg += f"but class {type(self).__name__} is a socket"
            raise NodeError(msg)

        # ---------------------------------------------------------------------------
        # Attribute not found
        # ---------------------------------------------------------------------------

        raise NodeError(f"Class {type(self).__name__} as no property named '{name}'", keyword=name)
    
    # ----------------------------------------------------------------------------------------------------
    # Set attr
    # ----------------------------------------------------------------------------------------------------

    def __setattr__OLD(self, name, value):

        # Do we keep that complex sttuff ?

        attr_name = utils.get_attr_name(name)
        
        if attr_name is not None:
            msg = f"Impossible to store named attribute '{attr_name}' ({name}) in class '{type(self).__name__}'"
            if self.SOCKET_TYPE == 'GEOMETRY':
                raise NodeError(f"{msg}: named attributes can't be stored directly in geometry, use a domain.",
                    keyword=(name, attr_name))
            else:
                raise NodeError(f"{msg}: only domains support Named Attributes.", keyword=(name, attr_name))

        return super().__setattr__(name, value)

    # ====================================================================================================
    # Test a value in a list
    # ====================================================================================================

    @staticmethod
    def check_in_list(value, valids, context=""):
        if value in valids:
            return True
        raise NodeError(f"{context} value error: '{value}' is not valid.", valids=valids)
    
    # ====================================================================================================
    # To output
    # ====================================================================================================

    def out(self, name: str = None, panel: str = "", **props):
        """ Plug the value to the Group Output Node.

        ``` python
        with GeoNodes("Plug to group output"):
            # Create a cube
            geo = Mesh.Cube()
            # To Group Output geometry as socket named "Cube"
            geo.out("Cube")
        ```

        The "Do nothing" modifier is simply ``` Geometry().out() ```

        Arguments
        ---------
        - name (str = None) : socket name

        Returns
        -------
        - None
        """
        #print("OUTING", self._bsocket.name, self._bsocket.type)
        out_node = self._tree.get_output_node()
        out_node.set_input_socket(name=name, value=self, create=True, panel=panel, **props)

    # ====================================================================================================
    # Context management
    # ====================================================================================================

    def _push(self):

        from .treeclass import Layout

        self.node._push()

        # Push a Layout dedicated this context
        # (will be removed by arrange if no node is created)
        if self._use_layout:
            self._layout = Layout()
            self._layout.push()

    def _pop(self, error: bool = False):

        self.node._pop(error)

        # Pop inout capture and layout
        if self._use_layout:
            self._layout.pop()

    def __enter__(self):
        self._push()
        return self
    
    def __exit__(self, type, exc_value, traceback):
        ok = exc_value is None or isinstance(exc_value, Break)
        self._pop(not ok)
    
    # ====================================================================================================
    # Menu Switch
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constructor version
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def MenuSwitch(cls, 
                   named_sockets: dict = {},
                   **sockets):
        """ > Node <&Node Menu Switch>

        The items of the Menu Switch node are provided in the 'items' dict.

        Arguments
        ---------
        - named_sockets (dict = {}) : sockets to create
        - sockets (dict) : items

        Returns
        -------
        - Socket
        """
        node = Node('Menu Switch',
                named_sockets = named_sockets,
                data_type = SocketType(cls.SOCKET_TYPE).type,
                **sockets)
        
        return cls(node._out)
    
    # ----------------------------------------------------------------------------------------------------
    # Method version
    # ----------------------------------------------------------------------------------------------------

    def menu_switch(self,
                self_name: str = 'Self', 
                named_sockets: dict = {},
                default_value: str = None,
                **sockets):
        """ > Node <&Node Menu Switch>

        [&NO_JUMP]

        Self is connected to the first menu item with the name provided as argument.

        The items of the Menu Switch node are provided in the 'items' dict.
        An group input socket named after the 'name' argument is linked to menu selector.

        Arguments
        ---------
        - named_sockets (dict = {}) : sockets to create
        - sockets (dict) : items

        Returns
        -------
        - Socket
        """        
        return self.MenuSwitch(
            named_sockets = {self_name: self, **named_sockets},
            **sockets)
    
    # ====================================================================================================
    # Index Switch
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constructor version
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def IndexSwitch(cls, *values, index = None):
        """ > Node <&Node Index Switch>

        ``` python
        with GeoNodes("IndexSwitch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=tree.new_input("Geometry index", default_value=2))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer = None) : socket 'Index' (Index)

        Returns
        -------
        - Socket
        """
        #return IndexSwitchNode(*values, index=index, data_type=cls.input_type())._out
        return Node('Index Switch', {str(i): value for i, value in enumerate(values)}, data_type=cls.SOCKET_TYPE, Index=index)._out
    
    # ----------------------------------------------------------------------------------------------------
    # Method version
    # ----------------------------------------------------------------------------------------------------

    def index_switch(self, *values, index = None):
        """ > Node <&Node Index Switch>

        ``` python
        with GeoNodes("index_switch demo") as tree:

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = geo.index_switch(cube, sphere, cone, index=tree.new_input("Geometry index", default_value=2))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer = None) : socket 'Index' (Index)

        Returns
        -------
        - Socket
        """
        return self.IndexSwitch(self, *values, index=index)
    
    # ====================================================================================================
    # Switch
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Constructor version
    # ----------------------------------------------------------------------------------------------------

    @classmethod
    def Switch(cls, condition=None, false=None, true=None):
        """ > Node <&Node Switch>

        ``` python
        with GeoNodes("Switch demo"):

            # Two possible geometries
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()

            # Select
            geo = Geometry.Switch(Boolean(True, "Use Sphere"), cube, sphere)

            # To group output
            geo.out()
        ```

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - false : socket 'False' (False)
        - true : socket 'True' (True)

        Returns
        -------
        - Socket
        """
        return Node('Switch', {'Switch': condition, 'False': false, 'True': true}, input_type=cls.SOCKET_TYPE)._out

    # ----------------------------------------------------------------------------------------------------
    # Method version
    # ----------------------------------------------------------------------------------------------------

    def switch(self, condition=None, true=None):
        """ > Node <&Node Switch>

        [&NO_JUMP]

        Self is connected to 'false' socket.

        ``` python
        with GeoNodes("Switch demo"):

            choice = Boolean(True, "Use Sphere")

            # Two possible geometries
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()

            # Select
            geo = cube.switch(choice, sphere)

            # To group output
            geo.out()
        ```

        Information
        -----------
        - Socket 'False' : self

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - true : socket 'True' (True)

        Returns
        -------
        - Socket
        """
        return self.Switch(condition=condition, false=self, true=true)
    
    # ----------------------------------------------------------------------------------------------------
    # Alternative method version
    # ----------------------------------------------------------------------------------------------------

    def switch_false(self, condition=None, false=None):
        """ > Node <&Node Switch>

        [&NO_JUMP]

        Self is connected to 'true' socket.

        > [!IMPORTANT]
        > This methods behaves the inverse of <#switch> : self is connected to "True" socket and  the argument to "False", socket

        > [!NOTE]
        > This method is mainly provided to cover the case when 'False' socket is None

        ``` python
        with GeoNodes("Switch demo"):

            geo = Geometry()

            show_geometry = Boolean(False, "Merge with Cube")

            cube = Mesh.Cube()

            geo += cube.switch_false(show_geometry)

            # Is equivalent to
            geo += Geometry.Switch(show_geometry, None, cube)

            # To group output
            geo.out()
        ```

        > [!NOTE]
        > This method let self socket unchanged. To set self socket to the result

        Information
        -----------
        - Socket 'True' : self

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - false : socket 'False' (False)

        Returns
        -------
        - Socket
        """
        return self.Switch(condition=condition, false=false, true=self)
    
    # ====================================================================================================
    # Loops
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Repeat
    # ----------------------------------------------------------------------------------------------------

    def repeat(self, iterations=1, named_sockets: dict={}, **sockets):
        """ Repeat zone

        Arguments
        ---------
        - Iteration (Integer = 1) : iteration socket
        - named_socket (dict) : named sockets
        - sockets (dict) : other sockets

        Returns
        -------
        - ZoneIterator
        """
        node = ZoneNode("Repeat", self, named_sockets=named_sockets, **sockets)
        return ZoneIterator(self, node)
    
    # ----------------------------------------------------------------------------------------------------
    # Simulation
    # ----------------------------------------------------------------------------------------------------

    def simulation(self, named_sockets: dict={}, **sockets):
        """ Simulation zone

        Arguments
        ---------
        - named_socket (dict) : named sockets
        - sockets (dict) : other sockets

        Returns
        -------
        - ZoneIterator
        """
        node = ZoneNode("Simulation", self, named_sockets=named_sockets, **sockets)
        return ZoneIterator(self, node)


        




    # ====================================================================================================
    # Class Test
    # ====================================================================================================

    @staticmethod
    def _classes_test():

        from .utils import SOCKET_CLASSES
        from .geonodes import GeoNodes
        from .geometry_class import Geometry

        print()
        print("Socket._class_test...")
        print()

        with GeoNodes("Tree Inputs") as tree:

            inps = []
            vars = []

            for stype, klass in SOCKET_CLASSES.items():
                if stype == 'SHADER':
                    continue

                class_name = klass.__name__
                inps.append(klass(name=class_name))
                vars.append(klass())

            # Avoid error
            Geometry().out()

        for klass in SOCKET_CLASSES.values():
            if hasattr(klass, '_class_test'):
                print(f"Testing {klass}...")
                klass._class_test()

        print("Socket._class_test done.")

# ====================================================================================================
# Input socket
# ====================================================================================================

class Input(Socket):

    __slots__ = Socket.__slots__ + ['name', 'panel', 'props']

    SOCKET_TYPE = 'CUSTOM'

    def __init__(self, name: str = None, panel: str = "", **props):
        """ Input Socket wrapping an output virtual socket.

        When plugging to the input socket of a Node, a New socket is creaated.

        Arguments
        ---------
        - name (str = None) : the name to give to the output
        - panel (str = "") : the panel to create if possible
        - props (dict) : socket properties
        """

        innode = Tree.current_tree().get_input_node()

        bsocket = None
        for bsock in innode._bnode.outputs:
            if bsock.type == 'CUSTOM':
                bsocket = bsock
                break

        if bsocket is None:
            raise RuntimeError(f"Impossible to initialize an Input socket: no output virtual socket found in node {innode}.")
        
        super().__init__(bsocket)

        self.name  = name
        self.panel = panel
        self.props = {**props}



