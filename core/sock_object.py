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
from . import blender


class Object(generated.Object):
    """ Object Socket.

    An object can be refered to using its name in bpy.data.objects.

    ``` python
    from geonodes import GeoNodes, Image, nd, Bundle, Object, Mesh, Input, Geometry

    with GeoNodes("Object Test"):
        
        # Default cube
        with Bundle() as b0:
            def_cube = Object("Cube")
            def_cube.info().out()
            
        # User object
        with Bundle() as b1:
            Object("Cube", name="Object").info().out()
            
        # Selft object
        with Bundle() as b2:
            sobj = nd.self_object
            nd.self_object.info().node.link_outputs(None, exclude=["Geometry"])
            Geometry().out()
            
        sig = b0.get_signature()
            
        bundle = Bundle.MenuSwitch(
            menu = Input("Object Selection", default_value="Self"),
            Cube = b0,
            Input = b1,
            Self  = b2)
            
        bundle.separate(signature=sig).out()    
    ```
    """

    SOCKET_TYPE = 'OBJECT'

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Image, nd, Bundle, Object, Mesh, Input, Geometry

        with GeoNodes("Object Test"):
            
            # Default cube
            with Bundle() as b0:
                def_cube = Object("Cube")
                def_cube.info().out()
                
            # User object
            with Bundle() as b1:
                Object("Cube", name="Object").info().out()
                
            # Selft object
            with Bundle() as b2:
                sobj = nd.self_object
                nd.self_object.info().node.link_outputs(None, exclude=["Geometry"])
                Geometry().out()
                
            sig = b0.get_signature()
                
            bundle = Bundle.MenuSwitch(
                menu = Input("Object Selection", default_value="Self"),
                Cube = b0,
                Input = b1,
                Self  = b2)
                
            bundle.separate(signature=sig).out()

            





