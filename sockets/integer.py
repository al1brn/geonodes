#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-24
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
# Data class Integer

class Integer(dsock.Integer):
    """ 

    Data socket Integer
    -------------------
        > Inherits from dsock.Integer
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Random : value (Integer)
    

        Methods
        -------
            - abs : value (Float)
            - accumulate_field : Sockets      [leading (Integer), trailing (Integer), total (Integer)]
            - add : value (Float)
            - arccos : value (Float)
            - arcsin : value (Float)
            - arctan : value (Float)
            - arctan2 : value (Float)
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Integer)]
            - ceil : value (Float)
            - compare : value (Float)
            - cos : value (Float)
            - cosh : value (Float)
            - degrees : value (Float)
            - divide : value (Float)
            - equal : result (Boolean)
            - exp : value (Float)
            - field_at_index : value (Integer)
            - floor : value (Float)
            - fract : value (Float)
            - greater_equal : result (Boolean)
            - greater_than : result (Boolean)
            - greater_than : value (Float)
            - inverse_sqrt : value (Float)
            - less_equal : result (Boolean)
            - less_than : result (Boolean)
            - less_than : value (Float)
            - log : value (Float)
            - max : value (Float)
            - min : value (Float)
            - modulo : value (Float)
            - multiply : value (Float)
            - multiply_add : value (Float)
            - not_equal : result (Boolean)
            - pingpong : value (Float)
            - pow : value (Float)
            - radians : value (Float)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
            - round : value (Float)
            - sign : value (Float)
            - sin : value (Float)
            - sinh : value (Float)
            - smooth_max : value (Float)
            - smooth_min : value (Float)
            - snap : value (Float)
            - sqrt : value (Float)
            - subtract : value (Float)
            - switch : output (Integer)
            - tan : value (Float)
            - tanh : value (Float)
            - trunc : value (Float)
            - wrap : value (Float)
    """


    def copy(self):

        return Integer(self)


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None, node_label = None, node_color = None):
        """ > Node: RandomValue
          
        <sub>go to: top index
        blender ref FunctionNodeRandomValue
        node ref Random Value </sub>
                                  
        ```python
        v = Integer.Random(min, max, ID, seed, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - min : Integer
            - max : Integer
            - ID : Integer
            - seed : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT', label=node_label, node_color=node_color).value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: AccumulateField
          
        <sub>go to: top index
        blender ref GeometryNodeAccumulateField
        node ref Accumulate Field </sub>
                                  
        ```python
        v = integer.accumulate_field(group_index, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Integer (self)
            - group_index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [leading (Integer), trailing (Integer), total (Integer)]
            
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain, label=node_label, node_color=node_color)

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = integer.capture_attribute(geometry, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Integer (self)
            - geometry : Geometry## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Integer)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, value=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
                                  
        ```python
        v = integer.field_at_index(value, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - index : Integer (self)
            - value : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label = None, node_color = None):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
                                  
        ```python
        v = integer.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Integer (self)
            - target_geometry : Geometry
            - source_position : Vector
            - ray_direction : Vector
            - ray_length : Float## Parameters
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = integer.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Integer (self)
            - switch : Boolean
            - true : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'INT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='INT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='INT', label=node_label, node_color=node_color).output

    def less_than(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.less_than(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Integer (self)
            - b : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
            - mode : 'ELEMENT'
            - operation : 'LESS_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def less_equal(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.less_equal(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Integer (self)
            - b : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
            - mode : 'ELEMENT'
            - operation : 'LESS_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def greater_than(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.greater_than(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Integer (self)
            - b : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
            - mode : 'ELEMENT'
            - operation : 'GREATER_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def greater_equal(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.greater_equal(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Integer (self)
            - b : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
            - mode : 'ELEMENT'
            - operation : 'GREATER_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def equal(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.equal(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Integer (self)
            - b : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
            - mode : 'ELEMENT'
            - operation : 'EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = integer.not_equal(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Integer (self)
            - b : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'INT'
            - mode : 'ELEMENT'
            - operation : 'NOT_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def add(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.add(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ADD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='ADD', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='ADD', label=node_label, node_color=node_color).value

    def subtract(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.subtract(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SUBTRACT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color).value

    def multiply(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.multiply(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MULTIPLY'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color).value

    def divide(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.divide(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'DIVIDE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color).value

    def multiply_add(self, value1=None, value2=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.multiply_add(value1, value2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float
            - value2 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MULTIPLY_ADD'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).value

    def pow(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.pow(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'POWER'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='POWER', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='POWER', label=node_label, node_color=node_color).value

    def log(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.log(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'LOGARITHM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color).value

    def sqrt(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sqrt(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SQRT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SQRT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SQRT', label=node_label, node_color=node_color).value

    def inverse_sqrt(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.inverse_sqrt(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'INVERSE_SQRT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='INVERSE_SQRT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='INVERSE_SQRT', label=node_label, node_color=node_color).value

    def abs(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.abs(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ABSOLUTE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ABSOLUTE', label=node_label, node_color=node_color).value

    def exp(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.exp(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'EXPONENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='EXPONENT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='EXPONENT', label=node_label, node_color=node_color).value

    def min(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.min(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MINIMUM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color).value

    def max(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.max(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MAXIMUM'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color).value

    def less_than(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.less_than(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'LESS_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color).value

    def greater_than(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.greater_than(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'GREATER_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color).value

    def sign(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sign(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SIGN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SIGN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SIGN', label=node_label, node_color=node_color).value

    def compare(self, value1=None, value2=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.compare(value1, value2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float
            - value2 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'COMPARE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color).value

    def smooth_min(self, value1=None, value2=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.smooth_min(value1, value2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float
            - value2 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SMOOTH_MIN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color).value

    def smooth_max(self, value1=None, value2=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.smooth_max(value1, value2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float
            - value2 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SMOOTH_MAX'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color).value

    def round(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.round(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ROUND'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ROUND', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ROUND', label=node_label, node_color=node_color).value

    def floor(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.floor(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'FLOOR'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='FLOOR', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='FLOOR', label=node_label, node_color=node_color).value

    def ceil(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.ceil(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'CEIL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='CEIL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='CEIL', label=node_label, node_color=node_color).value

    def trunc(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.trunc(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'TRUNC'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='TRUNC', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='TRUNC', label=node_label, node_color=node_color).value

    def fract(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.fract(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'FRACT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='FRACT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='FRACT', label=node_label, node_color=node_color).value

    def modulo(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.modulo(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'MODULO'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='MODULO', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='MODULO', label=node_label, node_color=node_color).value

    def wrap(self, value1=None, value2=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.wrap(value1, value2, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float
            - value2 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'WRAP'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color).value

    def snap(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.snap(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SNAP'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='SNAP', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='SNAP', label=node_label, node_color=node_color).value

    def pingpong(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.pingpong(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'PINGPONG'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color).value

    def sin(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sin(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SINE', label=node_label, node_color=node_color).value

    def cos(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.cos(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'COSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='COSINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='COSINE', label=node_label, node_color=node_color).value

    def tan(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.tan(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'TANGENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='TANGENT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='TANGENT', label=node_label, node_color=node_color).value

    def arcsin(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arcsin(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ARCSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ARCSINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ARCSINE', label=node_label, node_color=node_color).value

    def arccos(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arccos(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ARCCOSINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ARCCOSINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ARCCOSINE', label=node_label, node_color=node_color).value

    def arctan(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arctan(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ARCTANGENT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='ARCTANGENT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='ARCTANGENT', label=node_label, node_color=node_color).value

    def arctan2(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.arctan2(value1, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)
            - value1 : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'ARCTAN2'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color).value

    def sinh(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.sinh(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'SINH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='SINH', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='SINH', label=node_label, node_color=node_color).value

    def cosh(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.cosh(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'COSH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='COSH', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='COSH', label=node_label, node_color=node_color).value

    def tanh(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.tanh(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'TANH'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='TANH', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='TANH', label=node_label, node_color=node_color).value

    def radians(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.radians(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'RADIANS'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='RADIANS', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='RADIANS', label=node_label, node_color=node_color).value

    def degrees(self, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = integer.degrees(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value0 : Float (self)## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - operation : 'DEGREES'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Math(value0=self, operation='DEGREES', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Math(value0=self, operation='DEGREES', label=node_label, node_color=node_color).value


