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

module : socket_type
--------------------
- class wrapping all the possible ways to defined a socket type

updates
-------
- creation : 2025/12/03
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

import numpy as np
import bpy
from . import constants
from .scripterror import NodeError
from . import colors
from . import blender

# ====================================================================================================
# Socket Type
# ====================================================================================================

class SocketType:

    __slots__ = ('_full_socket_id',)

    def __init__(self, value):

        self._full_socket_id  = None

        # ---------------------------------------------------------------------------
        # Specific cases
        # ---------------------------------------------------------------------------

        # Socket : its type has priority over bsocket
        if getattr(value, 'SOCKET_TYPE', None) is not None:
            value = value.SOCKET_TYPE

        elif getattr(value, 'DOMAIN_NAME', None) is not None:
            value = value._geo

        # List of sockets
        elif isinstance(value, list):
            ok = False
            for v in value:
                if SocketType.get_bsocket(v) is None:
                    ok = False
                    break
            if ok:
                value = value[0]

        bsocket = SocketType.get_bsocket(value)

        # ---------------------------------------------------------------------------
        # From another SocketType
        # ---------------------------------------------------------------------------

        if isinstance(value, SocketType):
            self._full_socket_id  = value._full_socket_id

        # ---------------------------------------------------------------------------
        # None
        # ---------------------------------------------------------------------------

        elif value is None:
            self._full_socket_id = 'NodeSocketGeometry'

        # ---------------------------------------------------------------------------
        # From a socket
        # ---------------------------------------------------------------------------

        elif bsocket is not None:
            self._full_socket_id = bsocket.bl_idname

        # ---------------------------------------------------------------------------
        # From a NodeTreeInterfaceSocket
        # ---------------------------------------------------------------------------

        elif isinstance(value, bpy.types.NodeTreeInterfaceSocket):
            tsock = value
            self._full_socket_id = tsock.socket_type
            if hasattr(tsock, 'subtype'):
                self.subtype = tsock.subtype
            if self.is_vector:
                self.dimensions = tsock.dimensions

        # ---------------------------------------------------------------------------
        # From a string
        # ---------------------------------------------------------------------------

        elif isinstance(value, str):
            self._full_socket_id = constants.SOCKET_IDS.get(value)

        # ====================================================================================================
        # If socket_id is still None, argument is a python value
        # ====================================================================================================

        if self._full_socket_id is None:

            if isinstance(value, bool):
                sid = 'NodeSocketBool'

            elif isinstance(value, (int, np.int8, np.int32, np.int64)):
                sid = 'NodeSocketInt'

            elif isinstance(value, (float, np.float32, np.float64)):
                sid = 'NodeSocketFloat'

            elif isinstance(value, str):
                sid = 'NodeSocketString'

            elif isinstance(value, bpy.types.Object):
                sid = 'NodeSocketObject'

            elif isinstance(value, bpy.types.Material):
                sid = 'NodeSocketMaterial'

            elif isinstance(value, bpy.types.Image):
                sid = 'NodeSocketImage'

            elif isinstance(value, bpy.types.Collection):
                sid = 'NodeSocketCollection'

            elif np.shape(value) != ():
                size = np.size(value)
                if size == 2:
                    sid = 'NodeSocketVector2D'
                elif size == 3:
                    sid = 'NodeSocketVector'
                elif size == 4:
                    sid = 'NodeSocketColor'
                elif size == 16:
                    sid = 'NodeSocketMatrix'
                else:
                    raise NodeError(
                        f"Error when trying to get the socket type of value {value} (type= {type(value).__name__}).\n"
                        f"The value seems to be an array of size {1} (shape {np.shape(value)})."
                        f"Acceptable sizes are 2, 3, 4 and 16.")

            else:
                from .nodeclass import Node
                if isinstance(value, Node):
                    s = "The value is a node, you certainly forgot to get one of its sockets.\n"
                    s += repr(value)
                else:
                    s = f"The value is : {value}\nIts type is  : {type(value)}\n"

                raise NodeError(
                    "Socket type error\n\n"
                    f"Impossible to build a socket type from the passed value.\n{s}"
                )

            self._full_socket_id = sid

    # ====================================================================================================
    # Str and Repr
    # ====================================================================================================

    @property
    def is_virtual(self):
        return self._full_socket_id == 'NodeSocketVirtual'

    def __str__(self):
        s = self.class_name
        if self.dimensions is not None:
            s += f"[{self.dimensions}]"

        if self.subtype is not None:
            if self.subtype == 'XYZ':
                s += " (XYZ)"
            else:
                s += f" ({self.subtype.title()})"

        return s

    def __repr__(self):
        return f"<SocketType {self.class_name}: {self.full_socket_id} = ({self.type}, {self.subtype}, {self.dimensions})>"
    
    def serialize(self):
        return self._full_socket_id

    # ====================================================================================================
    # Checkings
    # ====================================================================================================

    @staticmethod
    def check_socket_id(socket_id, halt: bool = True) -> bool:
        if socket_id in constants.SOCKET_SUBTYPES:
            return True
        if halt:
            raise RuntimeError("Value '{socket_id}' is not a valid socket id, valids are: {list(constants.SOCKET_SUBTYPES.keys())}")
        return False
    
    @staticmethod
    def check_type(socket_type, halt: bool = True) -> bool:
        if socket_type in constants.SOCKETS:
            return True
        if halt:
            raise RuntimeError("Value '{socket_type}' is not a valid socket id, valids are: {list(constants.SOCKETS.keys())}")
        return False
    
    @staticmethod
    def check_class_name(class_name, halt: bool = True) -> bool:

        if class_name in ['Custom', 'Virtual', 'Input']:
            return True 

        if class_name in constants.CLASS_NAMES.values():
            return True

        if class_name in constants.GEOMETRY_CLASSES:
            return True
        
        if class_name in constants.DOMAIN_CLASSES:
            return True
        
        if halt:
            raise RuntimeError("Value '{class_name}' is not a valid class name.")

        return False
    
    @staticmethod
    def type_from_class_name(class_name) -> str:

        if class_name in ['Custom', 'Virtual', 'Input']:
            return 'CUSTOM'

        if class_name in constants.GEOMETRY_CLASSES:
            return 'NodeSocketGeometry'
        
        if class_name in constants.DOMAIN_CLASSES:
            return 'NodeSocketGeometry'
        
        for stype, cname in constants.CLASS_NAMES.items():
            if cname == class_name:
                return stype
            
        assert False, f"Calls check_class_name before  type_from_class_name {class_name}"
    
    # ====================================================================================================
    # Get a NodeSocket
    # ====================================================================================================

    @staticmethod
    def get_bsocket(value):
        if isinstance(value, bpy.types.NodeSocket):
            return value
        
        bsocket = getattr(value, '_bsocket', None)
        if bsocket is None:
            return None
        
        # Can be an empty socket
        if not isinstance(bsocket, bpy.types.NodeSocket):
            return None
        
        # Virtual socket can point on the wrong output socket
        if value.SOCKET_TYPE != 'CUSTOM':
            return bsocket
        
        for bsock in value.node._bnode.outputs:
            if bsock.type == 'CUSTOM':
                return bsock
            
        assert False, f"Shouldn't happen {value}"
        
        
    @staticmethod
    def get_socket_name(socket):
        bsocket = SocketType.get_bsocket(socket)
        assert bsocket is not None, f"Shouldn't happen {socket} !"
        return bsocket.name if bsocket.label in [None, ""] else bsocket.label

        
    @staticmethod
    def class_name_from_socket_name(name):
        
        name = name.lower()

        # 5.0.0 socket names
        # IN : {'Geometry', 'Target Geometry', 'Volume', 'A', 'Points', 'Curves', 'Instances', 
        # 'True', 'Profile Curve', 'False', 'Guide Curves', 'Mesh 1', 'Mesh', '0', 
        # 'Grease Pencil', 'B', 'Mesh 2', 'Curve', '1', 'Instance'}
        # OUT: {'Points', 'Convex Hull', 'Element', 'Curves', 'Bounding Box', 
        # 'Geometry', 'Output', 'Inverted', 'Instances', 'Selection', 'Transform', 
        # 'Dual Mesh', 'Curve Instances', 'Mesh', 'Volume', 'Curve', 'Point Cloud', 'Grease Pencil'}
        
        if name in ('mesh', 'convex hull', 'bounding box', 'dual mesh') or name.startswith('Mesh'):
            return 'Mesh'
        elif name in ('curve', 'curves', 'profile curve', 'guide curve'):
            return 'Curve'
        elif name in ('points', 'point cloud'):
            return 'Cloud'
        elif name in ('grease pencil',):
            return 'GreasePencil'
        elif name in ('instance', 'instances', 'curve instances'):
            return 'Instances'
        elif name in ('volume'):
            return 'Volume'

        return 'Geometry'        
        
    # ====================================================================================================
    # Computed properties
    # ====================================================================================================

    @property
    def socket_id(self):
        return constants.SOCKET_SUBTYPES[self._full_socket_id]['nodesocket']
        
    @property
    def full_socket_id(self):
        return self._full_socket_id
    
    @property
    def type(self):
        return constants.SOCKET_SUBTYPES[self._full_socket_id]['socket_type']
    
    @property
    def items_type(self):
        # Used in Node.xxx_items.new(...)
        # ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE')
        t = self.type
        return {'VALUE': 'FLOAT'}.get(t, t)
    
    @property
    def is_geometry(self):
        return self._full_socket_id == 'NodeSocketGeometry'
    
    @property
    def is_vector(self):
        return self.type == 'VECTOR'
    
    @property
    def is_attribute(self):
        return self.class_name in constants.ATTRIBUTE_CLASSES
    
    # ====================================================================================================
    # Class name
    # ====================================================================================================

    @property
    def class_name(self):
        if self.is_virtual:
            return 'Input'
        return constants.CLASS_NAMES[self.type]
        
    # ====================================================================================================
    # Subtype
    # ====================================================================================================
        
    @property
    def subtype(self):
        subtype = constants.SOCKET_SUBTYPES[self._full_socket_id]['subtype']
        if subtype in ['NONE', ""]:
            return None
        else:
            return subtype
        
    @subtype.setter
    def subtype(self, value):

        # ---------------------------------------------------------------------------
        # Make sure it as an upper case string
        # ---------------------------------------------------------------------------

        if value is None:
            subtype = "NONE"
        elif isinstance(value, str):
            subtype = value.upper()
        else:
            raise RuntimeError(f"Impossible to set subtype '{value}': must be a string.")
        
        # ---------------------------------------------------------------------------
        # Removing subtype
        # ---------------------------------------------------------------------------

        socket_id = self.socket_id

        if subtype in [None, "", "NONE"]:
            self._full_socket_id = socket_id
            return

        # ---------------------------------------------------------------------------
        # Check it is a valid
        # ---------------------------------------------------------------------------

        spec = constants.SOCKETS[self.type]
        _, subtypes, _  = spec['props'].get('subtype', (None, None, None))
        if subtypes is None:
            raise RuntimeError(f"Impossible to set subtype '{subtype}': type '{self.class_name}' doesn't accept subtypes.")
        if subtype not in subtypes:
            raise RuntimeError(f"Impossible to set subtype: '{subtype}' is not a subtype of {self.class_name}, subtypes are {subtypes}.")

        # ---------------------------------------------------------------------------
        # Ok, look for the full socket id
        # ---------------------------------------------------------------------------

        for full_socket_id, spec in constants.SOCKET_SUBTYPES.items():
            if spec['nodesocket'] == socket_id and spec['subtype'] == subtype:
                self._full_socket_id = full_socket_id
                return

        assert False, f"Shouldn't happen: {self}, {subtype} in {subtypes}"

    # ====================================================================================================
    # Vector dimensions
    # ====================================================================================================

    @property
    def dimensions(self):
        if self.is_vector:
            d = constants.SOCKET_SUBTYPES[self._full_socket_id]['dimensions']
            if d is None:
                return 3
            else:
                return d
        else:
            return None
    
    @dimensions.setter
    def dimensions(self, value):

        if value is None:
            if self.is_vector:
                value = 3
            else:
                return
        
        if not self.is_vector:
            raise AttributeError(f"SocketType error: dimensions can set only to Vector type, not {self.class_name}.")
        
        s = self._full_socket_id
        if s[-1] == 'D':
            s = s[:-2]

        if value == 3:
            self._full_socket_id = s
        elif value in [2, 4]:
            self._full_socket_id = f"{s}{value}D"
        else:
            raise AttributeError(f"SocketType error: {value} is an invalid dimensions for Vector type. Must be in (2, 3, 4).")
    
    # ====================================================================================================
    # Information
    # ====================================================================================================

    def get_props(self):
        return {**constants.SOCKET_SUBTYPES[self._full_socket_id]}
    
    def set_props(self, props):
        if self.subtype is not None:
            props['subtype'] = self.subtype
        if self.dimensions is not None:
            props['dimensions'] = self.dimensions

        return props
    
    @property
    def default_value(self):
        props = constants.SOCKETS[self.type].get('props')
        if 'default' in props:
            return props['default'][2]
        else:
            return None
        
    def get_default_from_value(self, value = None):
        if value is None:
            return self.default_value
        
        stype = self.type
        if stype == 'BOOLEAN':
            return bool(value)
        
        elif stype == 'INT':
            return int(value)
        
        elif stype == 'RGBA':
            return colors.to_color(value)
        
        elif stype in ['ROTATION', 'VECTOR']:
            if np.shape(value) == ():
                a = float(value)
                return (a, a, a)
            elif np.size(value) == 3:
                return tuple(np.asarray(value, dtype=float))
            else:
                raise NodeError(f"The value <{value}> is not a {self.class_name}.")
            
        elif stype == 'STRING':
            return str(value)
        
        elif stype == 'VALUE':
            return float(value)
        
        elif stype in ['COLLECTION', 'IMAGE', 'MATERIAL', 'OBJECT']:
            return blender.get_resource(self.type, value)
        
        else:
            return None


    # ====================================================================================================
    # Data type for node
    # ====================================================================================================

    def get_node_data_type(self, tree_type: str, bl_idname: str, halt: bool = True):

        # Node conversion dict
        #'FunctionNodeCompare': {'data_type': {
        #   'INT'   : 'INT',
        #   'RGBA'  : 'RGBA',
        #   'STRING': 'STRING',
        #   'VALUE' : 'FLOAT',
        #   'VECTOR': 'VECTOR'
        # }},

        info = constants.NODE_INFO[tree_type][bl_idname]

        conv = info.get('data_type')
        if conv is None:
            raise RuntimeError(f"Node '{bl_idname}' doesn't have a 'data_type' attribute.")
        
        # Argument value
        socket_type = self.type

        # Let's find in the valid type
        valids = []
        for stype, node_type in conv.items():
            if stype == socket_type:
                return node_type
            
            valids.append(SocketType(stype).class_name)

        if halt:
            raise AttributeError(f"Invalid data_type argument '{self}' for node [{info['name']}], valids are {valids}")
        else:
            return None
    
    # ====================================================================================================
    # Comparaison
    # ====================================================================================================

    def equal_to(self, other, with_subtype: bool = False):

        other = SocketType(other)

        ok = self.type == other.type
        if not ok:
            return False
        
        if not with_subtype:
            return True

        if self.subtype != other.subtype:
            return False
        
        if not self.is_vector:
            return True
        
        if self.dimensions != other.dimensions:
            return False
        
        return True

    def __eq__(self, other):
        return self.equal_to(other)
    
    def __neq__(self, other):
        return not self.equal_to(other)
    





    
    
