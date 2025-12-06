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

module : sock_image
---------------------
- Image socket

This class inherits from Socket and from generated.Image
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


class Image(generated.Image):

    SOCKET_TYPE = 'IMAGE'

    def __init__(self, 
        value: Socket | str = None, 
        name: str = None, 
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        ):
        """ Class Image data socket

        Node <&Node Image>

        Arguments
        ---------
        - value (bpy.types.Image or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (object = None) : Property default_value
        """
        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('IMAGE', value)
            if name is None:
                bsock = Node('Image', image=image)._out
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

        from geonodes import GeoNodes, Image, nd, Bundle, Geometry

        with GeoNodes("Image Test"):

            with Bundle() as b1:
                Image().info().node.out()
                
                
            with Bundle() as b2:
                Image(name="Your Image").info().node.out()
                
            Geometry().out()
            
            b1.separate().node.out(panel="First")
            b2.separate().node.out(panel="Second")




