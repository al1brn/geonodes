#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-18
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
# Data class Object

class Object(dsock.Object):
    """ Data class Object
    """

    def copy(self):

        return Object(self)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Object
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Object
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'OBJECT'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='OBJECT', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='OBJECT', label=node_label, node_color=node_color).output

    def info(self, as_instance=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color)
                
        """

        return nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color)

    def location(self, as_instance=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                location in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).location
                
        """

        return nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).location

    def rotation(self, as_instance=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                rotation in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).rotation
                
        """

        return nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).rotation

    def scale(self, as_instance=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                scale in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).scale
                
        """

        return nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).scale

    def geometry(self, as_instance=None, transform_space='ORIGINAL', node_label = None, node_color = None):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                geometry in Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).geometry
                
        """

        return nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=node_label, node_color=node_color).geometry


