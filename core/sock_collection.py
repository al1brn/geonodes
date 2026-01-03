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


import bpy
from . import constants, utils
from .treeclass import Tree
from .nodeclass import Node
from .socket_class import Socket
from . import blender
from . import generated

class Collection(generated.Collection):
    """ Collection Socket.

    The Collection can be read from bpy.data.collections or passed with its name.

    ``` python
    import bpy
    from geonodes import GeoNodes, Collection, nd

    for c in "ABC":
        test_name = f"Test Coll {c}"
        coll = bpy.data.collections.get(test_name)
        if coll is None:
            coll = bpy.data.collections.new(test_name)
            bpy.context.collection.children.link(coll)

    with GeoNodes("Collection Test"):

        g = Collection("Test Coll A").info(transform_space='RELATIVE')
        g += Collection(name="From Input'").info(separate_children=True, reset_children=True)
        g += nd.collection_info("Test Coll B")
        g += nd.collection_info(bpy.data.collections["Test Coll C"])

        g.out()
    ```
    """

    SOCKET_TYPE = 'COLLECTION'

    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        import bpy
        from geonodes import GeoNodes, Collection, nd

        for c in "ABC":
            test_name = f"Test Coll {c}"
            coll = bpy.data.collections.get(test_name)
            if coll is None:
                coll = bpy.data.collections.new(test_name)
                bpy.context.collection.children.link(coll)


        with GeoNodes("Collection Test"):

            g = Collection("Test Coll A").info(transform_space='RELATIVE')
            g += Collection(name="From Input'").info(separate_children=True, reset_children=True)
            g += nd.collection_info("Test Coll B")
            g += nd.collection_info(bpy.data.collections["Test Coll C"])

            g.out()


