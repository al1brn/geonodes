#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : colorclass
-------------------
- Implement color data socket

classes
-------
- Color         : Socket of type 'RGBA'

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node, ColorRamp
from .socketclass import Socket
from .vectorclass import VectorLike

# =============================================================================================================================
# =============================================================================================================================
# Color
# =============================================================================================================================
# =============================================================================================================================

class Color(VectorLike):

    SOCKET_TYPE = 'RGBA'

    def __init__(self, value: tuple | float | Socket | str | None =(0., 0., 0., 1.), name: str = None, tip: str = None):
        """ Socket of type COLOR (RGBA)

        > Nodes <&Node RGB> <&Node Combine Color> <&Node Color>

        Arguments
        ---------
        - value (tuple or Socket = (0, 0, 0, 1)) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        """

        if isinstance(value, str):
            value = type(self).Named(value)

        bsock = utils.get_bsocket(value)
        if bsock is None:
            if name is None:
                if np.shape(value) == (3,):
                    a = (value[0], value[1], value[2], 1)
                else:
                    a = utils.value_to_array(value, (4,))

                if utils.has_bsocket(a):
                    if Tree.is_geonodes:
                        bsock = Node('Combine Color', {0: a[0], 1: a[1], 2:a[2], 3:a[3]})._out
                    else:
                        bsock = Node('Combine Color', {0: a[0], 1: a[1], 2:a[2]})._out

                elif Tree.is_geonodes:
                    bsock = Node('Color', value=a)._out

                else:
                    bsock = Node('RGB')._out
                    bsock._bsocket.default_value = a
            else:
                bsock = Tree.new_input('NodeSocketColor', name, value=value, description=tip)

        super().__init__(bsock)

    # ====================================================================================================
    # Constructors

    @classmethod
    def Combine(cls, a=0, b=0, c=0, alpha=1, mode='RGB'):
        """ Constructor : Combine Color

        > Node <&Node Combine Color>

        Arguments
        ---------
        - a (Float) : depending on mode
        - b (Float) : depending on mode
        - c (Float) : depending on mode
        - alpha (Float) : alpha component
        - mode (str = 'RGB') = mode in ('RGB', 'HSV', 'HSL')

        Returns
        -------
        - Color
        """

        if Tree.is_shader:
            return Node('Combine Color', {0: a, 1: b, 2: c}, mode=mode)._out
        else:
            return Node('Combine Color', {0: a, 1: b, 2: c, 3: alpha}, mode=mode)._out

    @classmethod
    def CombineRGB(cls, red=0, green=0, blue=0, alpha=1):
        """ Constructor : Combine Color from RGB

        > Node <&Node Combine Color>

        Arguments
        ---------
        - red (Float)
        - green (Float)
        - blue (Float)
        - alpha (Float)

        Returns
        -------
        - Color
        """

        return cls.Combine(red, green, blue, alpha, mode='RGB')

    @classmethod
    def CombineHSV(cls, hue=0, saturation=0, value=0, alpha=1):
        """ Constructor : Combine Color from HSV

        > Node <&Node Combine Color>

        Arguments
        ---------
        - hue (Float)
        - saturation (Float)
        - value (Float)
        - alpha (Float)

        Returns
        -------
        - Color
        """
        return cls.Combine(hue, saturation, value, alpha, mode='HSV')

    @classmethod
    def CombineHSL(cls, hue=0, saturation=0, lightness=0, alpha=1):
        """ Constructor : Combine Color from HSL

        > Node <&Node Combine Color>

        Arguments
        ---------
        - hue (Float)
        - saturation (Float)
        - lightness (Float)
        - alpha (Float)

        Returns
        -------
        - Color
        """
        return cls.Combine(hue, saturation, lightness, alpha, mode='HSL')

    @classmethod
    def Blackbody(cls, temperature=None):
        """ Constructor : Black Body

        > Node <&Node Blackbody>

        Arguments
        ---------
        - temperature (Float)

        Returns
        -------
        - Color
        """
        return Node('Blackbody', {'Temperature': temperature})._out

    @classmethod
    def ColorRamp(cls, fac=None, stops=None):
        """ Constructor : Color Ramp

        > Node <&Node Color Ramp>

        Arguments
        ---------
        - fac (Float)
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)

        Returns
        -------
        - Color
        """
        return ColorRamp(fac=fac, stops=stops)._out

    # ====================================================================================================
    # Properties

    # ----- Separate color

    @property
    def RGB(self):
        """ Separate RGB Node

        > Node <&Node Separate Color>

        Returns
        -------
        - Node : 'Separate Color' node
        """
        return self._cache('Separate Color', {'Color': self}, mode='RGB', cache_name='RGB')

    @property
    def HSV(self):
        """ Separate HSV Node

        > Node <&Node Separate Color>

        Returns
        -------
        - Node : 'Separate Color' node
        """
        return self._cache('Separate Color', {'Color': self}, mode='HSV', cache_name='HSV')

    @property
    def HSL(self):
        """ Separate HSL Node

        > Node <&Node Separate Color>

        Returns
        -------
        - Node : 'Separate Color' node
        """
        return self._cache('Separate Color', {'Color': self}, mode='HSL', cache_name='HSL')

    @property
    def red(self):
        """ Red component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Red' socket
        """
        return self.RGB.red

    @property
    def green(self):
        """ Green component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Green' socket
        """
        return self.RGB.green

    @property
    def blue(self):
        """ Blue component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Blue' socket
        """
        return self.RGB.blue

    @property
    def alpha(self):
        """ Alpha component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Alpha' socket
        """
        node = self._cached_nodes.get('RGB')
        if node is None:
            node = self._cached_nodes.get('HSV')
        if node is None:
            node = self._cached_nodes.get('HSL')
        if node is None:
            node = self.RGB

        return node.alpha

    @property
    def hue(self):
        """ Hue component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Hue' socket
        """
        node = self._cached_nodes.get('HSV')
        if node is None:
            node = self._cached_nodes.get('HSL')
        if node is None:
            node = self.HSV
        return node.red

    @property
    def saturation(self):
        """ Saturation component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Saturation' socket
        """
        node = self._cached_nodes.get('HSV')
        if node is Node:
            node = self._cached_nodes.get('HSL')
        if node is None:
            node = self.HSV
        return node.green

    @property
    def value(self):
        """ Value component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Value' socket
        """
        return self.HSV.blue

    @property
    def lightness(self):
        """ Lightness component

        > Node <&Node Separate Color>

        Returns
        -------
        - Float : 'Lightness' socket
        """
        return self.HSL.blue

    @property
    def rgb(self):
        """ Triplet of RGB components

        > Node <&Node Separate Color>

        Returns
        -------
        - Triplet of Floats
        """
        return self.RGB.red, self.RGB.greeen, self.RGB.blue

    @property
    def hsl(self):
        """ Triplet of RGB components

        > Node <&Node Separate Color>

        Returns
        -------
        - Triplet of Floats
        """
        return self.HSL.red, self.HSL.greeen, self.HSL.blue

    @property
    def hsv(self):
        """ Triplet of RGB components

        > Node <&Node Separate Color>

        Returns
        -------
        - Triplet of Floats
        """
        return self.HSV.red, self.HSV.greeen, self.HSV.blue



    # ====================================================================================================
    # Methods

    # ----- Mix

    def mix(self, factor=None, other=None, clamp_result=False, clamp_factor=True, blend_type='MIX'):
        """ Mix with another color

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag
        - blend_type (str = 'MIX) : blend type in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE',
          'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT',
          'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')

        Returns
        -------
        - Color : 'Result' socket
        """
        return Node('Mix', {'Factor': factor, 'A': self, 'B': other},
            clamp_result=False, clamp_factor=True, blend_type=blend_type, data_type='RGBA')._out

    def darken(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : DARKEN

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DARKEN')

    def multiply(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : MULTIPLY

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='MULTIPLY')

    def burn(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : BURN

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='BURN')

    def lighten(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : LIGHTEN

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='LIGHTEN')

    def screen(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : SCREEN

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SCREEN')

    def dodge(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : DODGE

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DODGE')

    def add(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : ADD

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='ADD')

    def overlay(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : OVERLAY

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='OVERLAY')

    def soft_light(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : SOFT LIGHT

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SOFT_LIGHT')

    def linear_light(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : LINEAR LIGHT

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='LINEAR_LIGHT')

    def difference(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : DIFFERENCE

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DIFFERENCE')

    def exclusion(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : EXCLUSION

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='EXCLUSION')

    def subtract(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : SUBTRACT

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SUBTRACT')

    def divide(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : DIVIDE

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='DIVIDE')

    def mix_hue(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : HUE

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='HUE')

    def mix_saturation(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : SATURATION

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='SATURATION')

    def mix_color(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : COLOR

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='COLOR')

    def mix_value(self, factor=None, other=None, clamp_result=False, clamp_factor=True):
        """ Mix with another color : VALUE

        > Node <&Node Mix>

        Arguments
        ---------
        - factor (Float) : socket
        - other (Color) : socket
        - clamp_result (bool) : clamp result flag
        - clamp_factor (bool) : clamp factor flag

        Returns
        -------
        - Color : 'Result' socket
        """
        return self.mix(factor=factor, other=other, clamp_result=clamp_result, clamp_factor=clamp_factor, blend_type='VALUE')

    # ----- RGB curves

    def curves(self, fac=None, keep=None):
        """ Color curves.

        > Node <&Node RGB Curves>

        Arguments
        ---------
        - fac (Float) : socket

        Returns
        -------
        - Color : 'Color' socket
        """
        return Node('RGB Curves', {'Fac': fac, 'Color': self}, _keep=keep)._out

    # ----- Comparison

    def equal(self, other, epsilon=None):
        """ Compare with another Color : EQUAL

        > Node <&Node Compare>

        Arguments
        ---------
        - other (Color) : socket
        - epsilon (Float) : socket

        Returns
        -------
        - Boolean : 'Result' socket
        """
        # operation in ('EQUAL', 'NOT_EQUAL', 'BRIGHTER', 'DARKER')
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='RGBA', operation='EQUAL')._out

    def not_equal(self, other, epsilon=None):
        """ Compare with another Color : NOT EQUAL

        > Node <&Node Compare>

        Arguments
        ---------
        - other (Color) : socket
        - epsilon (Float) : socket

        Returns
        -------
        - Boolean : 'Result' socket
        """
        return Node("Compare", {'A': self, 'B': other, 'Epsilon': epsilon}, data_type='RGBA', operation='NOT_EQUAL')._out

    def brighter(self, other):
        """ Compare with another Color : BRIGHTER

        > Node <&Node Compare>

        Arguments
        ---------
        - other (Color) : socket

        Returns
        -------
        - Boolean : 'Result' socket
        """
        return Node("Compare", {'A': self, 'B': other}, data_type='RGBA', operation='BRIGHTER')._out

    def darker(self, other):
        """ Compare with another Color : DARKER

        > Node <&Node Compare>

        Arguments
        ---------
        - other (Color) : socket

        Returns
        -------
        - Boolean : 'Result' socket
        """
        return Node("Compare", {'A': self, 'B': other}, data_type='RGBA', operation='DARKER')._out

    # ====================================================================================================
    # Shader

    def out(self, name=None):
        """ > Connect to output

        [&SHADER]

        > [!IMPORTANT]
        > - Geometry Nodes : create a group output socket with the provided name
        > - Shader : create a node <&ShaderNode AOV Output>
        """
        if self._tree._btree.bl_idname == 'ShaderNodeTree' and not self._tree._is_group:
            if name is None:
                name = 'Color'
            self._tree.aov_output(name=name, color=self)
        else:
            super().out(name=name)

    # ----- Input

    @classmethod
    def Attribute(cls, name):
        """ Shader node Color Attribute.

        [&SHADER]
        > Node <&ShaderNode Color Attribute>

        Arguments
        ---------
        - name (str)

        Returns
        -------
        - Color : 'Color' socket, [alpha_]

        """
        return Node('Color Attribute', layer_name=name)._out

    def ambient_occlusion(self, distance=None, normal=None, inside=False, only_local=False, samples=16):
        """ Shader node Ambient Occlusion.

        [&SHADER]
        > Node <&ShaderNode Color Attribute>

        Arguments
        ---------
        - distance (Float) : socket
        - inside (Vector) : socket
        - inside (bool) : parameter
        - only_local (bool) : parameter
        - samples (int) : parameter

        Returns
        -------
        - Color : 'Color' socket, [ao_]

        """
        return Node('Ambient Occlusion', {'Color': self, 'Distance': distance, 'Normal': normal}, inside=inside, only_local=only_local, samples=samples)._out

    # ----- Converter

    @classmethod
    def Blackbody(cls, temperature=None):
        """ Constructor : Black body.

        [&SHADER]
        > Node <&ShaderNode Blackbody>

        Arguments
        ---------
        - temperature (Float) : socket

        Returns
        -------
        - Color : 'Color' socket
        """
        return Node('Blackbody', {'Temperature': temperature})._out

    @classmethod
    def FromShader(cls, shader):
        """ Constructor : Shader to RGB.

        [&SHADER]
        > Node <&ShaderNode Shader to RGB>

        Arguments
        ---------
        - shader (Shader) : socket

        Returns
        -------
        - Color : 'Color' socket, [alpha_]
        """
        return Node('Shader to RGB', {'Shader': shader})._out

    @classmethod
    def Wavelength(cls, wavelength=None):
        """ Constructor : Wave Length.

        [&SHADER]
        > Node <&ShaderNode Wavelength>

        Arguments
        ---------
        - wavelength (Float) : socket

        Returns
        -------
        - Color : 'Color' socket
        """
        return Node('Wavelength', {'Wavelength': wavelength})._out

    @property
    def to_bw(self):
        """ Conversion to black and white.

        [&SHADER]
        > Node <&ShaderNode RGB to BW>

        Returns
        -------
        - Float : 'Val' socket
        """
        return Node('RGB to BW', {'Color': self})._out

    # ----- Color

    def brightness_contrast(self, bright=None, contrast=None):
        """ Brightness and contrast.

        [&SHADER]
        > Node <&ShaderNode Brightness/Contrast>

        Arguments
        ---------
        - bright (Float) : socket
        - contrast (Float) : socket

        Returns
        -------
        - Color : 'Color' socket
        """
        return Node('Brightness/Contrast', {'Color': self, 'Bright': bright, 'Contrast': contrast})._out

    def gamma(self, gamma=None):
        """ Gamma.

        [&SHADER]
        > Node <&ShaderNode Gamma>

        Arguments
        ---------
        - gamma (Float) : socket

        Returns
        -------
        - Color : 'Gamma' socket
        """
        node = Node('Gamma', {'Color': self, 'Gamma': gamma})
        return node._out

    def hue_saturation_value(self, hue=None, saturation=None, value=None, fac=None):
        """ Hue / saturation / value.

        [&SHADER]
        > Node <&ShaderNode Hue/Saturation/Value>

        Arguments
        ---------
        - hue (Float) : socket
        - saturation (Float) : socket
        - value (Float) : socket
        - fac (Float) : socket

        Returns
        -------
        - Color : 'Color' socket
        """
        node = Node('Hue/Saturation/Value', {'Hue': hue, 'Saturation': saturation, 'Value': value, 'Fac': fac, 'Color': self})
        return node._out

    def invert(self, fac=None):
        """ Invert.

        [&SHADER]
        > Node <&ShaderNode Invert Color>

        Arguments
        ---------
        - fac (Float) : socket

        Returns
        -------
        - Color : 'Color' socket
        """
        node = Node('Invert Color', {'Fac': fac, 'Color': self})
        return node._out

    def normal_map(self, strength=None, space='TANGENT', uv_map=''):
        """ Normal map.

        [&SHADER]
        > Node <&ShaderNode Normal Map>

        Arguments
        ---------
        - strength (Float) : socket
        - space (str = 'TANGENT') : str in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')

        Returns
        -------
        - Color : 'Color' socket
        """
        node = Node('Normal Map', {'Strength': strength, 'Color': self}, space=space, uv_map=uv_map)
        return node._out

    def vector_displacement(self, midlevel=None, scale=None, space='TANGENT'):
        """ Vector displacement

        [&SHADER]
        > Node <&ShaderNode Vector Displacement>

        Arguments
        ---------
        - strength (Float) : socket
        - midlevel (Float) : socket
        - scale (Float) : socket
        - space (str = 'TANGENT') : str in ('TANGENT', 'OBJECT', 'WORLD')

        Returns
        -------
        - Vector : 'Displacement' socket
        """
        node = Node('Vector Displacement', {'Vector': self, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out
