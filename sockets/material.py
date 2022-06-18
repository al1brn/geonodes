#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-18
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
    """ 

    Data socket Material
    --------------------
        > Inherits from dsock.Material
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - selection : selection (Boolean)
            - switch : output (Material)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = material.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Material (self)
            - switch : Boolean
            - true : Material## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'MATERIAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='MATERIAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Material
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='MATERIAL', label=node_label, node_color=node_color).output

    def selection(self, node_label = None, node_color = None):
        """ > Node: MaterialSelection
          
        <sub>go to: top index
        blender ref GeometryNodeMaterialSelection
        node ref Material Selection </sub>
                                  
        ```python
        v = material.selection(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - material : Material (self)## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MaterialSelection(material=self, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.MaterialSelection(material=self, label=node_label, node_color=node_color).selection


