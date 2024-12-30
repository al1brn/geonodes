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

class Collection(generated.Collection):

    SOCKET_TYPE = 'COLLECTION'

    def __init__(self, value: bpy.types.Collection | Socket | str | None = None, name: str | None = None, tip: str | None = None):
        """ Class Collection data socket

        Arguments
        ---------
        - value (bpy.types.Object or str = None) : collection or collection name in bpy.data.collections
        - name (str = None) : create a group input socket of type Collection if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            coll = utils.get_blender_resource('COLLECTION', value)
            if name is None:
                name = 'Collection'
            bsock = Tree.new_input('NodeSocketCollection', name=name, value=coll, description=tip)

        super().__init__(bsock)
