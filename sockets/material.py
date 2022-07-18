#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-07-17
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
# Data class Material

class Material(dsock.Material):
    """ Data class Material
    """

    def copy(self):

        return Material(self)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Material
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Material
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'MATERIAL'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='MATERIAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='MATERIAL', label=node_label, node_color=node_color).output

    def selection(self, node_label = None, node_color = None):
        """ Geometry node [*Material Selection*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.MaterialSelection`
            
            
            .. blid:: GeometryNodeMaterialSelection
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.MaterialSelection(material=self, label=node_label, node_color=node_color)
                
        """

        return nodes.MaterialSelection(material=self, label=node_label, node_color=node_color).selection


