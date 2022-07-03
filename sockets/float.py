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
# Data class Float

class Float(dsock.Float):
    """ 

    Data socket Float
    -----------------
        > Inherits from dsock.Float
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - Random : value (Float)
    

        Methods
        -------
            - abs : value (Float)
            - accumulate_field : Sockets      [leading (Float), trailing (Float), total (Float)]
            - add : value (Float)
            - arccos : value (Float)
            - arcsin : value (Float)
            - arctan : value (Float)
            - arctan2 : value (Float)
            - attribute_statistic : Sockets      [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
            - capture_attribute : Sockets      [geometry (Geometry), attribute (Float)]
            - ceil : value (Float)
            - clamp : result (Float)
            - color_ramp : Sockets      [color (Color), alpha (Float)]
            - compare : value (Float)
            - cos : value (Float)
            - cosh : value (Float)
            - curve : value (Float)
            - degrees : value (Float)
            - divide : value (Float)
            - equal : result (Boolean)
            - exp : value (Float)
            - field_at_index : value (Float)
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
            - map_range : result (Float)
            - max : value (Float)
            - min : value (Float)
            - modulo : value (Float)
            - multiply : value (Float)
            - multiply_add : value (Float)
            - not_equal : result (Boolean)
            - pingpong : value (Float)
            - pow : value (Float)
            - radians : value (Float)
            - raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
            - round : value (Float)
            - sign : value (Float)
            - sin : value (Float)
            - sinh : value (Float)
            - smooth_max : value (Float)
            - smooth_min : value (Float)
            - snap : value (Float)
            - sqrt : value (Float)
            - subtract : value (Float)
            - switch : output (Float)
            - tan : value (Float)
            - tanh : value (Float)
            - to_integer : integer (Integer)
            - to_string : string (String)
            - trunc : value (Float)
            - wrap : value (Float)
    """


    def copy(self):

        return Float(self)


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None, node_label = None, node_color = None):
        """ > Node: RandomValue
          
        <sub>go to: top index
        blender ref FunctionNodeRandomValue
        node ref Random Value </sub>
                                  
        ```python
        v = Float.Random(min, max, ID, seed, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - min : Float
            - max : Float
            - ID : Integer
            - seed : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT', label=node_label, node_color=node_color).value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: AccumulateField
          
        <sub>go to: top index
        blender ref GeometryNodeAccumulateField
        node ref Accumulate Field </sub>
                                  
        ```python
        v = float.accumulate_field(group_index, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - group_index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [leading (Float), trailing (Float), total (Float)]
            
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)

    def attribute_statistic(self, geometry=None, selection=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: AttributeStatistic
          
        <sub>go to: top index
        blender ref GeometryNodeAttributeStatistic
        node ref Attribute Statistic </sub>
                                  
        ```python
        v = float.attribute_statistic(geometry, selection, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Float (self)
            - geometry : Geometry
            - selection : Boolean## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
            
        """

        return nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: CaptureAttribute
          
        <sub>go to: top index
        blender ref GeometryNodeCaptureAttribute
        node ref Capture Attribute </sub>
                                  
        ```python
        v = float.capture_attribute(geometry, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - geometry : Geometry## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), attribute (Float)]
            
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, index=None, domain='POINT', node_label = None, node_color = None):
        """ > Node: FieldAtIndex
          
        <sub>go to: top index
        blender ref GeometryNodeFieldAtIndex
        node ref Field at Index </sub>
                                  
        ```python
        v = float.field_at_index(index, domain, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - index : Integer## Parameters
            - domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color).value

    def raycast(self, target_geometry=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label = None, node_color = None):
        """ > Node: Raycast
          
        <sub>go to: top index
        blender ref GeometryNodeRaycast
        node ref Raycast </sub>
                                  
        ```python
        v = float.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - attribute : Float (self)
            - target_geometry : Geometry
            - source_position : Vector
            - ray_direction : Vector
            - ray_length : Float## Parameters
            - mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
            
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ > Node: Switch
          
        <sub>go to: top index
        blender ref GeometryNodeSwitch
        node ref Switch </sub>
                                  
        ```python
        v = float.switch(switch, true, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - false : Float (self)
            - switch : Boolean
            - true : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - input_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Switch(false=self, switch=switch, true=true, input_type='FLOAT', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='FLOAT', label=node_label, node_color=node_color).output

    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR', node_label = None, node_color = None):
        """ > Node: MapRange
          
        <sub>go to: top index
        blender ref ShaderNodeMapRange
        node ref Map Range </sub>
                                  
        ```python
        v = float.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - from_min : Float
            - from_max : Float
            - to_min : Float
            - to_max : Float## Parameters
            - clamp : True
            - interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type, label=node_label, node_color=node_color).result

    def less_than(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = float.less_than(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Float (self)
            - b : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
            - mode : 'ELEMENT'
            - operation : 'LESS_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def less_equal(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = float.less_equal(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Float (self)
            - b : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
            - mode : 'ELEMENT'
            - operation : 'LESS_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def greater_than(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = float.greater_than(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Float (self)
            - b : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
            - mode : 'ELEMENT'
            - operation : 'GREATER_THAN'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def greater_equal(self, b=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = float.greater_equal(b, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Float (self)
            - b : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
            - mode : 'ELEMENT'
            - operation : 'GREATER_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = float.equal(b, epsilon, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Float (self)
            - b : Float
            - epsilon : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
            - mode : 'ELEMENT'
            - operation : 'EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ > Node: Compare
          
        <sub>go to: top index
        blender ref FunctionNodeCompare
        node ref Compare </sub>
                                  
        ```python
        v = float.not_equal(b, epsilon, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - a : Float (self)
            - b : Float
            - epsilon : Float## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - data_type : 'FLOAT'
            - mode : 'ELEMENT'
            - operation : 'NOT_EQUAL'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def add(self, value1=None, node_label = None, node_color = None):
        """ > Node: Math
          
        <sub>go to: top index
        blender ref ShaderNodeMath
        node ref Math </sub>
                                  
        ```python
        v = float.add(value1, node_label = None, node_color = None)
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
        v = float.subtract(value1, node_label = None, node_color = None)
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
        v = float.multiply(value1, node_label = None, node_color = None)
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
        v = float.divide(value1, node_label = None, node_color = None)
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
        v = float.multiply_add(value1, value2, node_label = None, node_color = None)
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
        v = float.pow(value1, node_label = None, node_color = None)
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
        v = float.log(value1, node_label = None, node_color = None)
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
        v = float.sqrt(node_label = None, node_color = None)
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
        v = float.inverse_sqrt(node_label = None, node_color = None)
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
        v = float.abs(node_label = None, node_color = None)
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
        v = float.exp(node_label = None, node_color = None)
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
        v = float.min(value1, node_label = None, node_color = None)
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
        v = float.max(value1, node_label = None, node_color = None)
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
        v = float.less_than(value1, node_label = None, node_color = None)
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
        v = float.greater_than(value1, node_label = None, node_color = None)
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
        v = float.sign(node_label = None, node_color = None)
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
        v = float.compare(value1, value2, node_label = None, node_color = None)
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
        v = float.smooth_min(value1, value2, node_label = None, node_color = None)
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
        v = float.smooth_max(value1, value2, node_label = None, node_color = None)
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
        v = float.round(node_label = None, node_color = None)
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
        v = float.floor(node_label = None, node_color = None)
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
        v = float.ceil(node_label = None, node_color = None)
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
        v = float.trunc(node_label = None, node_color = None)
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
        v = float.fract(node_label = None, node_color = None)
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
        v = float.modulo(value1, node_label = None, node_color = None)
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
        v = float.wrap(value1, value2, node_label = None, node_color = None)
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
        v = float.snap(value1, node_label = None, node_color = None)
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
        v = float.pingpong(value1, node_label = None, node_color = None)
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
        v = float.sin(node_label = None, node_color = None)
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
        v = float.cos(node_label = None, node_color = None)
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
        v = float.tan(node_label = None, node_color = None)
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
        v = float.arcsin(node_label = None, node_color = None)
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
        v = float.arccos(node_label = None, node_color = None)
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
        v = float.arctan(node_label = None, node_color = None)
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
        v = float.arctan2(value1, node_label = None, node_color = None)
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
        v = float.sinh(node_label = None, node_color = None)
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
        v = float.cosh(node_label = None, node_color = None)
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
        v = float.tanh(node_label = None, node_color = None)
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
        v = float.radians(node_label = None, node_color = None)
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
        v = float.degrees(node_label = None, node_color = None)
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

    def to_integer(self, rounding_mode='ROUND', node_label = None, node_color = None):
        """ > Node: FloatToInteger
          
        <sub>go to: top index
        blender ref FunctionNodeFloatToInt
        node ref Float to Integer </sub>
                                  
        ```python
        v = float.to_integer(rounding_mode, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - float : Float (self)## Parameters
            - rounding_mode : 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FloatToInteger(float=self, rounding_mode=rounding_mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        return nodes.FloatToInteger(float=self, rounding_mode=rounding_mode, label=node_label, node_color=node_color).integer

    def to_string(self, decimals=None, node_label = None, node_color = None):
        """ > Node: ValueToString
          
        <sub>go to: top index
        blender ref FunctionNodeValueToString
        node ref Value to String </sub>
                                  
        ```python
        v = float.to_string(decimals, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - decimals : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ValueToString(value=self, decimals=decimals, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            String
            
        """

        return nodes.ValueToString(value=self, decimals=decimals, label=node_label, node_color=node_color).string

    def color_ramp(self, node_label = None, node_color = None):
        """ > Node: ColorRamp
          
        <sub>go to: top index
        blender ref ShaderNodeValToRGB
        node ref ColorRamp </sub>
                                  
        ```python
        v = float.color_ramp(node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - fac : Float (self)## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ColorRamp(fac=self, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [color (Color), alpha (Float)]
            
        """

        return nodes.ColorRamp(fac=self, label=node_label, node_color=node_color)

    def curve(self, factor=None, node_label = None, node_color = None):
        """ > Node: FloatCurve
          
        <sub>go to: top index
        blender ref ShaderNodeFloatCurve
        node ref Float Curve </sub>
                                  
        ```python
        v = float.curve(factor, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - factor : Float## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FloatCurve(value=self, factor=factor, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return self.stack(nodes.FloatCurve(value=self, factor=factor, label=node_label, node_color=node_color))

    def clamp(self, min=None, max=None, clamp_type='MINMAX', node_label = None, node_color = None):
        """ > Node: Clamp
          
        <sub>go to: top index
        blender ref ShaderNodeClamp
        node ref Clamp </sub>
                                  
        ```python
        v = float.clamp(min, max, clamp_type, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - value : Float (self)
            - min : Float
            - max : Float## Parameters
            - clamp_type : 'MINMAX' in [MINMAX, RANGE]
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        return self.stack(nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type, label=node_label, node_color=node_color))


