#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : geonodesclass
----------------------
- Geometry nodes tree

classes
-------
- GeoNodes      : sub class of Tree

functions
---------

updates
-------
- creation : 2024/07/23
"""

from .treeclass import Tree, Node
from .staticclass import nd

class GeoNodes(Tree, nd):
    def __init__(self, name, clear=True, is_group=False, prefix=None):

        tree_name = name if prefix is None else f"{prefix} {name}"
        super().__init__(name, tree_type='GeometryNodeTree', clear=clear, is_group=is_group)

        self._btree.is_modifier = not is_group
