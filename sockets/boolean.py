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
# Data class Boolean

class Boolean(dsock.Boolean):
    """ 

    Data socket Boolean
    -------------------
        > Inherits from dsock.Boolean
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Random : value (Boolean)
    

        Methods
        -------
            - b_and : boolean (Boolean)
            - b_not : boolean (Boolean)
            - b_or : boolean (Boolean)
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Boolean)]
            - field_at_index : value (Boolean)
            - imply : boolean (Boolean)
            - nand : boolean (Boolean)
            - nimply : boolean (Boolean)
            - nor : boolean (Boolean)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
            - switch : output (Boolean)
            - transfer_attribute : attribute (Boolean)
            - xnor : boolean (Boolean)
            - xor : boolean (Boolean)
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, probability=None, ID=None, seed=None, node_label = None, node_color = None):
        """ > Node: RandomValue
          
        <sub>go to: top index
        blender ref FunctionNodeRandomValue
        node ref Random Value </sub>
                                  
        ```python
        v = Boolean.Random(probability, ID, seed, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - probability : Float
            - ID : Integer
            - seed : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return cls(nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN', label=node_label, node_color=node_color).value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def transfer_attribute(self, source=None, source_position=None, index=None, domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', node_label = None, node_color = None):
        """ > Node: TransferAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeTransfer
        node ref Transfer Attribute </sub>
                                  
        ```python
        v = boolean.transfer_attribute(source, source_position, index, domain, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Boolean (self)
            - source : Geometry
            - source_position : Vector
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color).attribute

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = boolean.capture_attribute(geometry, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Boolean (self)
            - geometry : Geometry## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Boolean)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, index=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
                                  
        ```python
        v = boolean.field_at_index(index, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Boolean (self)
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label = None, node_color = None):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
                                  
        ```python
        v = boolean.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Boolean (self)
            - target_geometry : Geometry
            - source_position : Vector
            - ray_direction : Vector
            - ray_length : Float## Parameters
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, false=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = boolean.switch(false, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - switch : Boolean (self)
            - false : Boolean
            - true : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'BOOLEAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(switch=self, false=false, true=true, input_type='BOOLEAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Switch(switch=self, false=false, true=true, input_type='BOOLEAN', label=node_label, node_color=node_color).output

    def b_and(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.b_and(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'AND'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color).boolean

    def b_or(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.b_or(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'OR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color).boolean

    def b_not(self, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.b_not(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'NOT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, operation='NOT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, operation='NOT', label=node_label, node_color=node_color).boolean

    def nand(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.nand(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'NAND'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color).boolean

    def nor(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.nor(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'NOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color).boolean

    def xnor(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.xnor(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'XNOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color).boolean

    def xor(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.xor(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'XOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color).boolean

    def imply(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.imply(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'IMPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color).boolean

    def nimply(self, boolean1=None, node_label = None, node_color = None):
        """ > Node: BooleanMath
          
        <sub>go to: top index
        blender ref FunctionNodeBooleanMath
        node ref Boolean Math </sub>
                                  
        ```python
        v = boolean.nimply(boolean1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - boolean0 : Boolean (self)
            - boolean1 : Boolean## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'NIMPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color).boolean


