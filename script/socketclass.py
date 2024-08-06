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

        # ---- Output socket creation if
        # - It doesn't already exist
        # - The tree is not a group
        if self.SOCKET_TYPE == 'GEOMETRY':
            tree = Tree.current_tree
            if not(tree.has_output_geometry or tree._is_group):
                tree.set_output_geometry(self, name)
                return

        # ---- New output socket

        bsocket = tree.new_output(bl_idname, name)
        tree.link(self, bsocket)

    def out(self, name=None):
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
        res = Node('Switch', {'Switch': condition, 'False': false, 'True': true}, input_type=cls.input_type(default='GEOMETRY'))._out

        if cls.SOCKET_TYPE == 'GEOMETRY':
            geo_class = cls._geometry_class([false, true])
            if geo_class is not None:
                res = geo_class(res)

        return res


    # -----------------------------------------------------------------------------------------------------------------------------
    # Method versions

    def menu_switch(self, self_name='A', items={'B': None}, menu=0, name="Menu", tip=None):
        return self.MenuSwitch({self_name: self, **items}, menu=menu, name=name, tip=tip)

    def index_switch(self, *values, index=0):
        return self.IndexSwitch(self, *values, index=0)

    def switch(self, condition=None, true=None):
        return self.Switch(condition=condition, false=self, true=true)

    # ====================================================================================================
    # Methods

    def blur(self, iterations=None, weight=None):
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
        attribute = Node('Named Attribute', {'Name': name}, data_type=cls.data_type())._out
        attribute.exists_ = attribute.node.exists
        return attribute

    @classmethod
    def Named(cls, name):
        attribute = Node('Named Attribute', {'Name': name}, data_type=cls.data_type())._out
        attribute.exists_ = attribute.node.exists
        return attribute

    def store(self, domain, name):
        try:
            domain.store_named_attribute(name, self)
        except:
            raise NodeError(f"Impossible to store the named attribute '{name}' on domain {domain}.", domain=domain, attribute=self, name=name)

# =============================================================================================================================
# =============================================================================================================================
# String
# =============================================================================================================================
# =============================================================================================================================

class String(DataSocket):

    SOCKET_TYPE = 'STRING'

    def __init__(self, value="", name=None, tip=None):
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
        return value.to_string(decimals=decimals)

    @classmethod
    def Join(cls, *strings):
        return String().join(*strings)

    # ====================================================================================================
    # Properties

    @classmethod
    @property
    def special_characters(cls):
        return Node('Special Characters')

    @classmethod
    @property
    def line_break(cls):
        return cls.special_characters.line_break

    @classmethod
    @property
    def tab(cls):
        return cls.special_characters.tab

    @property
    def length(self):
        return Node('String Length')._out

    # ====================================================================================================
    # Methods

    def join(self, *strings):
        return Node('Join Strings', {0: self, 1: list(strings)})._out

    def replace(self, find=None, replace=None):
        return Node('Replace String', {'String': self, 'Find': find, 'Replace': replace})._out

    def slice(self, position=0, length=10):
        return Node('Slice String', {'String': self, 'Position': position, 'Length': length})._out

    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None,
                overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT'):

        from .geometryclass import Instances
        return Instances.FromString(self, size=size, character_spacing=character_spacing, word_spacing=word_spacing,
                    line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height,
                    overflow=overflow, align_x=align_x, align_y=align_y, pivot_mode=pivot_mode)

    # ----- Comparison

    def equal(self, other):
        # operation in ('EQUAL', 'NOT_EQUAL', 'BRIGHTER', 'DARKER')
        return Node("Compare", {'A': self, 'B': other}, data_type='STRING', operation='EQUAL')._out

    def not_equal(self, other):
        return Node("Compare", {'A': self, 'B': other}, data_type='STRING', operation='NOT_EQUAL')._out




# =============================================================================================================================
# =============================================================================================================================
# Material
# =============================================================================================================================
# =============================================================================================================================

class Material(DataSocket):

    SOCKET_TYPE = 'MATERIAL'

    def __init__(self, value=None, name=None, tip=None):
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
        return Node("Image Info", {"Image": image, "Frame": frame})

    def info(self, frame=None):
        return self._cache("Image Info", {"Image": self, "Frame": frame})


# =============================================================================================================================
# =============================================================================================================================
# Object
# =============================================================================================================================
# =============================================================================================================================

class Object(DataSocket):

    SOCKET_TYPE = 'OBJECT'

    def __init__(self, value=None, name=None, tip=None):
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
        return Node("Self Object")._out

    @classmethod
    @property
    def ActiveCamera(cls):
        return Node("Active Camera")._out

    # ====================================================================================================
    # Methods

    @staticmethod
    def Info(object=None, as_instance=None, original=True):
        return Node("Object Info", {"Object": object, "As Instance": as_instance}, transform_space = 'ORIGINAL' if original else 'RELATIVE')

    def info(self, as_instance=None, original=True):
        return self._cache("Object Info", {"Object": self, "As Instance": as_instance}, transform_space = 'ORIGINAL' if original else 'RELATIVE')

# =============================================================================================================================
# =============================================================================================================================
# Collection
# =============================================================================================================================
# =============================================================================================================================

class Collection(DataSocket):

    SOCKET_TYPE = 'COLLECTION'

    def __init__(self, value=None, name=None, tip=None):
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
        return Node("Collection Info", {"Collection": collection, "Separate Children": separate_children, "Reset Children": reset_children}, transform_space = 'ORIGINAL' if original else 'RELATIVE')

    def info(self, separate_children=None, reset_children=None, original=True):
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
