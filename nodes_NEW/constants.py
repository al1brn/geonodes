#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:30:38 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : constants
------------------

created : 2024/07/21
"""

TREE_TYPES = [
    'GeometryNodeTree',
    'ShaderNodeTree',
    'CompositorNodeTree',
    'TextureNodeTree',
    ]

CURRENT_TREE = None
