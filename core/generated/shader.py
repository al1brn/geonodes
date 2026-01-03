# Generated 2026-01-02 09:45:11

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
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


class Shader(Socket):
    """"
    $DOC SET hidden
    """
    def add(self, shader: Shader = None):
        """ > Node <&ShaderNode Add Shader>

        Information
        -----------
        - Socket 'Shader' : self

        Arguments
        ---------
        - shader (Shader) : socket 'Shader' (id: Shader_001)

        Returns
        -------
        - Shader
        """
        node = Node('Add Shader', {'Shader': self, 'Shader_001': shader})
        return node._out

    @classmethod
    def Glossy(cls,
                    color: Color = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    distribution: Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'] = 'MULTI_GGX'):
        """ > Node <&ShaderNode Glossy BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - rotation (Float) : socket 'Rotation' (id: Rotation)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Glossy BSDF', 'distribution', distribution, 'Glossy', ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'))
        node = Node('Glossy BSDF', {'Color': color, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent}, distribution=distribution)
        return cls(node._out)

    @classmethod
    def Diffuse(cls, color: Color = None, roughness: Float = None, normal: Vector = None):
        """ > Node <&ShaderNode Diffuse BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Shader
        """
        node = Node('Diffuse BSDF', {'Color': color, 'Roughness': roughness, 'Normal': normal})
        return cls(node._out)

    @classmethod
    def Glass(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX'):
        """ > Node <&ShaderNode Glass BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - thin_film_thickness (Float) : socket 'Thin Film Thickness' (id: Thin Film Thickness)
        - thin_film_ior (Float) : socket 'Thin Film IOR' (id: Thin Film IOR)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX', 'MULTI_GGX']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Glass BSDF', 'distribution', distribution, 'Glass', ('BECKMANN', 'GGX', 'MULTI_GGX'))
        node = Node('Glass BSDF', {'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution)
        return cls(node._out)

    @classmethod
    def Hair(cls,
                    color: Color = None,
                    offset: Float = None,
                    roughnessu: Float = None,
                    roughnessv: Float = None,
                    tangent: Vector = None,
                    component: Literal['Reflection', 'Transmission'] = 'Reflection'):
        """ > Node <&ShaderNode Hair BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - offset (Float) : socket 'Offset' (id: Offset)
        - roughnessu (Float) : socket 'RoughnessU' (id: RoughnessU)
        - roughnessv (Float) : socket 'RoughnessV' (id: RoughnessV)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - component (str): parameter 'component' in ['Reflection', 'Transmission']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Hair BSDF', 'component', component, 'Hair', ('Reflection', 'Transmission'))
        node = Node('Hair BSDF', {'Color': color, 'Offset': offset, 'RoughnessU': roughnessu, 'RoughnessV': roughnessv, 'Tangent': tangent}, component=component)
        return cls(node._out)

    @classmethod
    def PrincipledHair(cls,
                    color: Color = None,
                    roughness: Float = None,
                    radial_roughness: Float = None,
                    coat: Float = None,
                    ior: Float = None,
                    offset: Float = None,
                    random_roughness: Float = None,
                    random: Float = None,
                    model: Literal['CHIANG', 'HUANG'] = 'CHIANG',
                    parametrization: Literal['ABSORPTION', 'MELANIN', 'COLOR'] = 'COLOR'):
        """ > Node <&ShaderNode Principled Hair BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - radial_roughness (Float) : socket 'Radial Roughness' (id: Radial Roughness)
        - coat (Float) : socket 'Coat' (id: Coat)
        - ior (Float) : socket 'IOR' (id: IOR)
        - offset (Float) : socket 'Offset' (id: Offset)
        - random_roughness (Float) : socket 'Random Roughness' (id: Random Roughness)
        - random (Float) : socket 'Random' (id: Random)
        - model (str): parameter 'model' in ['CHIANG', 'HUANG']
        - parametrization (str): parameter 'parametrization' in ['ABSORPTION', 'MELANIN', 'COLOR']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Principled Hair BSDF', 'model', model, 'PrincipledHair', ('CHIANG', 'HUANG'))
        utils.check_enum_arg('Principled Hair BSDF', 'parametrization', parametrization, 'PrincipledHair', ('ABSORPTION', 'MELANIN', 'COLOR'))
        node = Node('Principled Hair BSDF', {'Color': color, 'Roughness': roughness, 'Radial Roughness': radial_roughness, 'Coat': coat, 'IOR': ior, 'Offset': offset, 'Random Roughness': random_roughness, 'Random': random}, model=model, parametrization=parametrization)
        return cls(node._out)

    @classmethod
    def Metallic(cls,
                    base_color: Color = None,
                    edge_tint: Color = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX',
                    fresnel_type: Literal['PHYSICAL_CONDUCTOR', 'F82'] = 'F82'):
        """ > Node <&ShaderNode Metallic BSDF>

        Arguments
        ---------
        - base_color (Color) : socket 'Base Color' (id: Base Color)
        - edge_tint (Color) : socket 'Edge Tint' (id: Edge Tint)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - rotation (Float) : socket 'Rotation' (id: Rotation)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - thin_film_thickness (Float) : socket 'Thin Film Thickness' (id: Thin Film Thickness)
        - thin_film_ior (Float) : socket 'Thin Film IOR' (id: Thin Film IOR)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX', 'MULTI_GGX']
        - fresnel_type (str): parameter 'fresnel_type' in ['PHYSICAL_CONDUCTOR', 'F82']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Metallic BSDF', 'distribution', distribution, 'Metallic', ('BECKMANN', 'GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Metallic BSDF', 'fresnel_type', fresnel_type, 'Metallic', ('PHYSICAL_CONDUCTOR', 'F82'))
        node = Node('Metallic BSDF', {'Base Color': base_color, 'Edge Tint': edge_tint, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, fresnel_type=fresnel_type)
        return cls(node._out)

    @classmethod
    def Principled(cls,
                    base_color: Color = None,
                    metallic: Float = None,
                    roughness: Float = None,
                    ior: Float = None,
                    alpha: Float = None,
                    normal: Vector = None,
                    diffuse_roughness: Float = None,
                    subsurface_weight: Float = None,
                    subsurface_radius: Vector = None,
                    subsurface_scale: Float = None,
                    subsurface_anisotropy: Float = None,
                    specular_ior_level: Float = None,
                    specular_tint: Color = None,
                    anisotropic: Float = None,
                    anisotropic_rotation: Float = None,
                    tangent: Vector = None,
                    transmission_weight: Float = None,
                    coat_weight: Float = None,
                    coat_roughness: Float = None,
                    coat_ior: Float = None,
                    coat_tint: Color = None,
                    coat_normal: Vector = None,
                    sheen_weight: Float = None,
                    sheen_roughness: Float = None,
                    sheen_tint: Color = None,
                    emission_color: Color = None,
                    emission_strength: Float = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['GGX', 'MULTI_GGX'] = 'MULTI_GGX',
                    subsurface_method: Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'] = 'RANDOM_WALK'):
        """ > Node <&ShaderNode Principled BSDF>

        Arguments
        ---------
        - base_color (Color) : socket 'Base Color' (id: Base Color)
        - metallic (Float) : socket 'Metallic' (id: Metallic)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - alpha (Float) : socket 'Alpha' (id: Alpha)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - diffuse_roughness (Float) : socket 'Diffuse Roughness' (id: Diffuse Roughness)
        - subsurface_weight (Float) : socket 'Subsurface Weight' (id: Subsurface Weight)
        - subsurface_radius (Vector) : socket 'Subsurface Radius' (id: Subsurface Radius)
        - subsurface_scale (Float) : socket 'Subsurface Scale' (id: Subsurface Scale)
        - subsurface_anisotropy (Float) : socket 'Subsurface Anisotropy' (id: Subsurface Anisotropy)
        - specular_ior_level (Float) : socket 'Specular IOR Level' (id: Specular IOR Level)
        - specular_tint (Color) : socket 'Specular Tint' (id: Specular Tint)
        - anisotropic (Float) : socket 'Anisotropic' (id: Anisotropic)
        - anisotropic_rotation (Float) : socket 'Anisotropic Rotation' (id: Anisotropic Rotation)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - transmission_weight (Float) : socket 'Transmission Weight' (id: Transmission Weight)
        - coat_weight (Float) : socket 'Coat Weight' (id: Coat Weight)
        - coat_roughness (Float) : socket 'Coat Roughness' (id: Coat Roughness)
        - coat_ior (Float) : socket 'Coat IOR' (id: Coat IOR)
        - coat_tint (Color) : socket 'Coat Tint' (id: Coat Tint)
        - coat_normal (Vector) : socket 'Coat Normal' (id: Coat Normal)
        - sheen_weight (Float) : socket 'Sheen Weight' (id: Sheen Weight)
        - sheen_roughness (Float) : socket 'Sheen Roughness' (id: Sheen Roughness)
        - sheen_tint (Color) : socket 'Sheen Tint' (id: Sheen Tint)
        - emission_color (Color) : socket 'Emission Color' (id: Emission Color)
        - emission_strength (Float) : socket 'Emission Strength' (id: Emission Strength)
        - thin_film_thickness (Float) : socket 'Thin Film Thickness' (id: Thin Film Thickness)
        - thin_film_ior (Float) : socket 'Thin Film IOR' (id: Thin Film IOR)
        - distribution (str): parameter 'distribution' in ['GGX', 'MULTI_GGX']
        - subsurface_method (str): parameter 'subsurface_method' in ['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Principled BSDF', 'distribution', distribution, 'Principled', ('GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Principled BSDF', 'subsurface_method', subsurface_method, 'Principled', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Principled BSDF', {'Base Color': base_color, 'Metallic': metallic, 'Roughness': roughness, 'IOR': ior, 'Alpha': alpha, 'Normal': normal, 'Diffuse Roughness': diffuse_roughness, 'Subsurface Weight': subsurface_weight, 'Subsurface Radius': subsurface_radius, 'Subsurface Scale': subsurface_scale, 'Subsurface Anisotropy': subsurface_anisotropy, 'Specular IOR Level': specular_ior_level, 'Specular Tint': specular_tint, 'Anisotropic': anisotropic, 'Anisotropic Rotation': anisotropic_rotation, 'Tangent': tangent, 'Transmission Weight': transmission_weight, 'Coat Weight': coat_weight, 'Coat Roughness': coat_roughness, 'Coat IOR': coat_ior, 'Coat Tint': coat_tint, 'Coat Normal': coat_normal, 'Sheen Weight': sheen_weight, 'Sheen Roughness': sheen_roughness, 'Sheen Tint': sheen_tint, 'Emission Color': emission_color, 'Emission Strength': emission_strength, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, subsurface_method=subsurface_method)
        return cls(node._out)

    @classmethod
    def RayPortal(cls, color: Color = None, position: Vector = None, direction: Vector = None):
        """ > Node <&ShaderNode Ray Portal BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - position (Vector) : socket 'Position' (id: Position)
        - direction (Vector) : socket 'Direction' (id: Direction)

        Returns
        -------
        - Shader
        """
        node = Node('Ray Portal BSDF', {'Color': color, 'Position': position, 'Direction': direction})
        return cls(node._out)

    @classmethod
    def Refraction(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    distribution: Literal['BECKMANN', 'GGX'] = 'BECKMANN'):
        """ > Node <&ShaderNode Refraction BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Refraction BSDF', 'distribution', distribution, 'Refraction', ('BECKMANN', 'GGX'))
        node = Node('Refraction BSDF', {'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal}, distribution=distribution)
        return cls(node._out)

    @classmethod
    def Sheen(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    distribution: Literal['ASHIKHMIN', 'MICROFIBER'] = 'MICROFIBER'):
        """ > Node <&ShaderNode Sheen BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - distribution (str): parameter 'distribution' in ['ASHIKHMIN', 'MICROFIBER']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Sheen BSDF', 'distribution', distribution, 'Sheen', ('ASHIKHMIN', 'MICROFIBER'))
        node = Node('Sheen BSDF', {'Color': color, 'Roughness': roughness, 'Normal': normal}, distribution=distribution)
        return cls(node._out)

    @classmethod
    def Toon(cls,
                    color: Color = None,
                    size: Float = None,
                    smooth: Float = None,
                    normal: Vector = None,
                    component: Literal['DIFFUSE', 'GLOSSY'] = 'DIFFUSE'):
        """ > Node <&ShaderNode Toon BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - size (Float) : socket 'Size' (id: Size)
        - smooth (Float) : socket 'Smooth' (id: Smooth)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - component (str): parameter 'component' in ['DIFFUSE', 'GLOSSY']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Toon BSDF', 'component', component, 'Toon', ('DIFFUSE', 'GLOSSY'))
        node = Node('Toon BSDF', {'Color': color, 'Size': size, 'Smooth': smooth, 'Normal': normal}, component=component)
        return cls(node._out)

    @classmethod
    def Translucent(cls, color: Color = None, normal: Vector = None):
        """ > Node <&ShaderNode Translucent BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Shader
        """
        node = Node('Translucent BSDF', {'Color': color, 'Normal': normal})
        return cls(node._out)

    @classmethod
    def Transparent(cls, color: Color = None):
        """ > Node <&ShaderNode Transparent BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)

        Returns
        -------
        - Shader
        """
        node = Node('Transparent BSDF', {'Color': color})
        return cls(node._out)

    @classmethod
    def Specular(cls,
                    base_color: Color = None,
                    specular: Color = None,
                    roughness: Float = None,
                    emissive_color: Color = None,
                    transparency: Float = None,
                    normal: Vector = None,
                    clear_coat: Float = None,
                    clear_coat_roughness: Float = None,
                    clear_coat_normal: Vector = None):
        """ > Node <&ShaderNode Specular BSDF>

        Arguments
        ---------
        - base_color (Color) : socket 'Base Color' (id: Base Color)
        - specular (Color) : socket 'Specular' (id: Specular)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - emissive_color (Color) : socket 'Emissive Color' (id: Emissive Color)
        - transparency (Float) : socket 'Transparency' (id: Transparency)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - clear_coat (Float) : socket 'Clear Coat' (id: Clear Coat)
        - clear_coat_roughness (Float) : socket 'Clear Coat Roughness' (id: Clear Coat Roughness)
        - clear_coat_normal (Vector) : socket 'Clear Coat Normal' (id: Clear Coat Normal)

        Returns
        -------
        - Shader
        """
        node = Node('Specular BSDF', {'Base Color': base_color, 'Specular': specular, 'Roughness': roughness, 'Emissive Color': emissive_color, 'Transparency': transparency, 'Normal': normal, 'Clear Coat': clear_coat, 'Clear Coat Roughness': clear_coat_roughness, 'Clear Coat Normal': clear_coat_normal})
        return cls(node._out)

    @classmethod
    def Emission(cls, color: Color = None, strength: Float = None):
        """ > Node <&ShaderNode Emission>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - strength (Float) : socket 'Strength' (id: Strength)

        Returns
        -------
        - Shader
        """
        node = Node('Emission', {'Color': color, 'Strength': strength})
        return cls(node._out)

    @classmethod
    def Holdout(cls):
        """ > Node <&ShaderNode Holdout>

        Returns
        -------
        - Shader
        """
        node = Node('Holdout', )
        return cls(node._out)

    def mix(self, shader: Shader = None, factor: Float = None):
        """ > Node <&ShaderNode Mix Shader>

        Information
        -----------
        - Socket 'Shader' : self

        Arguments
        ---------
        - shader (Shader) : socket 'Shader' (id: Shader_001)
        - factor (Float) : socket 'Factor' (id: Fac)

        Returns
        -------
        - Shader
        """
        node = Node('Mix Shader', {'Shader': self, 'Shader_001': shader, 'Fac': factor})
        return node._out

    def light_output(self,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode Light Output>

        Information
        -----------
        - Socket 'Surface' : self

        Arguments
        ---------
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Light Output', 'target', target, 'light_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Light Output', {'Surface': self}, is_active_output=is_active_output, target=target)
        return node._out

    def material_output(self,
                    volume: VolumeShader = None,
                    displacement: Vector = None,
                    thickness: Float = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode Material Output>

        Information
        -----------
        - Socket 'Surface' : self

        Arguments
        ---------
        - volume (VolumeShader) : socket 'Volume' (id: Volume)
        - displacement (Vector) : socket 'Displacement' (id: Displacement)
        - thickness (Float) : socket 'Thickness' (id: Thickness)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Material Output', 'target', target, 'material_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Material Output', {'Surface': self, 'Volume': volume, 'Displacement': displacement, 'Thickness': thickness}, is_active_output=is_active_output, target=target)
        return node._out

    def world_output(self,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode World Output>

        Information
        -----------
        - Socket 'Surface' : self

        Arguments
        ---------
        - volume (VolumeShader) : socket 'Volume' (id: Volume)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('World Output', 'target', target, 'world_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('World Output', {'Surface': self, 'Volume': volume}, is_active_output=is_active_output, target=target)
        return node._out

    def to_rgb(self):
        """ > Node <&ShaderNode Shader to RGB>

        Information
        -----------
        - Socket 'Shader' : self

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        node = Node('Shader to RGB', {'Shader': self})
        return node._out

    @classmethod
    def SubsurfaceScattering(cls,
                    color: Color = None,
                    scale: Float = None,
                    radius: Vector = None,
                    ior: Float = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    normal: Vector = None,
                    falloff: Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'] = 'RANDOM_WALK'):
        """ > Node <&ShaderNode Subsurface Scattering>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - scale (Float) : socket 'Scale' (id: Scale)
        - radius (Vector) : socket 'Radius' (id: Radius)
        - ior (Float) : socket 'IOR' (id: IOR)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - falloff (str): parameter 'falloff' in ['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Subsurface Scattering', 'falloff', falloff, 'SubsurfaceScattering', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Subsurface Scattering', {'Color': color, 'Scale': scale, 'Radius': radius, 'IOR': ior, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Normal': normal}, falloff=falloff)
        return cls(node._out)

    @classmethod
    def _create_input_socket(cls,
        name: str = 'Shader',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Shader Input

        New <#Shader> input with subtype 'NONE'.

        Aguments
        --------
        - name  (str = 'Shader') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier

        Returns
        -------
        - Shader
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketShader', name=name, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier)

