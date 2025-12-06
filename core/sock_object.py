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

module : sock_object
---------------------
- Object socket

This class inherits from Socket and from generated.Object
which is automatically generated.

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


import bpy
from . import constants, utils
from .treeclass import Tree
from .nodeclass import Node
from .socket_class import Socket
from . import generated

class Object(generated.Object):

    SOCKET_TYPE = 'OBJECT'

    def __init__(self, 
        value: Socket | str = None,
        name: str = None,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        ):
        """ Class Object data socket

        Arguments
        ---------
        - value (bpy.types.Object or str = None) : object or object name in bpy.data.objects
        - name (str = None) : create a group input socket of type Object if not None
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        """
        bsock = utils.get_bsocket(value)
        if bsock is None:
            obj = utils.get_blender_resource('OBJECT', value)
            if name is None:
                #name = 'Object' # Before Blender 4.4
                bsock = Node('Object', object=obj)._out
            else:
                bsock = self._create_input_socket(value=value, name=name, tip=tip,
            panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

        super().__init__(bsock)

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Image, nd, Bundle, Object

        with GeoNodes("Object Test"):

            with Bundle() as b1:
                Object("Cube").info().node.out()
                
            with Bundle() as b2:
                Object("Cube", name="Your Object").info().node.out()
                
            nd.self_object.info().node.out("Self")
            
            b1.separate().node.out(panel="First")
            b2.separate().node.out(panel="Second")
            





