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

from typing import Literal

from . import colors
from . import utils
from .sockettype import SocketType
from .scripterror import NodeError
from .treeclass import Tree
from .nodeclass import Node, ColorRamp, NodeCurves
from .socket_class import Socket
from .  import generated

# =============================================================================================================================
# =============================================================================================================================
# Color
# =============================================================================================================================
# =============================================================================================================================

class Color(generated.Color):
    """ Color Socket.

    A Color can be created in various ways:
    - using a triplet : `col = Color((0.1, 0.2, 0.8))`
    - using a Combine method : `col = Color.CombineHSV(hue=0.6, saturation=0.7, value=0.3)
    - using a color name : `col = Color("red")`
    - using an hexa value : `col = Color("#0F4C8E")`

    Note that because a string is interpreted as a color name, you can use the syntax `Color(name)` to created
    a named attribute. Use `Color.Named(name)` instead.

    Note that Alpha chanel is ignored when you create a Color in a Shader.

    ``` python
    from geonodes import GeoNodes, Mesh, Layout, Color, Texture

    with GeoNodes("Color Test"):
        
        with Layout("Base"):
            a = Color()
            a = a.mix_darken(Color((1, 1, 1)))
            a = a.mix_multiply(Color(name="Defaut"))
            a = a.mix_burn((1, 0, 0), Color(name="Red"))
            a = a.mix(Color.CombineHSV(hue=.5, saturation=.5, value=.5))
            
        a.hue.out()
            
        with Layout("Named Attribute"):
            g = Mesh()
            g.points._Color = a
            
            g.points._Mixed = a.mix(Color.Named("Color"))

        with Layout("Textures"):
            c = Texture.Brick()
            c = c.mix(Texture.Checker())
            c = c.mix(Texture.Gabor())
            c = c.mix(Texture.Gradient())
            c = c.mix(Texture.Magic())
            c = c.mix(Texture.Noise())
            c = c.mix(Texture.Voronoi())
            c = c.mix(Texture.Wave())
            c = c.mix(Texture.WhiteNoise())
            
            g.edges._Textures = c
            
        g.out()
    ```
    """

    SOCKET_TYPE = 'RGBA'

    # ====================================================================================================
    # Constructors
    # ====================================================================================================

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

    def out(self, name=None, panel: str = ""):
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
            super().out(name=name, panel=panel)

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
        node = NodeCurves('RGB Curves', named_sockets={'Color': self, 'Fac': fac})
        node.set_curves(curves)
        return node._out
    
    # ====================================================================================================
    # Class test    
    # ====================================================================================================

    @classmethod
    def _class_test(cls):

        from geonodes import GeoNodes, Mesh, Layout, Color, Texture

        with GeoNodes("Color Test"):
            
            with Layout("Base"):
                a = Color()
                a = a.mix_darken(Color((1, 1, 1)))
                a = a.mix_multiply(Color(name="Defaut"))
                a = a.mix_burn((1, 0, 0), Color(name="Red"))
                a = a.mix(Color.CombineHSV(hue=.5, saturation=.5, value=.5))
                
            a.hue.out()
                
            with Layout("Named Attribute"):
                g = Mesh()
                g.points._Color = a
                
                g.points._Mixed = a.mix(Color.Named("Color"))

            with Layout("Textures"):
                c = Texture.Brick()
                c = c.mix(Texture.Checker())
                c = c.mix(Texture.Gabor())
                c = c.mix(Texture.Gradient())
                c = c.mix(Texture.Magic())
                c = c.mix(Texture.Noise())
                c = c.mix(Texture.Voronoi())
                c = c.mix(Texture.Wave())
                c = c.mix(Texture.WhiteNoise())
                
                g.edges._Textures = c
                
            g.out()


