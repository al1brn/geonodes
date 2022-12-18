#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-12-12
@author: Generated from generator module
Blender version: 3.4.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Color

class Color(dsock.Color):
    """ Data class Color
    """

    def copy(self):

        return Color(self)


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, red=None, green=None, blue=None, alpha=None, mode='RGB', node_label = None, node_color = None):
        """ Geometry node [*Combine Color*].
        
        
            Args:
                red: Float
                green: Float
                blue: Float
                alpha: Float
                mode (str): 'RGB' in [RGB, HSV, HSL]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CombineColor`
            
            
            .. blid:: FunctionNodeCombineColor
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode=mode, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode=mode, label=node_label, node_color=node_color).color)

    @classmethod
    def CombineRGB(cls, red=None, green=None, blue=None, alpha=None, node_label = None, node_color = None):
        """ Geometry node [*Combine Color*].
        
        
            Args:
                red: Float
                green: Float
                blue: Float
                alpha: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CombineColor`
            
                - mode = 'RGB'
                  
            .. blid:: FunctionNodeCombineColor
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB', label=node_label, node_color=node_color).color)

    @classmethod
    def CombineHSV(cls, hue=None, saturation=None, value=None, alpha=None, node_label = None, node_color = None):
        """ Geometry node [*Combine Color*].
        
        
            Args:
                red: Float
                green: Float
                blue: Float
                alpha: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CombineColor`
            
                - mode = 'HSV'
                  
            .. blid:: FunctionNodeCombineColor
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV', label=node_label, node_color=node_color).color)

    @classmethod
    def CombineHSL(cls, hue=None, saturation=None, lightness=None, alpha=None, node_label = None, node_color = None):
        """ Geometry node [*Combine Color*].
        
        
            Args:
                red: Float
                green: Float
                blue: Float
                alpha: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CombineColor`
            
                - mode = 'HSL'
                  
            .. blid:: FunctionNodeCombineColor
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSL', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSL', label=node_label, node_color=node_color).color)


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
                Sockets [geometry (Geometry), attribute (Color)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CaptureAttribute`
            
                - data_type = 'FLOAT_COLOR'
                  
            .. blid:: GeometryNodeCaptureAttribute
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)

    def field_at_index(self, index=None, domain='POINT', node_label = None, node_color = None):
        """ Geometry node [*Field at Index*].
        
        
            Args:
                index: Integer
                domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FieldAtIndex`
            
                - data_type = 'FLOAT_COLOR'
                  
            .. blid:: GeometryNodeFieldAtIndex
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
                
        """

        return nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color).value

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
                Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Color)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Raycast`
            
                - data_type = 'FLOAT_COLOR'
                  
            .. blid:: GeometryNodeRaycast
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping, label=node_label, node_color=node_color)
                
        """

        return nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping, label=node_label, node_color=node_color)

    def switch(self, switch=None, true=None, node_label = None, node_color = None):
        """ Geometry node [*Switch*].
        
        
            Args:
                switch: Boolean
                true: Color
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Switch`
            
                - input_type = 'RGBA'
                  
            .. blid:: GeometryNodeSwitch
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Switch(false=self, switch=switch, true=true, input_type='RGBA', label=node_label, node_color=node_color)
                
        """

        return nodes.Switch(false=self, switch=switch, true=true, input_type='RGBA', label=node_label, node_color=node_color).output

    def equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Color
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'RGBA'
                - mode = 'ELEMENT'
                - operation = 'EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color).result

    def not_equal(self, b=None, epsilon=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Color
                epsilon: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'RGBA'
                - mode = 'ELEMENT'
                - operation = 'NOT_EQUAL'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color).result

    def brighter(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Color
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'RGBA'
                - mode = 'ELEMENT'
                - operation = 'BRIGHTER'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER', label=node_label, node_color=node_color).result

    def darker(self, b=None, node_label = None, node_color = None):
        """ Geometry node [*Compare*].
        
        
            Args:
                b: Color
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Boolean
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Compare`
            
                - data_type = 'RGBA'
                - mode = 'ELEMENT'
                - operation = 'DARKER'
                  
            .. blid:: FunctionNodeCompare
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER', label=node_label, node_color=node_color)
                
        """

        return nodes.Compare(a=self, b=b, data_type='RGBA', mode='ELEMENT', operation='DARKER', label=node_label, node_color=node_color).result

    def separate_color(self, mode='RGB', node_label = None, node_color = None):
        """ Geometry node [*Separate Color*].
        
        
            Args:
                mode (str): 'RGB' in [RGB, HSV, HSL]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [red (Float), green (Float), blue (Float), alpha (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateColor`
            
            
            .. blid:: FunctionNodeSeparateColor
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateColor(color=self, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.SeparateColor(color=self, mode=mode, label=node_label, node_color=node_color)

    def curves(self, fac=None, node_label = None, node_color = None):
        """ Geometry node [*RGB Curves*].
        
        
            Args:
                fac: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.RgbCurves`
            
            
            .. blid:: ShaderNodeRGBCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.RgbCurves(color=self, fac=fac, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.RgbCurves(color=self, fac=fac, label=node_label, node_color=node_color))


