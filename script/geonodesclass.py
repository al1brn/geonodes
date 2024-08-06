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
    def __init__(self, tree_name, clear=True, fake_user=False, is_group=False, prefix=None):

        super().__init__(tree_name, tree_type='GeometryNodeTree', clear=clear, fake_user=fake_user, is_group=is_group, prefix=prefix)

        self._btree.is_modifier = not is_group
