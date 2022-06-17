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

class Field(Socket):
    
    def __init__(self, domain, selection=None, name=None):
        super().__init__(domain, node=domain.node)
        self.domain    = domain
        self.selection = selection
        self.name      = name
        
    @property
    def data
        
    def stack(self, geometry):
        
        
        
        

class Position(Field):
    
    def set_position(self, position=None, offset=None):
        return nodes.SetPosition()
        
        def __init__(self, geometry=None, selection=None, position=None, offset=None, label=None, node_color=None):

        
