#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-21
@author: Generated from generator module
Blender version: 3.2.2
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Boolean

class Boolean(dsock.Boolean):
    """ Data class Boolean
    """

    def copy(self):

        return Boolean(self)


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None, node_label = None, node_color = None):
        """ Geometry node [*Random Value*].
        
        
            Args:
                probability: Float
                ID: Integer
                seed: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RandomValue`
            
                - data_type = 'BOOLEAN'
                  
            .. blid:: FunctionNodeRandomValue
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN', label=node_label, node_color=node_color).value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Capture Attribute*].
        
        
            Args:
                geometry: Geometry
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), attribute (Boolean)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
            
                - data_type = 'BOOLEAN'
                  
            .. blid:: GeometryNodeCaptureAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, index=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Field at Index*].
        
        
            Args:
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
            
                - data_type = 'BOOLEAN'
                  
            .. blid:: GeometryNodeFieldAtIndex
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label = None, node_color = None):
        """ Geometry node [*Raycast*].
        
        
            Args:
                target_geometry: Geometry
                source_position: Vector
                ray_direction: Vector
                ray_length: Float
                mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Raycast`
            
                - data_type = 'BOOLEAN'
                  
            .. blid:: GeometryNodeRaycast
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, false=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                false: Boolean
                true: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'BOOLEAN'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(switch=self, false=false, true=true, input_type='BOOLEAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(switch=self, false=false, true=true, input_type='BOOLEAN', label=node_label, node_color=node_color).output

    def b_and(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'AND'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color).boolean

    def b_or(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'OR'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color).boolean

    def b_not(self, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'NOT'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, operation='NOT', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, operation='NOT', label=node_label, node_color=node_color).boolean

    def nand(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'NAND'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color).boolean

    def nor(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'NOR'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color).boolean

    def xnor(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'XNOR'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color).boolean

    def xor(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'XOR'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color).boolean

    def imply(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'IMPLY'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color).boolean

    def nimply(self, boolean1=None, node_label = None, node_color = None):
        """ Geometry node [*Boolean Math*].
        
        
            Args:
                boolean1: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BooleanMath`
            
                - operation = 'NIMPLY'
                  
            .. blid:: FunctionNodeBooleanMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color)
                
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color).boolean


