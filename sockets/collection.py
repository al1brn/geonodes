#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-07-03
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
    """ 

    Data socket Collection
    ----------------------
        > Inherits from dsock.Collection
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - info : geometry (Geometry)
            - switch : output (Collection)
    """


    def copy(self):

        return Collection(self)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = collection.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Collection (self)
            - switch : Boolean
            - true : Collection## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'COLLECTION'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='COLLECTION', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Collection
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='COLLECTION', label=node_label, node_color=node_color).output

    def info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ > Node: CollectionInfo
          
        <sub>go to: top index
        blender ref GeometryNodeCollectionInfo
        node ref Collection Info </sub>
                                  
        ```python
        v = collection.info(separate_children, reset_children, transform_space, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - collection : Collection (self)
            - separate_children : Boolean
            - reset_children : Boolean## Parameters
            - transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, label=node_label, node_color=node_color).geometry


