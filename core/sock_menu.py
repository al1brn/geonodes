#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : menu
-------------------
- Socket class Menu

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


class Menu(Socket):

    SOCKET_TYPE = 'MENU'

    def __init__(self, socket=None, name="Menu", menu=0, items={'A': None, 'B': None}, tip=None, input_type=None):
        """ > Menu socket, node <&Node Menu Switch>

        Arguments
        ---------
        - socket (NodeSocket = None) :
        - name (str = 'Menu') : name of the group input socket
        - menu (int or str) : index or name of the default value
        - items (dict) : menu names and values
        - tip (str = None) : user tip
        """
        if socket is None:
            raise Exception("Menu Socket can't be instantiated directly, use 'Socket.MenuSwitch' instead")

        else:
            super().__init__(socket)
            return
