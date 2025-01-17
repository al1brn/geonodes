from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class VolumeShader(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def Absorption(cls, color=None, density=None):
        """ > Node <&ShaderNode Volume Absorption>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - density (Float) : socket 'Density' (id: Density)

        Returns
        -------
        - VolumeShader
        """
        node = Node('Volume Absorption', sockets={'Color': color, 'Density': density})
        return cls(node._out)

    @classmethod
    def info(cls):
        """ > Node <&ShaderNode Volume Info>

        Returns
        -------
        - node [color (Color), density (Float), flame (Float), temperature (Float)]
        """
        node = Node('Volume Info', sockets={})
        return node

    @classmethod
    def Principled(cls, color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None):
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
        node = Node('Principled Volume', sockets={'Color': color, 'Color Attribute': color_attribute, 'Density': density, 'Density Attribute': density_attribute, 'Anisotropy': anisotropy, 'Absorption Color': absorption_color, 'Emission Strength': emission_strength, 'Emission Color': emission_color, 'Blackbody Intensity': blackbody_intensity, 'Blackbody Tint': blackbody_tint, 'Temperature': temperature, 'Temperature Attribute': temperature_attribute})
        return cls(node._out)

    @classmethod
    def Scatter(cls, color=None, density=None, anisotropy=None, phase='HENYEY_GREENSTEIN'):
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
        node = Node('Volume Scatter', sockets={'Color': color, 'Density': density, 'Anisotropy': anisotropy}, phase=phase)
        return cls(node._out)

