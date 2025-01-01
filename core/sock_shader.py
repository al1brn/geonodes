#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : sock_shader
-------------------
- Implement Shader data socket

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
- update : 2024/12/29
- update : 2025/01/01
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node
from .socket_class import Socket
from .  import generated

class Shader(generated.Shader):

    SOCKET_TYPE = 'SHADER'

    def __init__(self, value: Socket | None = None, name: str | None = None, tip: str | None = None):
        """ Socket of type String

        Node <&Node String>

        A group input socket of type String is created if the name is not None.

        Arguments
        ---------
        - value (str or Socket) : initial value
        - name (str = None) : group input socket name if not None
        - tip (str = None) : user type for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                assert(False)
            else:
                bsock = Tree.new_input('NodeSocketShader', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Operators
