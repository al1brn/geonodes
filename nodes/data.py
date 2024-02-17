#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Feb  2 11:43:35 2024

@author: alain.bernard
@email: alain@ligloo.net

-----

Python to nodes module

NodeSocket
"""

import numpy as np

import bpy
from geopy.nodes.utils import get_tree, del_tree, snake_case, io_sock_key, value_for
from geopy.nodes.sockets import Sockets
from geopy.nodes.node import Node


class Data:
    def __init__(self, value, node=None, tree=None):
        self.value = value
        self.node  = node
        self.tree  = tree
        
    @property
    def is_socket(self):
        return isinstance(value, bpy.types.NodeSocket)
    
    @property
    def is_value(self):
        return not self.is_socket
    
    def __getattr__(self, node_name):
        
    
    
class Integer(TreeData):
    pass

class NodeSocket:
    def __init__(self, bnode, bsocket):
        pass
    
    
    
        