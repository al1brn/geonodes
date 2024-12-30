#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : collection
-------------------
- Socket class Collection

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
- update : 2024/12/29
"""

import bpy
from . import constants, utils
from .treeclass import Tree, Node
from .socket_class import Socket
from . import generated


class Material(Socket):

    SOCKET_TYPE = 'MATERIAL'

    def __init__(self, value: bpy.types.Material | Socket | str | None = None, name: str | None = None, tip: str | None = None):
        """ Class Material data socket

        Node <&Node Material>

        Arguments
        ---------
        - value (bpy.types.Material or str = None) : material or material name in bpy.data.materials
        - name (str = None) : create a group input socket of type Material if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            material = utils.get_blender_resource('MATERIAL', value)
            if name is None:
                bsock = Node('Material', material=material)._out
            else:
                bsock = Tree.new_input('NodeSocketMaterial', name=name, value=material, description=tip)

        super().__init__(bsock)
