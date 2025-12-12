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
#from .nodeclass import MenuNode
from .socket_class import Socket
from . import generated


class Menu(generated.Menu):

    SOCKET_TYPE = 'MENU'

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Geometry, Mesh, Menu, Input, Curve
        
        with GeoNodes("Menu Demo") as tree:
            
            # ----------------------------------------------------------------------------------------------------
            # First Menu
            # ----------------------------------------------------------------------------------------------------
            
            simple = Geometry().menu_switch("Input", {
                "Cube": Mesh.Cube(),
                "Ico": Mesh.IcoSphere(),
                "Cone": Mesh.Cone(), 
                },
                menu=Input("Simple Mesh", default="Ico"), 
                )

            # ----------------------------------------------------------------------------------------------------
            # Second Menu
            # ----------------------------------------------------------------------------------------------------
                
            profile = Curve.Circle(radius=.1)
                
            with Geometry.MenuSwitch() as from_curve:
                simple.out("Simple Mesh")
                
            with from_curve:
                Curve.Spiral().to_mesh(profile_curve=profile).out("Spiral")
                
            with from_curve:
                Curve.Circle().to_mesh(profile_curve=profile).out("Circle")
                
            from_curve.node.menu = Input("From Curve", default="Simple Mesh")
            
            # ----------------------------------------------------------------------------------------------------
            # Index Switch
            # ----------------------------------------------------------------------------------------------------
            
            curve = Curve.IndexSwitch(index=Input("Curve Index"))
            with curve:
                Curve.Spiral().out()
                
            with curve:
                Curve.Circle().out()
                
            with curve:
                Curve.Quadrilateral().out()
                
            # ----------------------------------------------------------------------------------------------------
            # Switch
            # ----------------------------------------------------------------------------------------------------
            
            curve.switch(Input("Mesh/Curve"), from_curve).out()

                




