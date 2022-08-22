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
# Data class Integer

class Integer(dsock.Integer):
    """ Data class Integer
    """

    def copy(self):

        return Integer(self)


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None, node_label = None, node_color = None):
        """ Geometry node [*Random Value*].
        
        
            Args:
                min: Integer
                max: Integer
                ID: Integer
                seed: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RandomValue`
            
                - data_type = 'INT'
                  
            .. blid:: FunctionNodeRandomValue
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT', label=node_label, node_color=node_color).value)


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def accumulate_field(self, group_index=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Accumulate Field*].
        
        
            Args:
                group_index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [leading (Integer), trailing (Integer), total (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.AccumulateField`
            
                - data_type = 'INT'
                  
            .. blid:: GeometryNodeAccumulateField
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain, label=node_label, node_color=node_color)

    def capture_attribute(self, geometry=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Capture Attribute*].
        
        
            Args:
                geometry: Geometry
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), attribute (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
            
                - data_type = 'INT'
                  
            .. blid:: GeometryNodeCaptureAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, value=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Field at Index*].
        
        
            Args:
                value: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
            
                - data_type = 'INT'
                  
            .. blid:: GeometryNodeFieldAtIndex
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color).value

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
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Raycast`
            
                - data_type = 'INT'
                  
            .. blid:: GeometryNodeRaycast
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Integer
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'INT'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='INT', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='INT', label=node_label, node_color=node_color).output

    def less_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'INT'
                - mode = 'ELEMENT'
                - operation = 'LESS_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color).result

    def less_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'INT'
                - mode = 'ELEMENT'
                - operation = 'LESS_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color).result

    def greater_than(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'INT'
                - mode = 'ELEMENT'
                - operation = 'GREATER_THAN'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color).result

    def greater_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'INT'
                - mode = 'ELEMENT'
                - operation = 'GREATER_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color).result

    def equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'INT'
                - mode = 'ELEMENT'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'INT'
                - mode = 'ELEMENT'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def multiply_add(self, value1=None, value2=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                value2: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'MULTIPLY_ADD'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color).value

    def pow(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'POWER'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='POWER', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='POWER', label=node_label, node_color=node_color).value

    def log(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'LOGARITHM'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color).value

    def sqrt(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SQRT'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='SQRT', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='SQRT', label=node_label, node_color=node_color).value

    def inverse_sqrt(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'INVERSE_SQRT'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='INVERSE_SQRT', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='INVERSE_SQRT', label=node_label, node_color=node_color).value

    def abs(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'ABSOLUTE'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='ABSOLUTE', label=node_label, node_color=node_color).value

    def exp(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'EXPONENT'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='EXPONENT', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='EXPONENT', label=node_label, node_color=node_color).value

    def min(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'MINIMUM'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color).value

    def max(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'MAXIMUM'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color).value

    def math_less_than(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'LESS_THAN'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color).value

    def math_greater_than(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'GREATER_THAN'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color).value

    def sign(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SIGN'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='SIGN', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='SIGN', label=node_label, node_color=node_color).value

    def compare(self, value1=None, value2=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                value2: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'COMPARE'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color).value

    def smooth_min(self, value1=None, value2=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                value2: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SMOOTH_MIN'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color).value

    def smooth_max(self, value1=None, value2=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                value2: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SMOOTH_MAX'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color).value

    def round(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'ROUND'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='ROUND', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='ROUND', label=node_label, node_color=node_color).value

    def floor(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'FLOOR'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='FLOOR', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='FLOOR', label=node_label, node_color=node_color).value

    def ceil(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'CEIL'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='CEIL', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='CEIL', label=node_label, node_color=node_color).value

    def trunc(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'TRUNC'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='TRUNC', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='TRUNC', label=node_label, node_color=node_color).value

    def fract(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'FRACT'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='FRACT', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='FRACT', label=node_label, node_color=node_color).value

    def modulo(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'MODULO'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='MODULO', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='MODULO', label=node_label, node_color=node_color).value

    def wrap(self, value1=None, value2=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                value2: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'WRAP'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color).value

    def snap(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SNAP'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='SNAP', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='SNAP', label=node_label, node_color=node_color).value

    def pingpong(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'PINGPONG'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color).value

    def sin(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SINE'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='SINE', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='SINE', label=node_label, node_color=node_color).value

    def cos(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'COSINE'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='COSINE', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='COSINE', label=node_label, node_color=node_color).value

    def tan(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'TANGENT'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='TANGENT', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='TANGENT', label=node_label, node_color=node_color).value

    def arcsin(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'ARCSINE'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='ARCSINE', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='ARCSINE', label=node_label, node_color=node_color).value

    def arccos(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'ARCCOSINE'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='ARCCOSINE', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='ARCCOSINE', label=node_label, node_color=node_color).value

    def arctan(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'ARCTANGENT'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='ARCTANGENT', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='ARCTANGENT', label=node_label, node_color=node_color).value

    def arctan2(self, value1=None, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                value1: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'ARCTAN2'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color).value

    def sinh(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'SINH'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='SINH', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='SINH', label=node_label, node_color=node_color).value

    def cosh(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'COSH'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='COSH', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='COSH', label=node_label, node_color=node_color).value

    def tanh(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'TANH'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='TANH', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='TANH', label=node_label, node_color=node_color).value

    def radians(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'RADIANS'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='RADIANS', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='RADIANS', label=node_label, node_color=node_color).value

    def degrees(self, node_label = None, node_color = None):
        """ Geometry node [*Math*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Math`
            
                - operation = 'DEGREES'
                  
            .. blid:: ShaderNodeMath
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Math(value0=self, operation='DEGREES', label=node_label, node_color=node_color)
                
        """

        return nodes.Math(value0=self, operation='DEGREES', label=node_label, node_color=node_color).value


