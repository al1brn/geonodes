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

module : sock_rotation
----------------------
- Rotation socket

This class inherits from Socket and from generated.Rotation
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
from .sockettype import SocketType
from .nodeclass import Node
from .socket_class import Socket
from . import generated


class Rotation(generated.Rotation):
    """ Rotation Socket.

    A Rotation can be created directly with a triplet of values. Operations between a Rotation
    and a triplet are also supported.

    ``` python
    from geonodes import GeoNodes, Mesh, Layout, Rotation, G, Float, Input, pi

    with GeoNodes("Rotation Test") as tree:
        
        
        with Layout("Base"):
            a = Rotation() @ Rotation((1, 2, 3))
            a = a.mix(Rotation(1, name="Your entry"), Input("Factor", subtype="Factor", min=0, max=1))
            b = G().random_rotation(max_zenith=pi/2).align_to_vector(Input("Vector"))
            c = Rotation.FromAxisAngle(axis=Input("Axis"), angle=Float.Angle(name="Angle"))
            b = b @ c
            
        with Layout("Named Attribute"):
            g = Mesh()
            g.points._A_Rotation = a
            
            c = a.rotate(Rotation("A Float"), rotation_space='LOCAL')
            g.faces.store("Another rotation", c)
            
        b.to_quaternion().node.out(panel="Quaternion")
            
        g.out()
    ```
    """

    SOCKET_TYPE = 'ROTATION'

    # ====================================================================================================
    # Operations

    def __matmul__(self, other):
        data_type = SocketType(other).type
        if data_type == 'ROTATION':
            return self.rotate_global(other)
        else:
            return self.rotate_vector(other)

    def __invert__(self):
        return self.invert()
    
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Rotation, G, Float, Input, pi

        with GeoNodes("Rotation Test") as tree:
            
            
            with Layout("Base"):
                a = Rotation() @ Rotation((1, 2, 3))
                a = a.mix(Rotation(1, name="Your entry"), Input("Factor", subtype="Factor", min=0, max=1))
                b = G().random_rotation(max_zenith=pi/2).align_to_vector(Input("Vector"))
                c = Rotation.FromAxisAngle(axis=Input("Axis"), angle=Float.Angle(name="Angle"))
                b = b @ c
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points._A_Rotation = a
                
                c = a.rotate(Rotation("A Float"), rotation_space='LOCAL')
                g.faces.store("Another rotation", c)
                
            b.to_quaternion().node.out(panel="Quaternion")
                
            g.out()
