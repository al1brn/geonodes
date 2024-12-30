#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : socket_class
--------------------
- Provides the base class for data socket Socket which wraps an output socket of a Node
- Implement simple Data Sockets:

classes
-------
- NodeCache     : Interface for Socket and Domain which can cache created nodes
- Socket        : Wraps the output socket of node and exposes nodes creation as methods or properties
- Attribute   : Socket subtype for sockets representing a value (i.e. attributes)
- String        : Socket of type 'STRING'
- Material      : Socket of type 'MATERIAL'
- Image         : Socket of type 'IMAGE'
- Object        : Socket of type 'OBJECT'
- Collection    : Socket of type 'COLLECTION'
- Menu          : Socket of type 'MENU'
- TextureRoot   : Socket of type 'TEXTURE'

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import numpy as np

import bpy
import mathutils

from .scripterror import NodeError
from . import constants
from . import utils
from .treeclass import Tree, Node


# =============================================================================================================================
# =============================================================================================================================
# Node cache interface
# =============================================================================================================================
# =============================================================================================================================

class NodeCache:

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

    """
    def _cache_node(self, node, name=None):
        # Cache a node without building it
        if name is None:
            name = node.name
        self._cached_nodes[name] = node

        return node
    """

# =============================================================================================================================
# =============================================================================================================================
# Data Socket root
# =============================================================================================================================
# =============================================================================================================================

