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
# Data class Color

class Color(dsock.Color):
    """ Data class Color
    """

    def copy(self):

        return Color(self)


    def reset_properties(self):

        super().reset_properties()

        self.separate_ = None

        self.r_ = None

        self.g_ = None

        self.b_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def Combine(cls, r=None, g=None, b=None, node_label = None, node_color = None):
        """ Geometry node [*Combine RGB*].
        
        
            Args:
                r: Float
                g: Float
                b: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CombineRgb`
            
            
            .. blid:: ShaderNodeCombineRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CombineRgb(r=r, g=g, b=b, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CombineRgb(r=r, g=g, b=b, label=node_label, node_color=node_color).image)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def separate(self):
        """ Geometry node [*Separate RGB*].
        
        
        
            Returns:
                Sockets [r (Float), g (Float), b (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateRgb`
            
            
            .. blid:: ShaderNodeSeparateRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
                
        """

        if self.separate_ is None:
            self.separate_ = nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.separate")
        return self.separate_

    @property
    def r(self):
        """ Geometry node [*Separate RGB*].
        
        
        
            Returns:
                Sockets [r (Float), g (Float), b (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateRgb`
            
            
            .. blid:: ShaderNodeSeparateRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.r")
                
        """

        return self.separate.r

    @r.setter
    def r(self, value):
        self.separate.r = value

    @property
    def g(self):
        """ Geometry node [*Separate RGB*].
        
        
        
            Returns:
                Sockets [r (Float), g (Float), b (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateRgb`
            
            
            .. blid:: ShaderNodeSeparateRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.g")
                
        """

        return self.separate.g

    @g.setter
    def g(self, value):
        self.separate.g = value

    @property
    def b(self):
        """ Geometry node [*Separate RGB*].
        
        
        
            Returns:
                Sockets [r (Float), g (Float), b (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SeparateRgb`
            
            
            .. blid:: ShaderNodeSeparateRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SeparateRgb(image=self, label=f"{self.node_chain_label}.b")
                
        """

        return self.separate.b

    @b.setter
    def b(self, value):
        self.separate.b = value


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

    def mix(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'MIX'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def darken(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'DARKEN'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def multiply(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'MULTIPLY'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def burn(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'BURN'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def lighten(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'LIGHTEN'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def screen(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'SCREEN'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def dodge(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'DODGE'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def add(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'ADD'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def overlay(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'OVERLAY'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def soft_light(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'SOFT_LIGHT'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def linear_light(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'LINEAR_LIGHT'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def difference(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'DIFFERENCE'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def subtract(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'SUBTRACT'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def divide(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'DIVIDE'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def hue(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'HUE'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def saturation(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'SATURATION'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def mix_color(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'COLOR'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha, label=node_label, node_color=node_color).color

    def value(self, color2=None, fac=None, use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
                - blend_type = 'VALUE'
                  
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha, label=node_label, node_color=node_color).color

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

    def mix(self, color2=None, fac=None, blend_type='MIX', use_alpha=False, node_label = None, node_color = None):
        """ Geometry node [*Mix*].
        
        
            Args:
                color2: Color
                fac: Float
                blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
                use_alpha (bool): False
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Color
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Mix`
            
            
            .. blid:: ShaderNodeMixRGB
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha, label=node_label, node_color=node_color)
                
        """

        return nodes.Mix(color1=self, color2=color2, fac=fac, blend_type=blend_type, use_alpha=use_alpha, label=node_label, node_color=node_color).color


