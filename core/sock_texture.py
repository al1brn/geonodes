#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : textures
-----------------
- Create the textures

This module implements texture creation as class methods of Texture class.
Texture class inherits from TextureRoot which can be created as a Group Input.

```  python
# Create a noise texture
noise_node = Texture.Noise()
```

classes
-------
- Texture       : Implements the texture nodes creation
    - Brick
    - Checker
    - Gradient
    - Image
    - Magic
    - Noise
    - Voronoi
    - Wave
    - WhiteNoise

functions
---------

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

class Texture(generated.Texture):

    SOCKET_TYPE = 'TEXTURE'

    def __init__(self, value: bpy.types.Texture | Socket | None = None, name: str | None = None, tip: str | None = None):
        """ Socket of type Texture

        Arguments
        ---------
        - value (bpy.types.Texture or str = None) : image or image name in bpy.data.images
        - name (str = None) : create a group input socket of type Image if not None
        - tip (str = None) : user tip for group input socket
        """

        bsock = utils.get_bsocket(value)
        if bsock is None:
            image = utils.get_blender_resource('TEXTURE', value)
            if name is None:
                name = "Texture"
            bsock = Tree.new_input('NodeSocketTexture', name=name, value=image, description=tip)

        super().__init__(bsock)
