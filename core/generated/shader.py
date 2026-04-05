# Generated 2026-04-05 12:37:59

from __future__ import annotations
from .. sockettype import SocketType
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
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Shader(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def add(self, shader: Shader = None):
        """ > Node <&ShaderNode Add Shader>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Shader | `self` |

        Parameters
        ----------
        shader : Shader, optional
            socket 'Shader' (id: Shader_001)
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        rotation : Float, optional
            socket 'Rotation' (id: Rotation)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        tangent : Vector, optional
            socket 'Tangent' (id: Tangent)
        
        distribution : Literal['Beckmann', 'GGX', 'Ashikhmin-Shirley', 'Multiscatter GGX']
            parameter `distribution`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Glossy BSDF', 'distribution', distribution, 'Glossy', ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'))
        node = Node('Glossy BSDF', {'Color': color, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent}, distribution=distribution)
        return cls(node._out)

    @classmethod
    def Diffuse(cls, color: Color = None, roughness: Float = None, normal: Vector = None):
        """ > Node <&ShaderNode Diffuse BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        thin_film_thickness : Float, optional
            socket 'Thin Film Thickness' (id: Thin Film Thickness)
        
        thin_film_ior : Float, optional
            socket 'Thin Film IOR' (id: Thin Film IOR)
        
        distribution : Literal['Beckmann', 'GGX', 'Multiscatter GGX']
            parameter `distribution`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        offset : Float, optional
            socket 'Offset' (id: Offset)
        
        roughnessu : Float, optional
            socket 'RoughnessU' (id: RoughnessU)
        
        roughnessv : Float, optional
            socket 'RoughnessV' (id: RoughnessV)
        
        tangent : Vector, optional
            socket 'Tangent' (id: Tangent)
        
        component : Literal['Reflection', 'Transmission']
            parameter `component`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        radial_roughness : Float, optional
            socket 'Radial Roughness' (id: Radial Roughness)
        
        coat : Float, optional
            socket 'Coat' (id: Coat)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        offset : Float, optional
            socket 'Offset' (id: Offset)
        
        random_roughness : Float, optional
            socket 'Random Roughness' (id: Random Roughness)
        
        random : Float, optional
            socket 'Random' (id: Random)
        
        model : Literal['Chiang', 'Huang']
            parameter `model`
        
        parametrization : Literal['Absorption Coefficient', 'Melanin Concentration', 'Direct Coloring']
            parameter `parametrization`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        base_color : Color, optional
            socket 'Base Color' (id: Base Color)
        
        edge_tint : Color, optional
            socket 'Edge Tint' (id: Edge Tint)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        rotation : Float, optional
            socket 'Rotation' (id: Rotation)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        tangent : Vector, optional
            socket 'Tangent' (id: Tangent)
        
        thin_film_thickness : Float, optional
            socket 'Thin Film Thickness' (id: Thin Film Thickness)
        
        thin_film_ior : Float, optional
            socket 'Thin Film IOR' (id: Thin Film IOR)
        
        distribution : Literal['Beckmann', 'GGX', 'Multiscatter GGX']
            parameter `distribution`
        
        fresnel_type : Literal['Physical Conductor', 'F82 Tint']
            parameter `fresnel_type`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        base_color : Color, optional
            socket 'Base Color' (id: Base Color)
        
        metallic : Float, optional
            socket 'Metallic' (id: Metallic)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        diffuse_roughness : Float, optional
            socket 'Diffuse Roughness' (id: Diffuse Roughness)
        
        subsurface_weight : Float, optional
            socket 'Subsurface Weight' (id: Subsurface Weight)
        
        subsurface_radius : Vector, optional
            socket 'Subsurface Radius' (id: Subsurface Radius)
        
        subsurface_scale : Float, optional
            socket 'Subsurface Scale' (id: Subsurface Scale)
        
        subsurface_anisotropy : Float, optional
            socket 'Subsurface Anisotropy' (id: Subsurface Anisotropy)
        
        specular_ior_level : Float, optional
            socket 'Specular IOR Level' (id: Specular IOR Level)
        
        specular_tint : Color, optional
            socket 'Specular Tint' (id: Specular Tint)
        
        anisotropic : Float, optional
            socket 'Anisotropic' (id: Anisotropic)
        
        anisotropic_rotation : Float, optional
            socket 'Anisotropic Rotation' (id: Anisotropic Rotation)
        
        tangent : Vector, optional
            socket 'Tangent' (id: Tangent)
        
        transmission_weight : Float, optional
            socket 'Transmission Weight' (id: Transmission Weight)
        
        coat_weight : Float, optional
            socket 'Coat Weight' (id: Coat Weight)
        
        coat_roughness : Float, optional
            socket 'Coat Roughness' (id: Coat Roughness)
        
        coat_ior : Float, optional
            socket 'Coat IOR' (id: Coat IOR)
        
        coat_tint : Color, optional
            socket 'Coat Tint' (id: Coat Tint)
        
        coat_normal : Vector, optional
            socket 'Coat Normal' (id: Coat Normal)
        
        sheen_weight : Float, optional
            socket 'Sheen Weight' (id: Sheen Weight)
        
        sheen_roughness : Float, optional
            socket 'Sheen Roughness' (id: Sheen Roughness)
        
        sheen_tint : Color, optional
            socket 'Sheen Tint' (id: Sheen Tint)
        
        emission_color : Color, optional
            socket 'Emission Color' (id: Emission Color)
        
        emission_strength : Float, optional
            socket 'Emission Strength' (id: Emission Strength)
        
        thin_film_thickness : Float, optional
            socket 'Thin Film Thickness' (id: Thin Film Thickness)
        
        thin_film_ior : Float, optional
            socket 'Thin Film IOR' (id: Thin Film IOR)
        
        distribution : Literal['GGX', 'Multiscatter GGX']
            parameter `distribution`
        
        subsurface_method : Literal['Christensen-Burley', 'Random Walk', 'Random Walk (Skin)']
            parameter `subsurface_method`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Principled BSDF', 'distribution', distribution, 'Principled', ('GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Principled BSDF', 'subsurface_method', subsurface_method, 'Principled', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Principled BSDF', {'Base Color': base_color, 'Metallic': metallic, 'Roughness': roughness, 'IOR': ior, 'Alpha': alpha, 'Normal': normal, 'Diffuse Roughness': diffuse_roughness, 'Subsurface Weight': subsurface_weight, 'Subsurface Radius': subsurface_radius, 'Subsurface Scale': subsurface_scale, 'Subsurface Anisotropy': subsurface_anisotropy, 'Specular IOR Level': specular_ior_level, 'Specular Tint': specular_tint, 'Anisotropic': anisotropic, 'Anisotropic Rotation': anisotropic_rotation, 'Tangent': tangent, 'Transmission Weight': transmission_weight, 'Coat Weight': coat_weight, 'Coat Roughness': coat_roughness, 'Coat IOR': coat_ior, 'Coat Tint': coat_tint, 'Coat Normal': coat_normal, 'Sheen Weight': sheen_weight, 'Sheen Roughness': sheen_roughness, 'Sheen Tint': sheen_tint, 'Emission Color': emission_color, 'Emission Strength': emission_strength, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, subsurface_method=subsurface_method)
        return cls(node._out)

    @classmethod
    def RayPortal(cls, color: Color = None, position: Vector = None, direction: Vector = None):
        """ > Node <&ShaderNode Ray Portal BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        position : Vector, optional
            socket 'Position' (id: Position)
        
        direction : Vector, optional
            socket 'Direction' (id: Direction)
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        distribution : Literal['Beckmann', 'GGX']
            parameter `distribution`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        distribution : Literal['Ashikhmin', 'Microfiber']
            parameter `distribution`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        size : Float, optional
            socket 'Size' (id: Size)
        
        smooth : Float, optional
            socket 'Smooth' (id: Smooth)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        component : Literal['Diffuse', 'Glossy']
            parameter `component`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Toon BSDF', 'component', component, 'Toon', ('DIFFUSE', 'GLOSSY'))
        node = Node('Toon BSDF', {'Color': color, 'Size': size, 'Smooth': smooth, 'Normal': normal}, component=component)
        return cls(node._out)

    @classmethod
    def Translucent(cls, color: Color = None, normal: Vector = None):
        """ > Node <&ShaderNode Translucent BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        

        Returns
        -------
        Shader
        """
        node = Node('Translucent BSDF', {'Color': color, 'Normal': normal})
        return cls(node._out)

    @classmethod
    def Transparent(cls, color: Color = None):
        """ > Node <&ShaderNode Transparent BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        base_color : Color, optional
            socket 'Base Color' (id: Base Color)
        
        specular : Color, optional
            socket 'Specular' (id: Specular)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        emissive_color : Color, optional
            socket 'Emissive Color' (id: Emissive Color)
        
        transparency : Float, optional
            socket 'Transparency' (id: Transparency)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        clear_coat : Float, optional
            socket 'Clear Coat' (id: Clear Coat)
        
        clear_coat_roughness : Float, optional
            socket 'Clear Coat Roughness' (id: Clear Coat Roughness)
        
        clear_coat_normal : Vector, optional
            socket 'Clear Coat Normal' (id: Clear Coat Normal)
        

        Returns
        -------
        Shader
        """
        node = Node('Specular BSDF', {'Base Color': base_color, 'Specular': specular, 'Roughness': roughness, 'Emissive Color': emissive_color, 'Transparency': transparency, 'Normal': normal, 'Clear Coat': clear_coat, 'Clear Coat Roughness': clear_coat_roughness, 'Clear Coat Normal': clear_coat_normal})
        return cls(node._out)

    @classmethod
    def Emission(cls, color: Color = None, strength: Float = None):
        """ > Node <&ShaderNode Emission>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        strength : Float, optional
            socket 'Strength' (id: Strength)
        

        Returns
        -------
        Shader
        """
        node = Node('Emission', {'Color': color, 'Strength': strength})
        return cls(node._out)

    @classmethod
    def Holdout(cls):
        """ > Node <&ShaderNode Holdout>

        Returns
        -------
        Shader
        """
        node = Node('Holdout', )
        return cls(node._out)

    def mix(self, shader: Shader = None, factor: Float = None):
        """ > Node <&ShaderNode Mix Shader>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Shader | `self` |

        Parameters
        ----------
        shader : Shader, optional
            socket 'Shader' (id: Shader_001)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Shader
        """
        node = Node('Mix Shader', {'Shader': self, 'Shader_001': shader, 'Fac': factor})
        return node._out

    def light_output(self,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode Light Output>

        **Fixed values**

        | Kind   | Name    | Value  |
        | ------ | ------- | ------ |
        | Socket | Surface | `self` |

        Parameters
        ----------
        is_active_output : bool
            parameter `is_active_output`
        
        target : Literal['All', 'EEVEE', 'Cycles']
            parameter `target`
        

        Returns
        -------
        None
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

        **Fixed values**

        | Kind   | Name    | Value  |
        | ------ | ------- | ------ |
        | Socket | Surface | `self` |

        Parameters
        ----------
        volume : VolumeShader, optional
            socket 'Volume' (id: Volume)
        
        displacement : Vector, optional
            socket 'Displacement' (id: Displacement)
        
        thickness : Float, optional
            socket 'Thickness' (id: Thickness)
        
        is_active_output : bool
            parameter `is_active_output`
        
        target : Literal['All', 'EEVEE', 'Cycles']
            parameter `target`
        

        Returns
        -------
        None
        """
        utils.check_enum_arg('Material Output', 'target', target, 'material_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Material Output', {'Surface': self, 'Volume': volume, 'Displacement': displacement, 'Thickness': thickness}, is_active_output=is_active_output, target=target)
        return node._out

    def world_output(self,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode World Output>

        **Fixed values**

        | Kind   | Name    | Value  |
        | ------ | ------- | ------ |
        | Socket | Surface | `self` |

        Parameters
        ----------
        volume : VolumeShader, optional
            socket 'Volume' (id: Volume)
        
        is_active_output : bool
            parameter `is_active_output`
        
        target : Literal['All', 'EEVEE', 'Cycles']
            parameter `target`
        

        Returns
        -------
        None
        """
        utils.check_enum_arg('World Output', 'target', target, 'world_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('World Output', {'Surface': self, 'Volume': volume}, is_active_output=is_active_output, target=target)
        return node._out

    def to_rgb(self):
        """ > Node <&ShaderNode Shader to RGB>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Shader | `self` |

        Returns
        -------
        Color
            peer sockets: alpha_ (Float)

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

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        radius : Vector, optional
            socket 'Radius' (id: Radius)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        falloff : Literal['Christensen-Burley', 'Random Walk', 'Random Walk (Skin)']
            parameter `falloff`
        

        Returns
        -------
        Shader
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

        Parameters
        ----------
        name : str, default=`Shader`
            Input socket name

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier


        Returns
        -------
        Shader
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketShader', name=name, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier)

