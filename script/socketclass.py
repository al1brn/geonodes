#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : socketclass
--------------------
- Provides the base class for data socket DataSocket which wraps an output socket of a Node
- Implement simple Data Sockets:

classes
-------
- NodeCache     : Interface for DataSocket and Domain which can cache created nodes
- DataSocket    : Wraps the output socket of node and exposes nodes creation as methods or properties
- String        : DataSocket of type 'STRING'
- Material      : DataSocket of type 'MATERIAL'
- Image         : DataSocket of type 'IMAGE'
- Object        : DataSocket of type 'OBJECT'
- Collection    : DataSocket of type 'COLLECTION'
- Menu          : DataSocket of type 'MENU'

functions
---------

updates
-------
- creation : 2024/07/23
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

class DataSocket(NodeCache):
    """ DataSocket documentation
    """

    SOCKET_TYPE = None

    # ====================================================================================================
    # Initialization

    def __init__(self, socket):
        self._tree = Tree.current_tree

        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"Impossible to initialize DataSocket with a non socket argument: {socket}", socket_type=self.SOCKET_TYPE)
        else:
            self._bsocket = bsocket
        self._reset()

    def _reset(self):
        self._cache_reset()

    def _jump(self, socket, reset=True):
        bsocket = utils.get_bsocket(socket)
        if bsocket is None:
            raise NodeError(f"DataSocket error: Impossible to jump to socket {socket}")

        self._bsocket = bsocket
        if reset:
            self._reset()
        return self

    @classmethod
    @property
    def _class_name(cls):
        return cls.__name__.split('.')[-1]

    def __str__(self):
        return f"<{self._class_name} {self.SOCKET_TYPE} [{self.node._bnode.name}].'{self._bsocket.name}'>"

    #def __str__(self):
    #    return f"<DataSocket {self.SOCKET_TYPE} [{self.node._bnode.name}].'{self._bsocket.name}'>"

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

    # ----- Math modul

    @classmethod
    @property
    def math(cls):
        from geonodes.script import gnmath
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
        return self.node._color

    @node_color.setter
    def node_color(self, value):
        self.node._color = value

    @property
    def node_label(self):
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
    # Test a value in a list

    @staticmethod
    def check_in_list(value, valids, context=""):
        if value in valids:
            return True
        raise NodeError(f"{context} value error: '{value}' is not valid.", valids=valids)

    # =============================================================================================================================
    # To output

    def to_output(self, name=None):
        """ Plug a socket to an output socket.

        Arguments
        ---------
            - socket (Socket) : the socket to plug to the output
            - name (str = None) : output socket name
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
            if not(tree.has_output_geometry or tree._is_group):
                tree.set_output_geometry(self, name)
                return

        # ----------------------------------------------------------------------------------------------------
        # New output socket

        bsocket = tree.new_output(bl_idname, name)
        tree.link(self, bsocket)

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
        self.to_output(name)

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
        """ Node 'Menu Switch' (GeometryNodeMenuSwitch)

        [!Node] Menu Switch

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
        - output
        """

        # ----- Create the nodes

        node = Node('Menu Switch', data_type=cls.input_type())

        # ----- Create the items

        enum_items = node._bnode.enum_items
        menu_index = None
        for i, (menu_name, menu_value) in enumerate(items.items()):

            # ----- Create the socket

            if i < len(enum_items):
                enum_items[i].name = menu_name
            else:
                enum_items.new(menu_name)

            # ----- Is it the menu socket

            if isinstance(menu, str) and menu == menu_name:
                menu_index = i

            # ----- Plug the value

            node.plug_value_into_socket(menu_value, node.in_socket(1 + i))

        # ----- Plug the menu

        if isinstance(menu, int):
            menu_index = menu

        if menu_index is None:
            menu_index = 0

        menu_socket = utils.get_bsocket(menu)
        set_menu_index = False
        if menu_socket is None:
            #menu_socket = Tree.new_input('NodeSocketMenu', name=name, value=menu_index, description=tip)
            menu_socket = Tree.new_input('NodeSocketMenu', name=name, value=None, description=tip)
            set_menu_index = True

        node.plug_value_into_socket(menu_socket, node.in_socket('Menu'))
        if set_menu_index:
            Tree.current_tree.set_input_socket_default(menu_socket, list(items.keys())[menu_index])

        # ----- Geometry type

        res = node._out
        if cls.SOCKET_TYPE == 'GEOMETRY':
            geo_class = cls._geometry_class(list(items.values()))
            if geo_class is not None:
                res = geo_class(res)

        return res

    # -----------------------------------------------------------------------------------------------------------------------------
    # Index switch

    @classmethod
    def IndexSwitch(cls, *values, index=0):
        """ Node 'Index Switch' (GeometryNodeIndexSwitch)

        [!Node] Index Switch

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
        - *values : list of DataSockets to select into
        - index (Integer) : socket 'Index' (Index)

        Returns
        -------
        - DataSocket
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

        # ----- Geometry type

        res = node._out
        if cls.SOCKET_TYPE == 'GEOMETRY':
            geo_class = cls._geometry_class(list(values))
            if geo_class is not None:
                res = geo_class(res)

        return res

    # -----------------------------------------------------------------------------------------------------------------------------
    # Switch

    @classmethod
    def Switch(cls, condition=None, false=None, true=None):
        """ Node 'Switch' (GeometryNodeSwitch)

        [!Node] Switch

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
        - DataSocket
        """

        res = Node('Switch', {'Switch': condition, 'False': false, 'True': true}, input_type=cls.input_type(default='GEOMETRY'))._out

        if cls.SOCKET_TYPE == 'GEOMETRY':
            geo_class = cls._geometry_class([false, true])
            if geo_class is not None:
                res = geo_class(res)

        return res


    # -----------------------------------------------------------------------------------------------------------------------------
    # Method versions

    def menu_switch(self, self_name='A', items={'B': None}, menu=0, name="Menu", tip=None):
        """ Node 'Menu Switch' (GeometryNodeMenuSwitch)

        [!Node] Menu Switch

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
        - output
        """
        return self.MenuSwitch({self_name: self, **items}, menu=menu, name=name, tip=tip)

    def index_switch(self, *values, index=0):
        """ Node 'Index Switch' (GeometryNodeIndexSwitch)

        [!Node] Index Switch

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
        - *values : list of DataSockets to select into
        - index (Integer) : socket 'Index' (Index)

        Returns
        -------
        - output
        """

        return self.IndexSwitch(self, *values, index=index)

    def switch(self, condition=None, true=None):
        """ Node 'Switch' (GeometryNodeSwitch)

        [!Node] Switch

        Self is connected to 'false' socket.

        ``` python
        with GeoNodes("Switch demo"):

            # Two possible geometries
            cube   = Mesh.Cube()
            sphere = Mesh.IcoSphere()

            # Select
            geo = cube.switch(Boolean(True, "Use Sphere"), sphere)

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
        - output
        """
        return self.Switch(condition=condition, false=self, true=true)

    # ====================================================================================================
    # Methods

    def blur(self, iterations=None, weight=None):
        """ Node 'Blur Attribute' (GeometryNodeBlurAttribute)

        [!Node] Blur Attribute

        Arguments
        ---------
        - self : socket 'Value'
        - iterations (Integer) : socket 'Iterations' (Iterations)
        - weight (Float) : socket 'Weight' (Weight)

        Returns
        -------
        - value
        """

        data_type = self.data_type(['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR'])
        return Node('Blur Attribute', {'Value': self, 'Iterations': iterations, 'Weight': weight}, data_type=data_type)._out

