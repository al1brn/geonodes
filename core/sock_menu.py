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

module : sock_menu
---------------------
- Menu socket

This class inherits from Socket and from generated.Menu
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

from typing import Literal

from . import utils
from .treeclass import Tree
from .nodeclass import MenuNode
from .socket_class import Socket
from . import generated


class Menu(generated.Menu):

    SOCKET_TYPE = 'MENU'

    def __init__(self,
        value: Socket = None,
        name: str = 'Menu',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: str = '',
        expanded: bool = False,
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
    ):
        """ > Menu socket, node <&Node Menu Switch>

        Arguments
        ---------
        - value (Socket = None) : Socket or value to set to 'Menu Switch' node
        - name (str = None) : Name of the input socket to create if not None
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (str = '') : Property default_value
        - expanded  (bool = False) : Property menu_expanded
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
        """

        # ----------------------------------------------------------------------------------------------------
        # Value can be a Socket
        # ----------------------------------------------------------------------------------------------------

        bsocket = None
        if value is not None:
            bsocket = utils.get_bsocket(value)

        # ----------------------------------------------------------------------------------------------------
        # No socket : we get it either from a Menu Switch node or from Group input
        # ----------------------------------------------------------------------------------------------------

        if bsocket is None:
            if name is None:
                bsocket = MenuNode()._out._bsocket

            else:
                bsocket = self._create_input_socket(value=value, name=name, tip=tip,
                    panel=panel, optional_label=optional_label, hide_value=hide_value,
                    hide_in_modifier=hide_in_modifier, default=default, expanded=expanded, shape=shape)

        super().__init__(bsocket)

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Geometry, Mesh, Menu

        with GeoNodes("Menu Demo") as tree:
            
            # ----------------------------------------------------------------------------------------------------
            # Menu
            # ----------------------------------------------------------------------------------------------------
            
            menu = Menu()
            menu = Menu(name="Another menu")
            
            # Build 1
            g = Geometry.MenuSwitch({"Cube": Mesh.Cube(), "Ico": Mesh.IcoSphere()}, menu=tree.new_input("Option 1"), default_value="Ico")
            
            
            # Build 2    
            with Geometry().menu_switch("Input Geometry", menu=tree.new_input("Option 2"), Previous=g) as g:
                Mesh.Cube().out("Cube")
                
            with g:
                Mesh.UVSphere().out("UV", default=True)
                

            # ----------------------------------------------------------------------------------------------------
            # Switch
            # ----------------------------------------------------------------------------------------------------
            
            with Geometry.Switch(tree.new_input("Previous or Cube")) as sg:
                Mesh.Cube().out()
                
            # Else    
            with sg:
                g.out()
                
            # ----------------------------------------------------------------------------------------------------
            # Index Switch
            # ----------------------------------------------------------------------------------------------------
                
            # If index 0, 1
            with sg.index_switch(index=tree.new_input("Select int")) as ig:
                Mesh.Cube().out()
                
            # Elif index 2
            with ig:
                Mesh.IcoSphere().out()
                
            with ig:
                Mesh.UVSphere().out(default=True)
                Mesh.Line().out()
                
            ig.out()
            
              
        




