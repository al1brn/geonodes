#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-17
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
from geonodes.core.domains import Domain
from geonodes import PointDomain, EdgeDomain, FaceDomain, CornerDomain, CurveDomain

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Image

class Image(dsock.Image):
    """ 

    Data socket Image
    -----------------
        > Inherits from dsock.Image
          
        <sub>go to index</sub>
        
        
    

        Methods
        -------
            - switch : output (Image)
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = image.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Image (self)
            - switch : Boolean
            - true : Image## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'IMAGE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='IMAGE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Image
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='IMAGE', label=node_label, node_color=node_color).output


