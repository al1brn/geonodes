#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : staticclass
--------------------
- Functional nodes

Functional nodes are nodes which can't be considered as methods or properties of a data class.
Functional nodes also include input nodes such as 'Position' or 'Index'. Theses nodes should be considered
as properties of geometry but to ease the scripting, there are also implemented as functions.

Functional nodes are implemented as static functions and properties or a class named nd which is short.

```  python
# Some functional nodes
pos = nd.position
i = nd.index
attr = named_attribute(name, 'FLOAT')
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
"""

import numpy as np

import bpy
from .treeclass import Node

class nd:

    # =============================================================================================================================
    # Geometry Read

    @classmethod
    @property
    def id(cls):
        return Node('ID')._out

    @classmethod
    @property
    def index(cls):
        return Node('Index')._out

    @classmethod
    @property
    def normal(cls):
        return Node('Normal')._out

    @classmethod
    @property
    def position(cls):
        return Node('Position')._out

    @classmethod
    @property
    def radius(cls):
        return Node('Radius')._out

    # =============================================================================================================================
    # Geometry Read

    @property
    def material_index(self):
        return Node('Material Index')._out

    @classmethod
    def material_selection(cls, material=None):
        return Node('Material Selection', {'Material': material})._out

    # ====================================================================================================
    # Scene nodes

    @classmethod
    @property
    def SceneTime(cls):
        return Node("Scene Time")

    @classmethod
    @property
    def seconds(cls):
        return cls.SceneTime.seconds

    @classmethod
    @property
    def frame(cls):
        return cls.SceneTime.frame

    @classmethod
    @property
    def is_viewport(cls):
        return Node("Is Viewport")._out

    @classmethod
    @property
    def self_object(cls):
        return Node("Self Object")._out

    @classmethod
    @property
    def active_camera(cls):
        return Node("Active Camera")._out