# =============================================================================================================================
# =============================================================================================================================
# Root for value sockets : BOOLEAN, INT MATRIX RGBA ROTATION VALUE VECTOR
# =============================================================================================================================
# =============================================================================================================================

class ValueSocket(DataSocket):

    # =============================================================================================================================
    # Constructors

    @classmethod
    def NamedAttribute(cls, name):
        """ Node 'Named Attribute' (GeometryNodeInputNamedAttribute)

        [!Node] Named Attribute

        'Named' is a synonym of 'NamedAttribute'

        ``` python
        with GeoNodes("Named Attributes"):

            cube = Mesh.Cube()

            # Create a named attribute
            cube.points.store("Some Value", Float.Random(0, 1, seed=0))

            # Read the random value to offset along z
            cube.points.offset = (0, 0, Float.NamedAttribute("Some Value"))

            # Remove the named attribute
            cube.remove_named_attribute("Some*", exact=False)

            cube.out()
        ```

        Arguments
        ---------
        - name (String) : socket 'Name' (Name)

        Returns
        -------
        - DataSocket [exists_]
        """
        attribute = Node('Named Attribute', {'Name': name}, data_type=cls.data_type())._out
        attribute.exists_ = attribute.node.exists
        return attribute

    @classmethod
    def Named(cls, name):
        """ Node 'Named Attribute' (GeometryNodeInputNamedAttribute)

        [!Node] Named Attribute

        'Named' is a synonym of 'NamedAttribute'

        ``` python
        with GeoNodes("Named Attributes"):

            cube = Mesh.Cube()

            # Create a named attribute
            cube.points.store("Some Value", Float.Random(0, 1, seed=0))

            # Read the random value to offset along z
            cube.points.offset = (0, 0, Float.Named("Some Value"))

            # Remove the named attribute
            cube.remove_named_attribute("Some*", exact=False)

            cube.out()
        ```

        Arguments
        ---------
        - name (String) : socket 'Name' (Name)

        Returns
        -------
        - DataSocket [exists_]
        """
        return cls.named_attribute(name=name)

