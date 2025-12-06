# Generated 2025-12-06 09:59:03

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves, MenuNode, IndexSwitchNode
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class VolumeShader(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def Absorption(cls, color: Color = None, density: Float = None):
        """ > Node <&ShaderNode Volume Absorption>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - density (Float) : socket 'Density' (id: Density)

        Returns
        -------
        - VolumeShader
        """
        node = Node('Volume Absorption', {'Color': color, 'Density': density})
        return cls(node._out)

    @classmethod
    def info(cls):
        """ > Node <&ShaderNode Volume Info>

        Returns
        -------
        - node [color (Color), density (Float), flame (Float), temperature (Float)]
        """
        node = Node('Volume Info', )
        return node

    @classmethod
    def Principled(cls,
                    color: Color = None,
                    color_attribute: String = None,
                    density: Float = None,
                    density_attribute: String = None,
                    anisotropy: Float = None,
                    absorption_color: Color = None,
                    emission_strength: Float = None,
                    emission_color: Color = None,
                    blackbody_intensity: Float = None,
                    blackbody_tint: Color = None,
                    temperature: Float = None,
                    temperature_attribute: String = None):
        """ > Node <&ShaderNode Principled Volume>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - color_attribute (String) : socket 'Color Attribute' (id: Color Attribute)
        - density (Float) : socket 'Density' (id: Density)
        - density_attribute (String) : socket 'Density Attribute' (id: Density Attribute)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - absorption_color (Color) : socket 'Absorption Color' (id: Absorption Color)
        - emission_strength (Float) : socket 'Emission Strength' (id: Emission Strength)
        - emission_color (Color) : socket 'Emission Color' (id: Emission Color)
        - blackbody_intensity (Float) : socket 'Blackbody Intensity' (id: Blackbody Intensity)
        - blackbody_tint (Color) : socket 'Blackbody Tint' (id: Blackbody Tint)
        - temperature (Float) : socket 'Temperature' (id: Temperature)
        - temperature_attribute (String) : socket 'Temperature Attribute' (id: Temperature Attribute)

        Returns
        -------
        - VolumeShader
        """
        node = Node('Principled Volume', {'Color': color, 'Color Attribute': color_attribute, 'Density': density, 'Density Attribute': density_attribute, 'Anisotropy': anisotropy, 'Absorption Color': absorption_color, 'Emission Strength': emission_strength, 'Emission Color': emission_color, 'Blackbody Intensity': blackbody_intensity, 'Blackbody Tint': blackbody_tint, 'Temperature': temperature, 'Temperature Attribute': temperature_attribute})
        return cls(node._out)

    @classmethod
    def Scatter(cls,
                    color: Color = None,
                    density: Float = None,
                    anisotropy: Float = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN'):
        """ > Node <&ShaderNode Volume Scatter>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - density (Float) : socket 'Density' (id: Density)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - phase (str): parameter 'phase' in ['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE']

        Returns
        -------
        - VolumeShader
        """
        utils.check_enum_arg('Volume Scatter', 'phase', phase, 'Scatter', ('HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'))
        node = Node('Volume Scatter', {'Color': color, 'Density': density, 'Anisotropy': anisotropy}, phase=phase)
        return cls(node._out)

