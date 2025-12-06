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

module : sock_integer
---------------------
- Integer socket

This class inherits from Socket and from generated.Integer
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


class Material(generated.Material):

    SOCKET_TYPE = 'MATERIAL'

    def __init__(self, 
        value: Socket = None, 
        name: str = None, 
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
                 ):
        """ Class Material data socket

        Node <&Node Material>

        Arguments
        ---------
        - value (bpy.types.Material or str = None) : material or material name in bpy.data.materials
        - name (str = None) : create a group input socket of type Material if not None
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            material = utils.get_blender_resource('MATERIAL', value)
            if name is None:
                bsock = Node('Material', material=material)._out
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

        from geonodes import GeoNodes, Material, nd, Mesh, ShaderNodes
        
        with ShaderNodes("Red"):
            pass

        with ShaderNodes("Blue"):
            pass

        with ShaderNodes("Green"):
            pass

        with GeoNodes("Material Test"):
            
            g = Mesh()
            
            mat0 = Material("Red")
            g.material = mat0
            
            mat1 = Material("Blue", name="Your Material")
            g[nd.index.less_than(3)].material = mat1

            g.replace_material(mat1, "Green")
            
            sel = nd.material_selection("Blue")
            g[sel].material = "Red"
            
            g.faces[nd.material_index.equal(1)].delete()
            
            
            g.out()
            