# =============================================================================================================================
# =============================================================================================================================
# String
# =============================================================================================================================
# =============================================================================================================================

class String(DataSocket):

    SOCKET_TYPE = 'STRING'

    def __init__(self, value="", name=None, tip=None):
        """ DataSocket of type String

        A group input socket of type String is created if the name is not None.

        Arguments
        ---------
        - value (str or DataSocket) : initial value
        - name (str = None) : group input socket name if not None
        - tip (str = None) : user type for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                bsock = Node('String', string=str(value))._out
            else:
                bsock = Tree.new_input('NodeSocketString', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def FromValue(cls, value, decimals=0):
        """ Node 'Value to String' (FunctionNodeValueToString)

        Arguments
        ---------
        - value (Float) : socket 'Value' (Value)
        - decimals (Int) : socket 'Decimals' (Decimals)

        Returns
        -------
        - string (String)
        """

        return value.to_string(decimals=decimals)

    @classmethod
    def Join(cls, *strings, delimiter=None):
        """ Node 'Join Strings' (GeometryNodeStringJoin)

        Arguments
        ---------
        - *strings (String) : socket 'Strings' (Strings)
        - delimiter (String) : socket 'Delimiter' (Delimiter)

        Returns
        -------
        - string (String)
        """

        return String(delimiter).join(*strings)

    # ====================================================================================================
    # Properties

    @classmethod
    @property
    def special_characters(cls):
        """ Node 'Special Characters' (FunctionNodeInputSpecialCharacters)

        Returns
        -------
        - Node: [line_break (String), tab (String)]
        """
        return Node('Special Characters')

    @classmethod
    @property
    def line_break(cls):
        """ Node 'Special Characters' (FunctionNodeInputSpecialCharacters)

        Returns
        -------
        - line_break (String)
        """
        return cls.special_characters.line_break

    @classmethod
    @property
    def tab(cls):
        """ Node 'Special Characters' (FunctionNodeInputSpecialCharacters)

        Returns
        -------
        - tab (String)
        """
        return cls.special_characters.tab

    @property
    def length(self):
        """ Node 'String Length' (FunctionNodeStringLength)

        Arguments
        ---------
        - self (String) : socket 'String' (String)

        Returns
        -------
        - Node: [length (Int)]
        """

        return Node('String Length')._out

    # ====================================================================================================
    # Methods

    def join(self, *strings):
        """ Node 'Join Strings' (GeometryNodeStringJoin)

        Arguments
        ---------
        - self (String) : socket 'Delimiter' (Delimiter)
        - *strings (String) : socket 'Strings' (Strings)

        Returns
        -------
        - string (String)
        """

        return Node('Join Strings', {0: self, 1: list(strings)})._out

    def replace(self, find=None, replace=None):
        """ Node 'Replace String' (FunctionNodeReplaceString)

        Arguments
        ---------
        - self (String) : socket 'String' (String)
        - find (String) : socket 'Find' (Find)
        - replace (String) : socket 'Replace' (Replace)

        Returns
        -------
        - string (String)
        """

        return Node('Replace String', {'String': self, 'Find': find, 'Replace': replace})._out

    def slice(self, position=0, length=10):
        """ Node 'Slice String' (FunctionNodeSliceString)

        Arguments
        ---------
        - self (String) : socket 'String' (String)
        - position (Integer) : socket 'Position' (Position)
        - length (Integer) : socket 'Length' (Length)

        Returns
        -------
        - string (String)
        """

        return Node('Slice String', {'String': self, 'Position': position, 'Length': length})._out

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None,
                overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT', font=None):
        """ Node 'String to Curves' (GeometryNodeStringToCurves)

        Arguments
        ---------
        - self (String) : socket 'String' (String)
        - size (Float) : socket 'Size' (Size)
        - character_spacing (Float) : socket 'Character Spacing' (Character Spacing)
        - word_spacing (Float) : socket 'Word Spacing' (Word Spacing)
        - line_spacing (Float) : socket 'Line Spacing' (Line Spacing)
        - text_box_width (Float) : socket 'Text Box Width' (Text Box Width)
        - text_box_height (Float) : socket 'Text Box Height' (Text Box Height)
        - overflow (str): Node.overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
        - align_x (str): Node.align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
        - align_y (str): Node.align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
        - pivot_mode (str): Node.pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
        - font (VectorFont): Node.font

        Returns
        -------
        - curve_instances (GEOMETRY)
        """

        from .geometryclass import Instances
        return Instances.FromString(self, size=size, character_spacing=character_spacing, word_spacing=word_spacing,
                    line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height,
                    overflow=overflow, align_x=align_x, align_y=align_y, pivot_mode=pivot_mode)

    # ----- Comparison

    def equal(self, other):
        """ Node 'Compare' (FunctionNodeCompare)

        Node compare with data_type = 'STRING' and operation = 'EQUAL'

        Arguments
        ---------
        - self : socket 'A' (A)
        - other (string) : socket 'B' (B)

        Returns
        -------
        - result (Boolean)
        """

        # operation in ('EQUAL', 'NOT_EQUAL', 'BRIGHTER', 'DARKER')
        return Node("Compare", {'A': self, 'B': other}, data_type='STRING', operation='EQUAL')._out

    def not_equal(self, other):
        """ Node 'Compare' (FunctionNodeCompare)

        Node compare with data_type = 'STRING' and operation = 'NOT_EQUAL'

        Arguments
        ---------
        - self : socket 'A' (A)
        - other (string) : socket 'B' (B)

        Returns
        -------
        - result (Boolean)
        """

        return Node("Compare", {'A': self, 'B': other}, data_type='STRING', operation='NOT_EQUAL')._out


# =============================================================================================================================
# =============================================================================================================================
# Material
# =============================================================================================================================
# =============================================================================================================================

class Material(DataSocket):

    SOCKET_TYPE = 'MATERIAL'

    def __init__(self, value=None, name=None, tip=None):
        """ Class Material data socket

        Arguments
        ---------
        - value (bpy.types.Material or str = None) : material or material name in bpy.data.materials
        - name (str = None) : create a group input socket of type Material if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            material = utils.get_blender_resource('MATERIAL', value)
            if name is None:
                bsock = Node('Material', material=material)._out
            else:
                bsock = Tree.new_input('NodeSocketMaterial', name=name, value=material, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

# =============================================================================================================================
# =============================================================================================================================
# Image
# =============================================================================================================================
# =============================================================================================================================

class Image(DataSocket):

    SOCKET_TYPE = 'IMAGE'

    def __init__(self, value=None, name=None, tip=None):
        """ Class Image data socket

        Arguments
        ---------
        - value (bpy.types.Image or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('IMAGE', value)
            if name is None:
                bsock = Node('Image', image=image)._out
            else:
                bsock = Tree.new_input('NodeSocketImage', name=name, value=image, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    # ====================================================================================================
    # Properties

    # ====================================================================================================
    # Methods

    @staticmethod
    def Info(image=None, frame=None):
        """ Node 'Image Info' (GeometryNodeImageInfo)

        Arguments
        ---------
        - image (Image) : socket 'Image' (Image)
        - frame (Integer) : socket 'Frame' (Frame)

        Returns
        -------
        - Node: [width (Integer), height (Integer), has_alpha (Boolean), frame_count (Integer), fps (Float)]
        """

        return Node("Image Info", {"Image": image, "Frame": frame})

    def info(self, frame=None):
        """ Node 'Image Info' (GeometryNodeImageInfo)

        Arguments
        ---------
        - self (Image) : socket 'Image' (Image)
        - frame (Integer) : socket 'Frame' (Frame)

        Returns
        -------
        - Node: [width (Integer), height (Integer), has_alpha (Boolean), frame_count (Integer), fps (Float)]
        """

        return self._cache("Image Info", {"Image": self, "Frame": frame})

# =============================================================================================================================
# =============================================================================================================================
# Image
# =============================================================================================================================
# =============================================================================================================================

class TextureRoot(DataSocket):

    SOCKET_TYPE = 'TEXTURE'

    def __init__(self, value=None, name=None, tip=None):
        """ Class Image data socket

        Arguments
        ---------
        - value (bpy.types.Image or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('TEXTURE', value)
            if name is None:
                name = "Texture"
            bsock = Tree.new_input('NodeSocketTexture', name=name, value=image, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    # ====================================================================================================
    # Properties

    # ====================================================================================================
    # Methods



# =============================================================================================================================
# =============================================================================================================================
# Object
# =============================================================================================================================
# =============================================================================================================================

class Object(DataSocket):

    SOCKET_TYPE = 'OBJECT'

    def __init__(self, value=None, name=None, tip=None):
        """ Class Object data socket

        Arguments
        ---------
        - value (bpy.types.Object or str = None) : object or object name in bpy.data.objects
        - name (str = None) : create a group input socket of type Object if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            obj = utils.get_blender_resource('OBJECT', value)
            if name is None:
                name = 'Object'
            bsock = Tree.new_input('NodeSocketObject', name=name, value=obj, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    @property
    def Self(cls):
        """ Node 'Self Object' (GeometryNodeSelfObject)

        Returns
        -------
        - self_object (Object)
        """
        return Node("Self Object")._out

    @classmethod
    @property
    def ActiveCamera(cls):
        """ Node 'Active Camera' (GeometryNodeInputActiveCamera)

        Returns
        -------
        - active_camera (Object)
        """

        return Node("Active Camera")._out

    # ====================================================================================================
    # Methods

    @staticmethod
    def Info(object=None, as_instance=None, original=True):
        """ Node 'Object Info'

        Tree: Geometry Nodes

        Sockets
        -------
        - Object (Object) : object
        - As Instance (Boolean) : as_instance
        - original (Boolean) : original

        Parameters
        ----------
        - transform_space = 'ORIGINAL' or 'RELATIVE'

        Arguments
        ---------
        - object (Object) : 'Object' socket
        - as_instance (Boolean) : 'As Instance': socket
        - original (Boolean = True) : transform_space parameter

        Returns
        -------
        - Node 'Object Info'
        """
        return Node("Object Info", {"Object": object, "As Instance": as_instance}, transform_space = 'ORIGINAL' if original else 'RELATIVE')

    def info(self, as_instance=None, original=True):
        """ Node 'Object Info' (GeometryNodeObjectInfo)

        Arguments
        ---------
        - self (Object) : socket 'Object' (Object)
        - as_instance (Boolean) : socket 'As Instance' (As Instance)
        - original (bool) : Node.transform_space in = 'ORIGINAL' if True else 'RELATIVE'

        Returns
        -------
        - Node: [transform (Matrix), location (Vector), rotation (Rotation), scale (Vector), geometry (GEOMETRY)]
        """

        return self._cache("Object Info", {"Object": self, "As Instance": as_instance}, transform_space = 'ORIGINAL' if original else 'RELATIVE')

# =============================================================================================================================
# =============================================================================================================================
# Collection
# =============================================================================================================================
# =============================================================================================================================

class Collection(DataSocket):

    SOCKET_TYPE = 'COLLECTION'

    def __init__(self, value=None, name=None, tip=None):
        """ Class Collection data socket

        Arguments
        ---------
        - value (bpy.types.Object or str = None) : collection or collection name in bpy.data.collections
        - name (str = None) : create a group input socket of type Collection if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            coll = utils.get_blender_resource('COLLECTION', value)
            if name is None:
                name = 'Collection'
            bsock = Tree.new_input('NodeSocketCollection', name=name, value=coll, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    # ====================================================================================================
    # Methods

    @staticmethod
    def Info(collection=None, separate_children=None, reset_children=None, original=True):
        """ Node 'Collection Info' (GeometryNodeCollectionInfo)

        Arguments
        ---------
        - collection (Collection) : socket 'Collection' (Collection)
        - separate_children (Boolean) : socket 'Separate Children' (Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (Reset Children)
        - original (bool) : Node.transform_space = 'ORIGINAL' if True else 'RELATIVE'

        Returns
        -------
        - instances (GEOMETRY)
        """

        return Node("Collection Info", {"Collection": collection, "Separate Children": separate_children, "Reset Children": reset_children}, transform_space = 'ORIGINAL' if original else 'RELATIVE')._out

    def info(self, separate_children=None, reset_children=None, original=True):
        """ Node 'Collection Info' (GeometryNodeCollectionInfo)

        Arguments
        ---------
        - self : socket 'Collection' (Collection)
        - separate_children (Boolean) : socket 'Separate Children' (Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (Reset Children)
        - original (bool) : Node.transform_space = 'ORIGINAL' if True else 'RELATIVE'

        Returns
        -------
        - instances (GEOMETRY)
        """

        return self._cache("Collection Info", {"Collection": self, "Separate Children": separate_children, "Reset Children": reset_children}, transform_space = 'ORIGINAL' if original else 'RELATIVE')


# =============================================================================================================================
# =============================================================================================================================
# Menu
# =============================================================================================================================
# =============================================================================================================================

class Menu(DataSocket):

    SOCKET_TYPE = 'MENU'

    # ====================================================================================================
    # Constructors
