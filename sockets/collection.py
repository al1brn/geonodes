#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-07-22
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Collection

class Collection(dsock.Collection):
    """ Data class Collection
    """

    def copy(self):

        return Collection(self)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Collection
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Collection
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'COLLECTION'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='COLLECTION', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='COLLECTION', label=node_label, node_color=node_color).output

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ Geometry node [*Collection Info*].
        
        
            Args:
                separate_children: Boolean
                reset_children: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CollectionInfo`
            
            
            .. blid:: GeometryNodeCollectionInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, label=node_label, node_color=node_color)
                
        """

        return nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, label=node_label, node_color=node_color).geometry


