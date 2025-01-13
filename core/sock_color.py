"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : sock_color
-------------------
- Color socket

This class inherits from Socket and from generated.Color
which is automatically generated.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

import numpy as np

import bpy
from . import utils
from .treeclass import Tree, Node, ColorRamp, NodeCurves
from .socket_class import Socket
from .  import generated

# =============================================================================================================================
# =============================================================================================================================
# Color
# =============================================================================================================================
# =============================================================================================================================

class Color(generated.Color):

    SOCKET_TYPE = 'RGBA'

    def __init__(self, value=(0., 0., 0., 1.), name=None, tip=None, panel=None,
        default_attribute="", hide_value=False, hide_in_modifier=False, single_value=False):
        """ Socket of type COLOR (RGBA)

        > Nodes <&Node RGB> <&Node Combine Color> <&Node Color>

        Arguments
        ---------
        - value (tuple or Socket = (0, 0, 0, 1)) : initial value
        - name (str = None) : Create an Group Input socket with the provided str if not None
        - tip (str = None) : User tip (for Group Input sockets)
        - panel (str = None) : panel name (overrides tree panel if exists)
        - default_attribute (str = "") : default attribute name
        - hide_value (bool = False) : Hide Value option
        - hide_in_modifier (bool = False) : Hide in Modifier option
        - single_value (bool = False) : Single Value option
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
                bsock = Tree.new_input('NodeSocketColor', name, value=value, panel=panel,
                    description             = tip,
                    default_attribute_name  = default_attribute,
                    hide_value              = hide_value,
                    hide_in_modifier        = hide_in_modifier,
                    force_non_field         = single_value,
                )

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

    def curves(self, fac=None, curves=None):
        """ > Node <&Node RGB Curves>

        A curve is defined by a list of 3-tuples (not list):
        - x (float) : x position
        - y (float) : y position
        - handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        > [!NOTE]
        > handle_type is optional, its default value is 'AUTO'. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

        Information
        -----------
        - Socket 'Color' : self

        Arguments
        ---------
        - fac (Float) : socket 'Fac' (id: Fac)
        - curves (list of lists of tuples (float, float, str)) : curves points

        Returns
        -------
        - Color
        """
        node = NodeCurves('RGB Curves', sockets={'Color': self, 'Fac': fac})
        node.set_curves(curves)
        return node._out
