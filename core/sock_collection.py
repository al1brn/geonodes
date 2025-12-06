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

module : sock_collection
------------------------
- Collection socket

This class inherits from Socket and from generated.Collection
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

class Collection(generated.Collection):

    SOCKET_TYPE = 'COLLECTION'

    def __init__(self, 
        value: object | str = None,
        name: str = None,
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: object = None,
        ):
        """ Class Collection data socket

        Arguments
        ---------
        - value (objet | str = None) : collection or collection name in bpy.data.collections
        - name (str = None) : create a group input socket of type Collection if not None
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        """
        bsock = utils.get_bsocket(value)

        if bsock is None:
            
            coll = utils.get_blender_resource('COLLECTION', value)
            
            if name is None:
                bsock = Node('Collection', collection=coll)._out

            else:
                bsock = self._create_input_socket(value=value, name=name,
                    tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
                    hide_in_modifier=hide_in_modifier)

        super().__init__(bsock)

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Collection, nd

        with GeoNodes("Collection Test"):

            g = Collection().info()
            g += Collection(name="From Input'").info(separate_children=True, reset_children=True)
            g += Collection("Collection").info(transform_space='RELATIVE')
            g += nd.collection_info("Collection")

            g.out()


