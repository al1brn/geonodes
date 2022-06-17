#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:08:29 2022

@author: alain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket
from geonodes.nodes import nodes
from geonodes.nodes.nodes import create_node

import bpy

import logging
logger = logging.getLogger('geonodes')


# =============================================================================================================================
# A field is the basic geometry data
#
# mesh.verts.position += (1, 2, 3)
# mesh.verts.position = (1, 2, 3)

class Field:
    
    def __init__(self, geo_domain, selection=None, name=None):
        self.geo_domain  = geo_domain
        self.selection   = selection
        self.name        = name
        self.input_node_ = None
        
    @property
    def geometry(self):
        return self.geo_domain.data_socket
    
    @property
    def input_node(self):
        if self.input_node_ is None:
            self.create_input_node()
        return self.input_node_
    
    @property
    def node_socket(self):
        return self.input_node.get_datasocket(0)
    
    def create_input_node(self):
        raise RuntimeError("Input node not implemented !")
            
        
    def stack(self, node):
        return self.geo_domain.data_socket.stack(node)
    
    def select(self, selection):
        return type(self)(self.geo_domain, selection=selection, name=self.name)
    
    def set_value(self, value):
        raise RuntimeError("set_value not implemented !")
        
        

class Location(Field):
    
    def create_input_node(self):
        print("FIELD: AS ATTRIBUTE", self.geo_domain, self.geo_domain.domain)
        self.input_node_ = nodes.Position()
        self.input_node_.as_attribute(owning_socket=self.geo_domain.data_socket, domain=self.geo_domain.domain)
    
    def set_position(self, position=None, offset=None):
        return self.stack(nodes.SetPosition(geometry=self.geometry, selection=self.selection, position=position, offset=offset))
                          
    def __add__(self, value):
        self.set_position(position=value)
        
    def __iadd__(self, value):
        self.set_position(offset=value)
                          
    def set_value(self, value):
        self.set_position(position=value)

        
