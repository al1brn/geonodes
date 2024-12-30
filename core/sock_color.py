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
- update : 2024/12/29
"""

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node, ColorRamp
from .socket_class import Socket
from .  import generated

# =============================================================================================================================
# =============================================================================================================================
# Color
# =============================================================================================================================
# =============================================================================================================================

class Color(generated.Color):

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
