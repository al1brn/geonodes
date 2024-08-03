#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
script nodes
- Scripting Geometry Nodes
-----------------------------------------------------

module : __init__
------------------
- low level constants uses by dynamic nodes generator
- dictionaries used to register the class created dynamically

modules
-------
- treearrange
- blendertree
- constants
- utils
- treeclass
- math
- textures
- socketclass
    - booleanclass
    - floatclass
    - vectorclass
    - colorclass
    - geometryclass
- zones


update : 2024/07/26
"""

import numpy as np

pi     = np.pi
tau    = 2*np.pi
halfpi = np.pi/2
d30    = np.pi/6
d45    = np.pi/4
d60    = np.pi/3
d90    = halfpi
d180   = pi
d270   = np.pi*1.5
d360   = tau

from .treeclass import Break, Tree, Layout, Node, Group
from .socketclass import Material, Image, Object, Collection, String, Menu
from .booleanclass import Boolean
from .floatclass import Float, Integer
from .vectorclass import Vector, Rotation, Matrix
from .colorclass import Color
from .geometryclass import Geometry, Mesh, Curve, Cloud, Instances, Volume
from .zones import Repeat, Simulation
from .textures import Texture
from .staticclass import nd
from . import gnmath
from .geonodesclass import GeoNodes
from . import macros
