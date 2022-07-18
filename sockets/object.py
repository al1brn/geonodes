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
# Data class Object

class Object(dsock.Object):
    """ Data class Object
    """

    def copy(self):

        return Object(self)


    def reset_properties(self):

        super().reset_properties()

        self.info_ = None

        self.location_ = None

        self.rotation_ = None

        self.scale_ = None

        self.geometry_ = None

    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                
            Returns:
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
                
        """

        if self.info_ is None:
            self.info_ = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
        return self.info_

    @property
    def location(self, as_instance=None, transform_space='ORIGINAL'):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                
            Returns:
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.location")
                
        """

        return self.info.location

    @property
    def rotation(self, as_instance=None, transform_space='ORIGINAL'):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                
            Returns:
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.rotation")
                
        """

        return self.info.rotation

    @property
    def scale(self, as_instance=None, transform_space='ORIGINAL'):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                
            Returns:
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.scale")
                
        """

        return self.info.scale

    @property
    def geometry(self, as_instance=None, transform_space='ORIGINAL'):
        """ Geometry node [*Object Info*].
        
        
            Args:
                as_instance: Boolean
                transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]
                
            Returns:
                Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ObjectInfo`
            
            
            .. blid:: GeometryNodeObjectInfo
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.geometry")
                
        """

        return self.info.geometry


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


