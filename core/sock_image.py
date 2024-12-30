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


class Image(generated.Image):

    SOCKET_TYPE = 'IMAGE'

    def __init__(self, value: bpy.types.Image | str | Socket | None = None, name: str | None = None, tip: str | None = None):
        """ Class Image data socket

        Node <&Node Image>

        Arguments
        ---------
        - value (bpy.types.Image or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip (str = None) : user tip for group input socket
        """
        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('IMAGE', value)
            if name is None:
                bsock = Node('Image', image=image)._out
            else:
                bsock = Tree.new_input('NodeSocketImage', name=name, value=image, description=tip)

        super().__init__(bsock)