class Socket(NodeCache):

    SOCKET_TYPE = None

    # ====================================================================================================
    # Initialization

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

        Arguments
        ---------
        - socket (NodeSocket) : the output socket to wrap
        """
        self._tree = Tree.current_tree

        # ----- Socket is the name of an attribute

        if isinstance(socket, str):
            raise NodeError(f"Socket '{self._class_name}' is not an attribute. Impossible to create a named attribute '{socket}'")

        # ----- Socket is a socket :-)

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Impossible to initialize Socket with a non socket argument: {socket}", socket_type=self.SOCKET_TYPE)
        else:
            self._bsocket = bsocket

        self._reset()

    def _reset(self):
        self._cache_reset()

    def _jump(self, socket, reset=True):
        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Socket error: Impossible to jump to socket {socket}")

        self._bsocket = bsocket
        if reset:
            self._reset()
        return self

    @classmethod
    @property
    def _class_name(cls):
        return cls.__name__.split('.')[-1]

    @classmethod
    @property
    def _is_attribute(cls):
        return self.class_name in constants.ATTRIBUTE_CLASSES

    def __str__(self):
        return f"<{self._class_name} {self.SOCKET_TYPE} [{self.node._bnode.name}].'{self._bsocket.name}'>"

    #def __str__(self):
    #    return f"<Socket {self.SOCKET_TYPE} [{self.node._bnode.name}].'{self._bsocket.name}'>"

    # ====================================================================================================
    # Socket type to data type conversion, depending on the nodes

    @classmethod
    def socket_type(cls, restrict_to=None, default=None):
        return utils.get_socket_type(cls, restrict_to=restrict_to, default=default)

    @classmethod
    def data_type(cls, restrict_to=None, default='FLOAT'):
        return utils.get_data_type(cls, restrict_to=restrict_to, default=default)

    @classmethod
    def input_type(cls, restrict_to=None, default='FLOAT'):
        return utils.get_input_type(cls, restrict_to=restrict_to, default=default)

    @classmethod
    def get_socket_class(cls, value):

        socket_type = utils.get_socket_type(value)

        if Tree.is_geonodes:
            from . import Boolean, Integer, Float, Vector, Rotation, Matrix, Color, String, Menu, Geometry
            from . import Material, Image, Object, Collection, Texture
            from . import Mesh, Curve, Cloud, Volume, Instances
            socket_class = {
                'BOOLEAN': Boolean, 'INT': Integer, 'VALUE': Float,
                'VECTOR': Vector, 'ROTATION': Rotation, 'MATRIX': Matrix, 'RGBA': Color,
                'STRING': String, 'MENU': Menu,
                'GEOMETRY': Geometry,
                'MATERIAL': Material, 'IMAGE': Image, 'OBJECT': Object,
                'COLLECTION': Collection, 'TEXTURE': Texture,
                }
            return socket_class[socket_type]

        elif Tree.is_shader:
            from geonodes import Float, Vector, Color, String, Shader

            socket_class = {
                'VALUE': Float, 'VECTOR': Vector, 'RGBA': Color,
                'STRING': String, 'SHADER': Shader,
                }
            return socket_class[socket_type]
        else:
            assert(False)

    # ----- Math modul

    @classmethod
    @property
    def math(cls):
        from . import gnmath
        return gnmath

    # ====================================================================================================
    # Owning node

    @property
    def node(self):
        """ Returns the node owning the socket.

        Returns
        -------
        - Node
        """
        for node in self._tree._nodes:
            if node._bnode == self._bsocket.node:
                return node
        return None

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
    # New in 4.3 : pin gizmo

    @property
    def pin_gizmo(self):
        return self._bsocket.pin_gizmo

    @pin_gizmo.setter
    def pin_gizmo(self, value):
        self._bsocket.pin_gizmo = value

    # =============================================================================================================================
    # Dynamic attributes
    # Syntax:
    # - Terminated by _ (value_) : peer socket
    # - Starting by _ and a Capital : Named Attribute

    def __getattr__(self, name):

        # ----- Named attribute

        attr_name = utils.get_attr_name(name)
        if attr_name is not None:
            if self.SOCKET_TYPE == 'GEOMETRY':
                return self._tree.get_named_attribute(prop_name=name)
            else:
                raise AttributeError(f"Class '{self._class_name}' doesn't support Named Attributes: impossible to get named attribute '{attr_name}' ({name}).")

        # ----- Not terminated by _

        if not (len(name) > 1 and name[-2] != '_' and name[-1] == '_'):

            # ----- Specific message for socket._out which is a dynamic attribute of Node

            if name == '_out':
                msg = "Node / Socket confusion: you tried to access to the default output socket of a node, "
                msg += f"but class {type(self).__name__} is a socket"
                raise NodeError(msg)

            # ----- Error

            raise AttributeError(f"Class {type(self).__name__} as no property named '{name}'")

        # ----- Peer socket

        return getattr(self.node, name[:-1])

    def __setattr__(self, name, value):
        attr_name = utils.get_attr_name(name)
        if attr_name is not None:
            if self.SOCKET_TYPE == 'GEOMETRY':
                raise AttributeError(f"Named attributes can't be store directly in geometry, use a domain: impossible to store named attribute '{attr_name}' ({name}) in class '{type(self).__name__}'.")
            else:
                raise AttributeError(f"Only domains support Named Attributes: impossible to store named attribute '{attr_name}' ({name}) in class '{type(self).__name__}'.")

        return super().__setattr__(name, value)

    # =============================================================================================================================
    # Test a value in a list

    @staticmethod
    def check_in_list(value, valids, context=""):
        if value in valids:
            return True
        raise NodeError(f"{context} value error: '{value}' is not valid.", valids=valids)

    # =============================================================================================================================
    # Node data type value

    def get_node_data_type(self, node_name, value='SELF', default=None):

        return utils.get_node_data_type(node_name, self._tree._btree.bl_idname, self if value=='SELF' else value, default=default)

        # OLD

        blid = utils.get_node_bl_idname(node_name, self._tree._btree.bl_idname)
        valids = list(constants.NODE_DATA_TYPES[blid].values())[0]

        if self.SOCKET_TYPE in valids.keys():
            return valids[self.SOCKET_TYPE]

        if default is None:
            raise NodeError(f"Node '{node_name}' doesn't accept '{self.SOCKET_TYPE}' data type, only {list(valids)}")

        return default

    # =============================================================================================================================
    # To output

    def out(self, name=None):
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
        tree = self._tree
        bl_idname = self._bsocket.bl_idname
        if name is None:
            name = self.input_type().title()

        # ----------------------------------------------------------------------------------------------------
        # Output socket creation if
        # - It doesn't already exist
        # - The tree is not a group

        if self.SOCKET_TYPE == 'GEOMETRY':
            tree = Tree.current_tree
            if not(tree._interface.has_out_geometry or tree._is_group):
                tree.set_output_geometry(self, name)
                return

        # ----------------------------------------------------------------------------------------------------
        # New output socket

        bsocket = tree.new_output(bl_idname, name)
        tree.link(self, bsocket)

    # =============================================================================================================================
    # Constructors

    # -----------------------------------------------------------------------------------------------------------------------------
    # Menu switch

    @staticmethod
    def _geometry_class(geometries):
        geo_class = None
        for geo in geometries:
            if geo is None:
                continue
            if utils.get_socket_type(geo) != 'GEOMETRY':
                return None
            if geo_class is None:
                geo_class = type(geo)
            else:
                if not isinstance(geo, geo_class):
                    return None
        return geo_class

    @classmethod
    def MenuSwitch(cls, items={'A': None, 'B': None}, menu=0, name="Menu", tip=None):
        """ > Node <&Node Menu Switch>

        The items of the Menu Switch node are provided in the 'items' dict.
        An group input socket named after the 'name' argument is linked to menu selector.

        ``` python
        with GeoNodes("Menu Switch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = Geometry.MenuSwitch({"Input": geo, "Cube": cube, "Sphere": sphere, "Cone": cone}, menu="Cube")

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - items (dict) : menu names and values
        - menu (int or str) : index or name of the default value
        - name (str = 'Menu') : name of the group input socket
        - tip (str = None) : user tip

        Returns
        -------
        - Socket
        """

        # Create the node

        node = Node('Menu Switch', data_type=cls.input_type())

        # Set the items

        node._set_items(items, clear=True)

        # Plug the menu

        if isinstance(menu, int):
            menu = list(items.keys())[menu]

        menu_socket = Tree.new_input('NodeSocketMenu', name=name, value=None, description=tip)
        node.plug_value_into_socket(menu_socket, node.in_socket('Menu'))
        Tree.current_tree.set_input_socket_default(menu_socket, menu)

        # Done

        return cls(node._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Index switch

    @classmethod
    def IndexSwitch(cls, *values, index=0):
        """ > Node <&Node Index Switch>

        ``` python
        with GeoNodes("Index Switch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=Integer(2, 'Index'))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer) : socket 'Index' (Index)

        Returns
        -------
        - Socket
        """

        # ----- Create the nodes

        node = Node('Index Switch', data_type=cls.input_type())

        # ----- Create the items

        enum_items = node._bnode.index_switch_items
        for i, item in enumerate(list(values)):

            # ----- Create the socket

            if i >= len(enum_items):
                enum_items.new()

            # ----- Plug the value

            node.plug_value_into_socket(item, node.in_socket(1 + i))

        # ----- Plug the index

        node.plug_value_into_socket(index, node.in_socket('Index'))

        # ----- Done

        return cls(node._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Switch

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
        return cls(Node('Switch', {'Switch': condition, 'False': false, 'True': true}, input_type=cls.input_type(default='GEOMETRY'))._out)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Method versions

    def menu_switch(self, self_name='A', items={'B': None}, menu=0, name="Menu", tip=None):
        """ > Node <&Node Menu Switch>

        [&NO_JUMP]

        Self is connected to the first menu item with the name provided as argument.

        ``` python
        with GeoNodes("Menu Switch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = geo.menu_switch("Input", {"Cube": cube, "Sphere": sphere, "Cone": cone}, menu="Cube")

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - self_name (str = 'A') : name to use
        - items (dict) : other menu names and values
        - menu (int or str) : index or name of the default value
        - name (str = 'Menu') : name of the group input socket
        - tip (str = None) : user tip

        Returns
        -------
        - Socket
        """
        return self.MenuSwitch({self_name: self, **items}, menu=menu, name=name, tip=tip)

    def index_switch(self, *values, index=0):
        """ > Node <&Node Index Switch>

        [&NO_JUMP]

        Self is used as first socket in the node.

        ``` python
        with GeoNodes("Index Switch demo"):

            # Create some geometries
            geo    = Geometry()
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()
            cone   = Mesh.Cone()

            # Pick in this list
            pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=Integer(2, 'Index'))

            # Plug the result to the output
            pick_geo.out()
        ```

        Arguments
        ---------
        - *values : list of Sockets to select into
        - index (Integer) : socket 'Index' (Index)

        Returns
        -------
        - Socket
        """
        return self.IndexSwitch(self, *values, index=index)

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

        > [!NOTE]
        > This method let self socket unchanged. To set self socket to the result

        Arguments
        ---------
        - condition (Boolean) : socket 'Switch' (Switch)
        - false : socket 'False' (False)
        - true : socket 'True' (True)

        Returns
        -------
        - Socket
        """
        return self.Switch(condition=condition, false=self, true=true)

    # ====================================================================================================
    # Run tests

    @classmethod
    def _run_tests(cls):

        from geonodes import GeoNodes

        import inspect
        import re
        from geonodes.core import constants

        tree = None

        # ----------------------------------------------------------------------------------------------------
        # Test Function

        def test_func(f_name, f):
            expr = r"<&Node *(?P<name>[^>]*)>"

            if f.__doc__ is None:
                return "No doc"

            m = re.search(expr, f.__doc__, flags=re.MULTILINE)
            if m is None:
                return "No node"

            node_name = m.group('name')
            if node_name.lower() not in constants.NODE_NAMES[tree._btree.bl_idname]:
                return f"Not in {tree._btree.bl_idname}"
            node = Node(node_name)

            argspec = inspect.getfullargspec(f)
            call = []
            used_args = []
            i_offset = len(argspec.args) if argspec.defaults is None else len(argspec.args) - len(argspec.defaults)
            for i, arg_name in enumerate(argspec.args):

                if arg_name in ('self', 'cls'):
                    continue

                i_def = i - i_offset
                if i_def < 0:
                    return "*args"
                    call.append("Boolean()")
                    used_args.append(arg_name)
                    continue

                if node.in_socket(arg_name, halt=False) is None:
                    continue

                if argspec.defaults[i_def] is None:
                    call.append(f"{arg_name}=Integer(123)")
                    used_args.append(arg_name)

            # ----- Test

            code = f"from geonodes import *\n{cls.__name__}(Float(10)).{f_name}({', '.join(call)})"
            try:
                exec(code, globals(), None)
            except Exception as e:
                print()
                print("ERROR in")
                print('-'*100)
                print(code)
                print('-'*100)
                return e

            return "Ok : (" + ", ".join(used_args) + ')'

        # ----------------------------------------------------------------------------------------------------
        # Loop

        tree = GeoNodes("TEST")

        print(f"Testing {cls.__name__}...")

        for name in dir(cls):
            m = getattr(cls, name)
            f = None
            if inspect.isfunction(m):
                f = m

            elif inspect.ismethod(m):
                f = m.__func__

            elif isinstance(m, property):
                continue
                if m.fget is not None:
                    print(f"{cls.__name__ + '.' + name:25s} - GETTER")
                    print(m.fget)
                    print("  ", inspect.getfullargspec(m.fget))
                if m.fset is not None:
                    print(f"{cls.__name__ + '.' + name:25s} - SETTER")
                    print(m.fset)
                    print("  ", inspect.getfullargspec(m.fset))

                continue

            else:
                continue

            print(f".  - {name:25s}", end = "")
            e = test_func(name, f)
            if isinstance(e, Exception):
                print("ERROR")
                raise (e)
            print(e)

        tree.pop()
