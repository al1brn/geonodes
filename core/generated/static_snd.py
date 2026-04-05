# Generated 2026-04-05 13:12:12

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


class SND:
    """" Static class

    Exposes all nodes as static methods:

    ``` python
    a = snd.math(1, 2, operation='ADD')
    ```
    """

    @classmethod
    def menu_switch(cls,
                    named_sockets: dict = {},
                    menu = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'MENU', 'SHADER', 'BUNDLE', 'CLOSURE'] = 'RGBA',
                    **sockets):
        """ > Node <&ShaderNode Menu Switch>

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        menu : Menu, optional
            Menu selection
        
        data_type : Literal['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'Menu', 'Shader', 'Bundle', 'Closure']
            parameter `data_type`
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        Color
            peer sockets: a_ (Boolean), b_ (Boolean)

        """
        node = Node('Menu Switch', {'Menu': menu, **named_sockets}, data_type=data_type, **sockets)
        return node._out

    @classmethod
    def repeat_input(cls, iterations: Integer = None):
        """ > Node <&ShaderNode Repeat Input>

        Parameters
        ----------
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        

        Returns
        -------
        Integer
        """
        node = Node('Repeat Input', {'Iterations': iterations})
        return node._out

    @classmethod
    def repeat_output(cls, inspection_index = 0):
        """ > Node <&ShaderNode Repeat Output>

        Parameters
        ----------
        inspection_index : int
            parameter `inspection_index`
        

        Returns
        -------
        None
        """
        node = Node('Repeat Output', inspection_index=inspection_index)
        return node._out

    @utils.classproperty
    def closure_input(self):
        """ > Node <&ShaderNode Closure Input>

        Returns
        -------
        None
        """
        node = Node('Closure Input', )
        return node._out

    @classmethod
    def closure_output(cls, active_input_index = 0, active_output_index = 0, define_signature = False):
        """ > Node <&ShaderNode Closure Output>

        Parameters
        ----------
        active_input_index : int
            parameter `active_input_index`
        
        active_output_index : int
            parameter `active_output_index`
        
        define_signature : bool
            parameter `define_signature`
        

        Returns
        -------
        Closure
        """
        node = Node('Closure Output', active_input_index=active_input_index, active_output_index=active_output_index, define_signature=define_signature)
        return node._out

    @classmethod
    def combine_bundle(cls, named_sockets: dict = {}, define_signature = False, **sockets):
        """ > Node <&ShaderNode Combine Bundle>

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        define_signature : bool
            parameter `define_signature`
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        Bundle
        """
        node = Node('Combine Bundle', named_sockets, define_signature=define_signature, **sockets)
        return node._out

    @classmethod
    def evaluate_closure(cls,
                    closure: Closure = None,
                    active_input_index = 0,
                    active_output_index = 0,
                    define_signature = False):
        """ > Node <&ShaderNode Evaluate Closure>

        Parameters
        ----------
        closure : Closure, optional
            socket 'Closure' (id: Closure)
        
        active_input_index : int
            parameter `active_input_index`
        
        active_output_index : int
            parameter `active_output_index`
        
        define_signature : bool
            parameter `define_signature`
        

        Returns
        -------
        None
        """
        node = Node('Evaluate Closure', {'Closure': closure}, active_input_index=active_input_index, active_output_index=active_output_index, define_signature=define_signature)
        return node._out

    @classmethod
    def frame(cls, label_size = 20, shrink = True, text = None):
        """ > Node <&ShaderNode Frame>

        Parameters
        ----------
        label_size : int
            parameter `label_size`
        
        shrink : bool
            parameter `shrink`
        
        text : NoneType
            parameter `text`
        

        Returns
        -------
        None
        """
        node = Node('Frame', label_size=label_size, shrink=shrink, text=text)
        return node._out

    @utils.classproperty
    def group_input(self):
        """ > Node <&ShaderNode Group Input>

        Returns
        -------
        None
        """
        node = Node('Group Input', )
        return node._out

    @classmethod
    def group_output(cls, is_active_output = True):
        """ > Node <&ShaderNode Group Output>

        Parameters
        ----------
        is_active_output : bool
            parameter `is_active_output`
        

        Returns
        -------
        None
        """
        node = Node('Group Output', is_active_output=is_active_output)
        return node._out

    @classmethod
    def join_bundle(cls, *bundle: Bundle):
        """ > Node <&ShaderNode Join Bundle>

        Parameters
        ----------
        bundle : Bundle, optional
            socket 'Bundle' (id: Bundle)
        

        Returns
        -------
        Bundle
        """
        node = Node('Join Bundle', {'Bundle': list(bundle)})
        return node._out

    @classmethod
    def reroute(cls, input: Color = None, socket_idname = 'NodeSocketColor'):
        """ > Node <&ShaderNode Reroute>

        Parameters
        ----------
        input : Color, optional
            socket 'Input' (id: Input)
        
        socket_idname : str
            parameter `socket_idname`
        

        Returns
        -------
        Color
        """
        node = Node('Reroute', {'Input': input}, socket_idname=socket_idname)
        return node._out

    @classmethod
    def separate_bundle(cls,
                    named_sockets: dict = {},
                    bundle: Bundle = None,
                    define_signature = False,
                    **sockets):
        """ > Node <&ShaderNode Separate Bundle>

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        bundle : Bundle, optional
            socket 'Bundle' (id: Bundle)
        
        define_signature : bool
            parameter `define_signature`
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        None
        """
        node = Node('Separate Bundle', {'Bundle': bundle, **named_sockets}, define_signature=define_signature, **sockets)
        return node

    @classmethod
    def add_shader(cls, shader: Shader = None, shader_1: Shader = None):
        """ > Node <&ShaderNode Add Shader>

        Parameters
        ----------
        shader : Shader, optional
            socket 'Shader' (id: Shader)
        
        shader_1 : Shader, optional
            socket 'Shader' (id: Shader_001)
        

        Returns
        -------
        Shader
        """
        node = Node('Add Shader', {'Shader': shader, 'Shader_001': shader_1})
        return node._out

    @classmethod
    def ambient_occlusion(cls,
                    color: Color = None,
                    distance: Float = None,
                    normal: Vector = None,
                    inside = False,
                    only_local = False,
                    samples = 16):
        """ > Node <&ShaderNode Ambient Occlusion>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        distance : Float, optional
            socket 'Distance' (id: Distance)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        inside : bool
            parameter `inside`
        
        only_local : bool
            parameter `only_local`
        
        samples : int
            parameter `samples`
        

        Returns
        -------
        Color
            peer sockets: ao_ (Float)

        """
        node = Node('Ambient Occlusion', {'Color': color, 'Distance': distance, 'Normal': normal}, inside=inside, only_local=only_local, samples=samples)
        return node._out

    @classmethod
    def attribute(cls,
                    attribute_name = '',
                    attribute_type: Literal['GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER'] = 'GEOMETRY'):
        """ > Node <&ShaderNode Attribute>

        Parameters
        ----------
        attribute_name : str
            parameter `attribute_name`
        
        attribute_type : Literal['Geometry', 'Object', 'Instancer', 'View Layer']
            parameter `attribute_type`
        

        Returns
        -------
        Color
            peer sockets: vector_ (Vector), factor_ (Float), alpha_ (Float)

        """
        utils.check_enum_arg('Attribute', 'attribute_type', attribute_type, 'attribute', ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER'))
        node = Node('Attribute', attribute_name=attribute_name, attribute_type=attribute_type)
        return node

    @classmethod
    def background(cls, color: Color = None, strength: Float = None, weight: Float = None):
        """ > Node <&ShaderNode Background>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Background', {'Color': color, 'Strength': strength, 'Weight': weight})
        return node._out

    @classmethod
    def bevel(cls, radius: Float = None, normal: Vector = None, samples = 4):
        """ > Node <&ShaderNode Bevel>

        Parameters
        ----------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        samples : int
            parameter `samples`
        

        Returns
        -------
        Vector
        """
        node = Node('Bevel', {'Radius': radius, 'Normal': normal}, samples=samples)
        return node._out

    @classmethod
    def blackbody(cls, temperature: Float = None):
        """ > Node <&ShaderNode Blackbody>

        Parameters
        ----------
        temperature : Float, optional
            socket 'Temperature' (id: Temperature)
        

        Returns
        -------
        Color
        """
        node = Node('Blackbody', {'Temperature': temperature})
        return node._out

    @classmethod
    def brightness_contrast(cls, color: Color = None, brightness: Float = None, contrast: Float = None):
        """ > Node <&ShaderNode Brightness/Contrast>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        brightness : Float, optional
            socket 'Brightness' (id: Bright)
        
        contrast : Float, optional
            socket 'Contrast' (id: Contrast)
        

        Returns
        -------
        Color
        """
        node = Node('Brightness/Contrast', {'Color': color, 'Bright': brightness, 'Contrast': contrast})
        return node._out

    @classmethod
    def glossy_bsdf(cls,
                    color: Color = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        distribution : Literal['Beckmann', 'GGX', 'Ashikhmin-Shirley', 'Multiscatter GGX']
            parameter `distribution`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Glossy BSDF', 'distribution', distribution, 'glossy_bsdf', ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'))
        node = Node('Glossy BSDF', {'Color': color, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def diffuse_bsdf(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    weight: Float = None):
        """ > Node <&ShaderNode Diffuse BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Diffuse BSDF', {'Color': color, 'Roughness': roughness, 'Normal': normal, 'Weight': weight})
        return node._out

    @classmethod
    def glass_bsdf(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
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
        utils.check_enum_arg('Glass BSDF', 'distribution', distribution, 'glass_bsdf', ('BECKMANN', 'GGX', 'MULTI_GGX'))
        node = Node('Glass BSDF', {'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal, 'Weight': weight, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution)
        return node._out

    @classmethod
    def hair_bsdf(cls,
                    color: Color = None,
                    offset: Float = None,
                    roughnessu: Float = None,
                    roughnessv: Float = None,
                    tangent: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        component : Literal['Reflection', 'Transmission']
            parameter `component`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Hair BSDF', 'component', component, 'hair_bsdf', ('Reflection', 'Transmission'))
        node = Node('Hair BSDF', {'Color': color, 'Offset': offset, 'RoughnessU': roughnessu, 'RoughnessV': roughnessv, 'Tangent': tangent, 'Weight': weight}, component=component)
        return node._out

    @classmethod
    def principled_hair_bsdf(cls,
                    color: Color = None,
                    melanin: Float = None,
                    melanin_redness: Float = None,
                    tint: Color = None,
                    absorption_coefficient: Vector = None,
                    aspect_ratio: Float = None,
                    roughness: Float = None,
                    radial_roughness: Float = None,
                    coat: Float = None,
                    ior: Float = None,
                    offset: Float = None,
                    random_color: Float = None,
                    random_roughness: Float = None,
                    random: Float = None,
                    weight: Float = None,
                    reflection: Float = None,
                    transmission: Float = None,
                    secondary_reflection: Float = None,
                    model: Literal['CHIANG', 'HUANG'] = 'CHIANG',
                    parametrization: Literal['ABSORPTION', 'MELANIN', 'COLOR'] = 'COLOR'):
        """ > Node <&ShaderNode Principled Hair BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        melanin : Float, optional
            socket 'Melanin' (id: Melanin)
        
        melanin_redness : Float, optional
            socket 'Melanin Redness' (id: Melanin Redness)
        
        tint : Color, optional
            socket 'Tint' (id: Tint)
        
        absorption_coefficient : Vector, optional
            socket 'Absorption Coefficient' (id: Absorption Coefficient)
        
        aspect_ratio : Float, optional
            socket 'Aspect Ratio' (id: Aspect Ratio)
        
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
        
        random_color : Float, optional
            socket 'Random Color' (id: Random Color)
        
        random_roughness : Float, optional
            socket 'Random Roughness' (id: Random Roughness)
        
        random : Float, optional
            socket 'Random' (id: Random)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        reflection : Float, optional
            socket 'Reflection' (id: R lobe)
        
        transmission : Float, optional
            socket 'Transmission' (id: TT lobe)
        
        secondary_reflection : Float, optional
            socket 'Secondary Reflection' (id: TRT lobe)
        
        model : Literal['Chiang', 'Huang']
            parameter `model`
        
        parametrization : Literal['Absorption Coefficient', 'Melanin Concentration', 'Direct Coloring']
            parameter `parametrization`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Principled Hair BSDF', 'model', model, 'principled_hair_bsdf', ('CHIANG', 'HUANG'))
        utils.check_enum_arg('Principled Hair BSDF', 'parametrization', parametrization, 'principled_hair_bsdf', ('ABSORPTION', 'MELANIN', 'COLOR'))
        node = Node('Principled Hair BSDF', {'Color': color, 'Melanin': melanin, 'Melanin Redness': melanin_redness, 'Tint': tint, 'Absorption Coefficient': absorption_coefficient, 'Aspect Ratio': aspect_ratio, 'Roughness': roughness, 'Radial Roughness': radial_roughness, 'Coat': coat, 'IOR': ior, 'Offset': offset, 'Random Color': random_color, 'Random Roughness': random_roughness, 'Random': random, 'Weight': weight, 'R lobe': reflection, 'TT lobe': transmission, 'TRT lobe': secondary_reflection}, model=model, parametrization=parametrization)
        return node._out

    @classmethod
    def metallic_bsdf(cls,
                    base_color: Color = None,
                    edge_tint: Color = None,
                    ior: Vector = None,
                    extinction: Vector = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    weight: Float = None,
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
        
        ior : Vector, optional
            socket 'IOR' (id: IOR)
        
        extinction : Vector, optional
            socket 'Extinction' (id: Extinction)
        
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
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
        utils.check_enum_arg('Metallic BSDF', 'distribution', distribution, 'metallic_bsdf', ('BECKMANN', 'GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Metallic BSDF', 'fresnel_type', fresnel_type, 'metallic_bsdf', ('PHYSICAL_CONDUCTOR', 'F82'))
        node = Node('Metallic BSDF', {'Base Color': base_color, 'Edge Tint': edge_tint, 'IOR': ior, 'Extinction': extinction, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent, 'Weight': weight, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, fresnel_type=fresnel_type)
        return node._out

    @classmethod
    def principled_bsdf(cls,
                    base_color: Color = None,
                    metallic: Float = None,
                    roughness: Float = None,
                    ior: Float = None,
                    alpha: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    diffuse_roughness: Float = None,
                    subsurface_weight: Float = None,
                    subsurface_radius: Vector = None,
                    subsurface_scale: Float = None,
                    subsurface_ior: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        diffuse_roughness : Float, optional
            socket 'Diffuse Roughness' (id: Diffuse Roughness)
        
        subsurface_weight : Float, optional
            socket 'Subsurface Weight' (id: Subsurface Weight)
        
        subsurface_radius : Vector, optional
            socket 'Subsurface Radius' (id: Subsurface Radius)
        
        subsurface_scale : Float, optional
            socket 'Subsurface Scale' (id: Subsurface Scale)
        
        subsurface_ior : Float, optional
            socket 'Subsurface IOR' (id: Subsurface IOR)
        
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
        utils.check_enum_arg('Principled BSDF', 'distribution', distribution, 'principled_bsdf', ('GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Principled BSDF', 'subsurface_method', subsurface_method, 'principled_bsdf', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Principled BSDF', {'Base Color': base_color, 'Metallic': metallic, 'Roughness': roughness, 'IOR': ior, 'Alpha': alpha, 'Normal': normal, 'Weight': weight, 'Diffuse Roughness': diffuse_roughness, 'Subsurface Weight': subsurface_weight, 'Subsurface Radius': subsurface_radius, 'Subsurface Scale': subsurface_scale, 'Subsurface IOR': subsurface_ior, 'Subsurface Anisotropy': subsurface_anisotropy, 'Specular IOR Level': specular_ior_level, 'Specular Tint': specular_tint, 'Anisotropic': anisotropic, 'Anisotropic Rotation': anisotropic_rotation, 'Tangent': tangent, 'Transmission Weight': transmission_weight, 'Coat Weight': coat_weight, 'Coat Roughness': coat_roughness, 'Coat IOR': coat_ior, 'Coat Tint': coat_tint, 'Coat Normal': coat_normal, 'Sheen Weight': sheen_weight, 'Sheen Roughness': sheen_roughness, 'Sheen Tint': sheen_tint, 'Emission Color': emission_color, 'Emission Strength': emission_strength, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, subsurface_method=subsurface_method)
        return node._out

    @classmethod
    def ray_portal_bsdf(cls,
                    color: Color = None,
                    position: Vector = None,
                    direction: Vector = None,
                    weight: Float = None):
        """ > Node <&ShaderNode Ray Portal BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        position : Vector, optional
            socket 'Position' (id: Position)
        
        direction : Vector, optional
            socket 'Direction' (id: Direction)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Ray Portal BSDF', {'Color': color, 'Position': position, 'Direction': direction, 'Weight': weight})
        return node._out

    @classmethod
    def refraction_bsdf(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        distribution : Literal['Beckmann', 'GGX']
            parameter `distribution`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Refraction BSDF', 'distribution', distribution, 'refraction_bsdf', ('BECKMANN', 'GGX'))
        node = Node('Refraction BSDF', {'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def sheen_bsdf(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        distribution : Literal['Ashikhmin', 'Microfiber']
            parameter `distribution`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Sheen BSDF', 'distribution', distribution, 'sheen_bsdf', ('ASHIKHMIN', 'MICROFIBER'))
        node = Node('Sheen BSDF', {'Color': color, 'Roughness': roughness, 'Normal': normal, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def toon_bsdf(cls,
                    color: Color = None,
                    size: Float = None,
                    smooth: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        component : Literal['Diffuse', 'Glossy']
            parameter `component`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Toon BSDF', 'component', component, 'toon_bsdf', ('DIFFUSE', 'GLOSSY'))
        node = Node('Toon BSDF', {'Color': color, 'Size': size, 'Smooth': smooth, 'Normal': normal, 'Weight': weight}, component=component)
        return node._out

    @classmethod
    def translucent_bsdf(cls, color: Color = None, normal: Vector = None, weight: Float = None):
        """ > Node <&ShaderNode Translucent BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Translucent BSDF', {'Color': color, 'Normal': normal, 'Weight': weight})
        return node._out

    @classmethod
    def transparent_bsdf(cls, color: Color = None, weight: Float = None):
        """ > Node <&ShaderNode Transparent BSDF>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Transparent BSDF', {'Color': color, 'Weight': weight})
        return node._out

    @classmethod
    def bump(cls,
                    strength: Float = None,
                    distance: Float = None,
                    filter_width: Float = None,
                    height: Float = None,
                    normal: Vector = None,
                    invert = False):
        """ > Node <&ShaderNode Bump>

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        distance : Float, optional
            socket 'Distance' (id: Distance)
        
        filter_width : Float, optional
            socket 'Filter Width' (id: Filter Width)
        
        height : Float, optional
            socket 'Height' (id: Height)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        invert : bool
            parameter `invert`
        

        Returns
        -------
        Vector
        """
        node = Node('Bump', {'Strength': strength, 'Distance': distance, 'Filter Width': filter_width, 'Height': height, 'Normal': normal}, invert=invert)
        return node._out

    @classmethod
    def camera_data(cls):
        """ > Node <&ShaderNode Camera Data>

        Returns
        -------
        Vector
            peer sockets: view_z_depth_ (Float), view_distance_ (Float)

        """
        node = Node('Camera Data', )
        return node

    @classmethod
    def clamp(cls,
                    value: Float = None,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX'):
        """ > Node <&ShaderNode Clamp>

        Parameters
        ----------
        value : Float, optional
            socket 'Value' (id: Value)
        
        min : Float, optional
            socket 'Min' (id: Min)
        
        max : Float, optional
            socket 'Max' (id: Max)
        
        clamp_type : Literal['Min Max', 'Range']
            parameter `clamp_type`
        

        Returns
        -------
        Float
        """
        utils.check_enum_arg('Clamp', 'clamp_type', clamp_type, 'clamp', ('MINMAX', 'RANGE'))
        node = Node('Clamp', {'Value': value, 'Min': min, 'Max': max}, clamp_type=clamp_type)
        return node._out

    @classmethod
    def combine_color(cls,
                    red: Float = None,
                    green: Float = None,
                    blue: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&ShaderNode Combine Color>

        Parameters
        ----------
        red : Float, optional
            socket 'Red' (id: Red)
        
        green : Float, optional
            socket 'Green' (id: Green)
        
        blue : Float, optional
            socket 'Blue' (id: Blue)
        
        mode : Literal['RGB', 'HSV', 'HSL']
            parameter `mode`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Combine Color', 'mode', mode, 'combine_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Combine Color', {'Red': red, 'Green': green, 'Blue': blue}, mode=mode)
        return node._out

    @classmethod
    def combine_xyz(cls, x: Float = None, y: Float = None, z: Float = None):
        """ > Node <&ShaderNode Combine XYZ>

        Parameters
        ----------
        x : Float, optional
            socket 'X' (id: X)
        
        y : Float, optional
            socket 'Y' (id: Y)
        
        z : Float, optional
            socket 'Z' (id: Z)
        

        Returns
        -------
        Vector
        """
        node = Node('Combine XYZ', {'X': x, 'Y': y, 'Z': z})
        return node._out

    @classmethod
    def displacement(cls,
                    height: Float = None,
                    midlevel: Float = None,
                    scale: Float = None,
                    normal: Vector = None,
                    space: Literal['OBJECT', 'WORLD'] = 'OBJECT'):
        """ > Node <&ShaderNode Displacement>

        Parameters
        ----------
        height : Float, optional
            socket 'Height' (id: Height)
        
        midlevel : Float, optional
            socket 'Midlevel' (id: Midlevel)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        
        space : Literal['Object Space', 'World Space']
            parameter `space`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Displacement', 'space', space, 'displacement', ('OBJECT', 'WORLD'))
        node = Node('Displacement', {'Height': height, 'Midlevel': midlevel, 'Scale': scale, 'Normal': normal}, space=space)
        return node._out

    @classmethod
    def specular_bsdf(cls,
                    base_color: Color = None,
                    specular: Color = None,
                    roughness: Float = None,
                    emissive_color: Color = None,
                    transparency: Float = None,
                    normal: Vector = None,
                    clear_coat: Float = None,
                    clear_coat_roughness: Float = None,
                    clear_coat_normal: Vector = None,
                    weight: Float = None):
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Specular BSDF', {'Base Color': base_color, 'Specular': specular, 'Roughness': roughness, 'Emissive Color': emissive_color, 'Transparency': transparency, 'Normal': normal, 'Clear Coat': clear_coat, 'Clear Coat Roughness': clear_coat_roughness, 'Clear Coat Normal': clear_coat_normal, 'Weight': weight})
        return node._out

    @classmethod
    def emission(cls, color: Color = None, strength: Float = None, weight: Float = None):
        """ > Node <&ShaderNode Emission>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Emission', {'Color': color, 'Strength': strength, 'Weight': weight})
        return node._out

    @classmethod
    def float_curve(cls, value: Float = None, factor: Float = None):
        """ > Node <&ShaderNode Float Curve>

        Parameters
        ----------
        value : Float, optional
            socket 'Value' (id: Value)
        
        factor : Float, optional
            socket 'Factor' (id: Factor)
        

        Returns
        -------
        Float
        """
        node = NodeCurves('Float Curve', {'Value': value, 'Factor': factor})
        return node._out

    @classmethod
    def fresnel(cls, ior: Float = None, normal: Vector = None):
        """ > Node <&ShaderNode Fresnel>

        Parameters
        ----------
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        

        Returns
        -------
        Float
        """
        node = Node('Fresnel', {'IOR': ior, 'Normal': normal})
        return node._out

    @classmethod
    def gamma(cls, color: Color = None, gamma: Float = None):
        """ > Node <&ShaderNode Gamma>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        gamma : Float, optional
            socket 'Gamma' (id: Gamma)
        

        Returns
        -------
        Color
        """
        node = Node('Gamma', {'Color': color, 'Gamma': gamma})
        return node._out

    @classmethod
    def group(cls, node_tree = None):
        """ > Node <&ShaderNode Group>

        Parameters
        ----------
        node_tree : NoneType
            parameter `node_tree`
        

        Returns
        -------
        None
        """
        node = Node('Group', node_tree=node_tree)
        return node._out

    @classmethod
    def curves_info(cls):
        """ > Node <&ShaderNode Curves Info>

        Returns
        -------
        Float
            peer sockets: intercept_ (Float), length_ (Float), thickness_ (Float), tangent_normal_ (Vector), random_ (Float)

        """
        node = Node('Curves Info', )
        return node

    @classmethod
    def holdout(cls, weight: Float = None):
        """ > Node <&ShaderNode Holdout>

        Parameters
        ----------
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        Shader
        """
        node = Node('Holdout', {'Weight': weight})
        return node._out

    @classmethod
    def hue_saturation_value(cls,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    color: Color = None,
                    factor: Float = None):
        """ > Node <&ShaderNode Hue/Saturation/Value>

        Parameters
        ----------
        hue : Float, optional
            socket 'Hue' (id: Hue)
        
        saturation : Float, optional
            socket 'Saturation' (id: Saturation)
        
        value : Float, optional
            socket 'Value' (id: Value)
        
        color : Color, optional
            socket 'Color' (id: Color)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Color
        """
        node = Node('Hue/Saturation/Value', {'Hue': hue, 'Saturation': saturation, 'Value': value, 'Color': color, 'Fac': factor})
        return node._out

    @classmethod
    def invert_color(cls, color: Color = None, factor: Float = None):
        """ > Node <&ShaderNode Invert Color>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Color
        """
        node = Node('Invert Color', {'Color': color, 'Fac': factor})
        return node._out

    @classmethod
    def layer_weight(cls, blend: Float = None, normal: Vector = None):
        """ > Node <&ShaderNode Layer Weight>

        Parameters
        ----------
        blend : Float, optional
            socket 'Blend' (id: Blend)
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        

        Returns
        -------
        Float
            peer sockets: facing_ (Float)

        """
        node = Node('Layer Weight', {'Blend': blend, 'Normal': normal})
        return node._out

    @classmethod
    def light_falloff(cls, strength: Float = None, smooth: Float = None):
        """ > Node <&ShaderNode Light Falloff>

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        smooth : Float, optional
            socket 'Smooth' (id: Smooth)
        

        Returns
        -------
        Float
            peer sockets: linear_ (Float), constant_ (Float)

        """
        node = Node('Light Falloff', {'Strength': strength, 'Smooth': smooth})
        return node._out

    @classmethod
    def light_path(cls):
        """ > Node <&ShaderNode Light Path>

        Returns
        -------
        Float
            peer sockets: is_shadow_ray_ (Float), is_diffuse_ray_ (Float), is_glossy_ray_ (Float), is_singular_ray_ (Float), is_reflection_ray_ (Float), is_transmission_ray_ (Float), is_volume_scatter_ray_ (Float), ray_length_ (Float), ray_depth_ (Float), diffuse_depth_ (Float), glossy_depth_ (Float), transparent_depth_ (Float), transmission_depth_ (Float), portal_depth_ (Float)

        """
        node = Node('Light Path', )
        return node

    @classmethod
    def map_range(cls,
                    value: Float = None,
                    from_min: Float = None,
                    from_max: Float = None,
                    to_min: Float = None,
                    to_max: Float = None,
                    steps: Float = None,
                    vector: Vector = None,
                    from_min_1: Vector = None,
                    from_max_1: Vector = None,
                    to_min_1: Vector = None,
                    to_max_1: Vector = None,
                    steps_1: Vector = None,
                    clamp = True,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR'):
        """ > Node <&ShaderNode Map Range>

        Parameters
        ----------
        value : Float, optional
            socket 'Value' (id: Value)
        
        from_min : Float, optional
            socket 'From Min' (id: From Min)
        
        from_max : Float, optional
            socket 'From Max' (id: From Max)
        
        to_min : Float, optional
            socket 'To Min' (id: To Min)
        
        to_max : Float, optional
            socket 'To Max' (id: To Max)
        
        steps : Float, optional
            socket 'Steps' (id: Steps)
        
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        from_min_1 : Vector, optional
            socket 'From Min' (id: From_Min_FLOAT3)
        
        from_max_1 : Vector, optional
            socket 'From Max' (id: From_Max_FLOAT3)
        
        to_min_1 : Vector, optional
            socket 'To Min' (id: To_Min_FLOAT3)
        
        to_max_1 : Vector, optional
            socket 'To Max' (id: To_Max_FLOAT3)
        
        steps_1 : Vector, optional
            socket 'Steps' (id: Steps_FLOAT3)
        
        clamp : bool
            parameter `clamp`
        
        data_type : Literal['Float', 'Vector']
            parameter `data_type`
        
        interpolation_type : Literal['Linear', 'Stepped Linear', 'Smooth Step', 'Smoother Step']
            parameter `interpolation_type`
        

        Returns
        -------
        Float
        """
        utils.check_enum_arg('Map Range', 'interpolation_type', interpolation_type, 'map_range', ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'))
        node = Node('Map Range', {'Value': value, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max, 'Steps': steps, 'Vector': vector, 'From_Min_FLOAT3': from_min_1, 'From_Max_FLOAT3': from_max_1, 'To_Min_FLOAT3': to_min_1, 'To_Max_FLOAT3': to_max_1, 'Steps_FLOAT3': steps_1}, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)
        return node._out

    @classmethod
    def mapping(cls,
                    vector: Vector = None,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT'):
        """ > Node <&ShaderNode Mapping>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        location : Vector, optional
            socket 'Location' (id: Location)
        
        rotation : Vector, optional
            socket 'Rotation' (id: Rotation)
        
        scale : Vector, optional
            socket 'Scale' (id: Scale)
        
        vector_type : Literal['Point', 'Texture', 'Vector', 'Normal']
            parameter `vector_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Mapping', 'vector_type', vector_type, 'mapping', ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL'))
        node = Node('Mapping', {'Vector': vector, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    @classmethod
    def math(cls,
                    value: Float = None,
                    value_1: Float = None,
                    value_2: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD',
                    use_clamp = False):
        """ > Node <&ShaderNode Math>

        Parameters
        ----------
        value : Float, optional
            socket 'Value' (id: Value)
        
        value_1 : Float, optional
            socket 'Value' (id: Value_001)
        
        value_2 : Float, optional
            socket 'Value' (id: Value_002)
        
        operation : Literal['Add', 'Subtract', 'Multiply', 'Divide', 'Multiply Add', 'Power', 'Logarithm', 'Square Root', 'Inverse Square Root', 'Absolute', 'Exponent', 'Minimum', 'Maximum', 'Less Than', 'Greater Than', 'Sign', 'Compare', 'Smooth Minimum', 'Smooth Maximum', 'Round', 'Floor', 'Ceil', 'Truncate', 'Fraction', 'Truncated Modulo', 'Floored Modulo', 'Wrap', 'Snap', 'Ping-Pong', 'Sine', 'Cosine', 'Tangent', 'Arcsine', 'Arccosine', 'Arctangent', 'Arctan2', 'Hyperbolic Sine', 'Hyperbolic Cosine', 'Hyperbolic Tangent', 'To Radians', 'To Degrees']
            parameter `operation`
        
        use_clamp : bool
            parameter `use_clamp`
        

        Returns
        -------
        Float
        """
        utils.check_enum_arg('Math', 'operation', operation, 'math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'))
        node = Node('Math', {'Value': value, 'Value_001': value_1, 'Value_002': value_2}, operation=operation, use_clamp=use_clamp)
        return node._out

    @classmethod
    def mix(cls,
                    a: Float = None,
                    b: Float = None,
                    a_1: Vector = None,
                    b_1: Vector = None,
                    a_2: Color = None,
                    b_2: Color = None,
                    a_3: Rotation = None,
                    b_3: Rotation = None,
                    factor: Vector = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    clamp_factor = True,
                    clamp_result = False,
                    data_type: Literal['FLOAT', 'VECTOR', 'RGBA'] = 'FLOAT',
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM'):
        """ > Node <&ShaderNode Mix>

        Parameters
        ----------
        a : Float, optional
            socket 'A' (id: A_Float)
        
        b : Float, optional
            socket 'B' (id: B_Float)
        
        a_1 : Vector, optional
            socket 'A' (id: A_Vector)
        
        b_1 : Vector, optional
            socket 'B' (id: B_Vector)
        
        a_2 : Color, optional
            socket 'A' (id: A_Color)
        
        b_2 : Color, optional
            socket 'B' (id: B_Color)
        
        a_3 : Rotation, optional
            socket 'A' (id: A_Rotation)
        
        b_3 : Rotation, optional
            socket 'B' (id: B_Rotation)
        
        factor : Vector, optional
            socket 'Factor' (id: Factor_Vector)
        
        blend_type : Literal['Mix', 'Darken', 'Multiply', 'Color Burn', 'Lighten', 'Screen', 'Color Dodge', 'Add', 'Overlay', 'Soft Light', 'Linear Light', 'Difference', 'Exclusion', 'Subtract', 'Divide', 'Hue', 'Saturation', 'Color', 'Value']
            parameter `blend_type`
        
        clamp_factor : bool
            parameter `clamp_factor`
        
        clamp_result : bool
            parameter `clamp_result`
        
        data_type : Literal['Float', 'Vector', 'Color']
            parameter `data_type`
        
        factor_mode : Literal['Uniform', 'Non-Uniform']
            parameter `factor_mode`
        

        Returns
        -------
        Float
        """
        utils.check_enum_arg('Mix', 'blend_type', blend_type, 'mix', ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'))
        utils.check_enum_arg('Mix', 'factor_mode', factor_mode, 'mix', ('UNIFORM', 'NON_UNIFORM'))
        node = Node('Mix', {'A_Float': a, 'B_Float': b, 'A_Vector': a_1, 'B_Vector': b_1, 'A_Color': a_2, 'B_Color': b_2, 'A_Rotation': a_3, 'B_Rotation': b_3, 'Factor_Vector': factor}, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type=data_type, factor_mode=factor_mode)
        return node._out

    @classmethod
    def mix_shader(cls, shader: Shader = None, shader_1: Shader = None, factor: Float = None):
        """ > Node <&ShaderNode Mix Shader>

        Parameters
        ----------
        shader : Shader, optional
            socket 'Shader' (id: Shader)
        
        shader_1 : Shader, optional
            socket 'Shader' (id: Shader_001)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Shader
        """
        node = Node('Mix Shader', {'Shader': shader, 'Shader_001': shader_1, 'Fac': factor})
        return node._out

    @classmethod
    def geometry(cls):
        """ > Node <&ShaderNode Geometry>

        Returns
        -------
        Vector
            peer sockets: normal_ (Vector), tangent_ (Vector), true_normal_ (Vector), incoming_ (Vector), parametric_ (Vector), backfacing_ (Float), pointiness_ (Float), random_per_island_ (Float)

        """
        node = Node('Geometry', )
        return node

    @classmethod
    def normal(cls, normal: Vector = None):
        """ > Node <&ShaderNode Normal>

        Parameters
        ----------
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        

        Returns
        -------
        Vector
            peer sockets: dot_ (Float)

        """
        node = Node('Normal', {'Normal': normal})
        return node._out

    @classmethod
    def normal_map(cls,
                    strength: Float = None,
                    color: Color = None,
                    base: Literal['ORIGINAL', 'DISPLACED'] = 'DISPLACED',
                    convention: Literal['OPENGL', 'DIRECTX'] = 'OPENGL',
                    space: Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT',
                    uv_map = ''):
        """ > Node <&ShaderNode Normal Map>

        Parameters
        ----------
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        color : Color, optional
            socket 'Color' (id: Color)
        
        base : Literal['Original Base', 'Displaced Base']
            parameter `base`
        
        convention : Literal['OpenGL', 'DirectX']
            parameter `convention`
        
        space : Literal['Tangent Space', 'Object Space', 'World Space', 'Blender Object Space', 'Blender World Space']
            parameter `space`
        
        uv_map : str
            parameter `uv_map`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Normal Map', 'base', base, 'normal_map', ('ORIGINAL', 'DISPLACED'))
        utils.check_enum_arg('Normal Map', 'convention', convention, 'normal_map', ('OPENGL', 'DIRECTX'))
        utils.check_enum_arg('Normal Map', 'space', space, 'normal_map', ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'))
        node = Node('Normal Map', {'Strength': strength, 'Color': color}, base=base, convention=convention, space=space, uv_map=uv_map)
        return node._out

    @classmethod
    def object_info(cls):
        """ > Node <&ShaderNode Object Info>

        Returns
        -------
        Vector
            peer sockets: color_ (Color), alpha_ (Float), object_index_ (Float), material_index_ (Float), random_ (Float)

        """
        node = Node('Object Info', )
        return node

    @classmethod
    def aov_output(cls, color: Color = None, value: Float = None, aov_name = ''):
        """ > Node <&ShaderNode AOV Output>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        value : Float, optional
            socket 'Value' (id: Value)
        
        aov_name : str
            parameter `aov_name`
        

        Returns
        -------
        None
        """
        node = Node('AOV Output', {'Color': color, 'Value': value}, aov_name=aov_name)
        return node._out

    @classmethod
    def light_output(cls,
                    surface: Shader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode Light Output>

        Parameters
        ----------
        surface : Shader, optional
            socket 'Surface' (id: Surface)
        
        is_active_output : bool
            parameter `is_active_output`
        
        target : Literal['All', 'EEVEE', 'Cycles']
            parameter `target`
        

        Returns
        -------
        None
        """
        utils.check_enum_arg('Light Output', 'target', target, 'light_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Light Output', {'Surface': surface}, is_active_output=is_active_output, target=target)
        return node._out

    @classmethod
    def line_style_output(cls,
                    color: Color = None,
                    color_fac: Float = None,
                    alpha: Float = None,
                    alpha_fac: Float = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL',
                    use_alpha = False,
                    use_clamp = False):
        """ > Node <&ShaderNode Line Style Output>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        color_fac : Float, optional
            socket 'Color Fac' (id: Color Fac)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        
        alpha_fac : Float, optional
            socket 'Alpha Fac' (id: Alpha Fac)
        
        blend_type : Literal['Mix', 'Darken', 'Multiply', 'Color Burn', 'Lighten', 'Screen', 'Color Dodge', 'Add', 'Overlay', 'Soft Light', 'Linear Light', 'Difference', 'Exclusion', 'Subtract', 'Divide', 'Hue', 'Saturation', 'Color', 'Value']
            parameter `blend_type`
        
        is_active_output : bool
            parameter `is_active_output`
        
        target : Literal['All', 'EEVEE', 'Cycles']
            parameter `target`
        
        use_alpha : bool
            parameter `use_alpha`
        
        use_clamp : bool
            parameter `use_clamp`
        

        Returns
        -------
        None
        """
        utils.check_enum_arg('Line Style Output', 'blend_type', blend_type, 'line_style_output', ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'))
        utils.check_enum_arg('Line Style Output', 'target', target, 'line_style_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Line Style Output', {'Color': color, 'Color Fac': color_fac, 'Alpha': alpha, 'Alpha Fac': alpha_fac}, blend_type=blend_type, is_active_output=is_active_output, target=target, use_alpha=use_alpha, use_clamp=use_clamp)
        return node._out

    @classmethod
    def material_output(cls,
                    surface: Shader = None,
                    volume: VolumeShader = None,
                    displacement: Vector = None,
                    thickness: Float = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode Material Output>

        Parameters
        ----------
        surface : Shader, optional
            socket 'Surface' (id: Surface)
        
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
        node = Node('Material Output', {'Surface': surface, 'Volume': volume, 'Displacement': displacement, 'Thickness': thickness}, is_active_output=is_active_output, target=target)
        return node._out

    @classmethod
    def world_output(cls,
                    surface: Shader = None,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL'):
        """ > Node <&ShaderNode World Output>

        Parameters
        ----------
        surface : Shader, optional
            socket 'Surface' (id: Surface)
        
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
        node = Node('World Output', {'Surface': surface, 'Volume': volume}, is_active_output=is_active_output, target=target)
        return node._out

    @classmethod
    def particle_info(cls):
        """ > Node <&ShaderNode Particle Info>

        Returns
        -------
        Float
            peer sockets: random_ (Float), age_ (Float), lifetime_ (Float), location_ (Vector), size_ (Float), velocity_ (Vector), angular_velocity_ (Vector)

        """
        node = Node('Particle Info', )
        return node

    @classmethod
    def point_info(cls):
        """ > Node <&ShaderNode Point Info>

        Returns
        -------
        Vector
            peer sockets: radius_ (Float), random_ (Float)

        """
        node = Node('Point Info', )
        return node

    @utils.classproperty
    def color(self):
        """ > Node <&ShaderNode Color>

        Returns
        -------
        Color
        """
        node = Node('Color', )
        return node._out

    @classmethod
    def rgb_curves(cls, color: Color = None, factor: Float = None):
        """ > Node <&ShaderNode RGB Curves>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Color
        """
        node = NodeCurves('RGB Curves', {'Color': color, 'Fac': factor})
        return node._out

    @classmethod
    def rgb_to_bw(cls, color: Color = None):
        """ > Node <&ShaderNode RGB to BW>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        

        Returns
        -------
        Float
        """
        node = Node('RGB to BW', {'Color': color})
        return node._out

    @classmethod
    def radial_tiling(cls,
                    vector: Vector = None,
                    sides: Float = None,
                    roundness: Float = None,
                    normalize = False):
        """ > Node <&ShaderNode Radial Tiling>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        sides : Float, optional
            socket 'Sides' (id: Sides)
        
        roundness : Float, optional
            socket 'Roundness' (id: Roundness)
        
        normalize : bool
            parameter `normalize`
        

        Returns
        -------
        Vector
            peer sockets: segment_id_ (Float), segment_width_ (Float), segment_rotation_ (Float)

        """
        node = Node('Radial Tiling', {'Vector': vector, 'Sides': sides, 'Roundness': roundness}, normalize=normalize)
        return node._out

    @classmethod
    def raycast(cls,
                    position: Vector = None,
                    direction: Vector = None,
                    length: Float = None,
                    only_local = False):
        """ > Node <&ShaderNode Raycast>

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        direction : Vector, optional
            socket 'Direction' (id: Direction)
        
        length : Float, optional
            socket 'Length' (id: Length)
        
        only_local : bool
            parameter `only_local`
        

        Returns
        -------
        Float
            peer sockets: self_hit_ (Float), hit_distance_ (Float), hit_position_ (Vector), hit_normal_ (Vector)

        """
        node = Node('Raycast', {'Position': position, 'Direction': direction, 'Length': length}, only_local=only_local)
        return node._out

    @classmethod
    def script(cls,
                    bytecode = '',
                    bytecode_hash = '',
                    filepath = '',
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL',
                    script = None,
                    use_auto_update = False):
        """ > Node <&ShaderNode Script>

        Parameters
        ----------
        bytecode : str
            parameter `bytecode`
        
        bytecode_hash : str
            parameter `bytecode_hash`
        
        filepath : str
            parameter `filepath`
        
        mode : Literal['Internal', 'External']
            parameter `mode`
        
        script : NoneType
            parameter `script`
        
        use_auto_update : bool
            parameter `use_auto_update`
        

        Returns
        -------
        None
        """
        utils.check_enum_arg('Script', 'mode', mode, 'script', ('INTERNAL', 'EXTERNAL'))
        node = Node('Script', bytecode=bytecode, bytecode_hash=bytecode_hash, filepath=filepath, mode=mode, script=script, use_auto_update=use_auto_update)
        return node._out

    @classmethod
    def separate_color(cls, color: Color = None, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB'):
        """ > Node <&ShaderNode Separate Color>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        mode : Literal['RGB', 'HSV', 'HSL']
            parameter `mode`
        

        Returns
        -------
        Float
            peer sockets: green_ (Float), blue_ (Float)

        """
        utils.check_enum_arg('Separate Color', 'mode', mode, 'separate_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Separate Color', {'Color': color}, mode=mode)
        return node

    @classmethod
    def separate_xyz(cls, vector: Vector = None):
        """ > Node <&ShaderNode Separate XYZ>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        

        Returns
        -------
        Float
            peer sockets: y_ (Float), z_ (Float)

        """
        node = Node('Separate XYZ', {'Vector': vector})
        return node

    @classmethod
    def shader_to_rgb(cls, shader: Shader = None):
        """ > Node <&ShaderNode Shader to RGB>

        Parameters
        ----------
        shader : Shader, optional
            socket 'Shader' (id: Shader)
        

        Returns
        -------
        Color
            peer sockets: alpha_ (Float)

        """
        node = Node('Shader to RGB', {'Shader': shader})
        return node._out

    @classmethod
    def subsurface_scattering(cls,
                    color: Color = None,
                    scale: Float = None,
                    radius: Vector = None,
                    ior: Float = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
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
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        falloff : Literal['Christensen-Burley', 'Random Walk', 'Random Walk (Skin)']
            parameter `falloff`
        

        Returns
        -------
        Shader
        """
        utils.check_enum_arg('Subsurface Scattering', 'falloff', falloff, 'subsurface_scattering', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Subsurface Scattering', {'Color': color, 'Scale': scale, 'Radius': radius, 'IOR': ior, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Normal': normal, 'Weight': weight}, falloff=falloff)
        return node._out

    @classmethod
    def tangent(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = ''):
        """ > Node <&ShaderNode Tangent>

        Parameters
        ----------
        axis : Literal['X', 'Y', 'Z']
            parameter `axis`
        
        direction_type : Literal['Radial', 'UV Map']
            parameter `direction_type`
        
        uv_map : str
            parameter `uv_map`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Tangent', 'axis', axis, 'tangent', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Tangent', 'direction_type', direction_type, 'tangent', ('RADIAL', 'UV_MAP'))
        node = Node('Tangent', axis=axis, direction_type=direction_type, uv_map=uv_map)
        return node._out

    @classmethod
    def brick_texture(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2):
        """ > Node <&ShaderNode Brick Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        color1 : Color, optional
            socket 'Color1' (id: Color1)
        
        color2 : Color, optional
            socket 'Color2' (id: Color2)
        
        mortar : Color, optional
            socket 'Mortar' (id: Mortar)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        mortar_size : Float, optional
            socket 'Mortar Size' (id: Mortar Size)
        
        mortar_smooth : Float, optional
            socket 'Mortar Smooth' (id: Mortar Smooth)
        
        bias : Float, optional
            socket 'Bias' (id: Bias)
        
        brick_width : Float, optional
            socket 'Brick Width' (id: Brick Width)
        
        row_height : Float, optional
            socket 'Row Height' (id: Row Height)
        
        offset : float
            parameter `offset`
        
        offset_frequency : int
            parameter `offset_frequency`
        
        squash : float
            parameter `squash`
        
        squash_frequency : int
            parameter `squash_frequency`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        node = Node('Brick Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node._out

    @classmethod
    def checker_texture(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None):
        """ > Node <&ShaderNode Checker Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        color1 : Color, optional
            socket 'Color1' (id: Color1)
        
        color2 : Color, optional
            socket 'Color2' (id: Color2)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        node = Node('Checker Texture', {'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return node._out

    @classmethod
    def texture_coordinate(cls, from_instancer = False, object = None):
        """ > Node <&ShaderNode Texture Coordinate>

        Parameters
        ----------
        from_instancer : bool
            parameter `from_instancer`
        
        object : NoneType
            parameter `object`
        

        Returns
        -------
        Vector
            peer sockets: normal_ (Vector), uv_ (Vector), object_ (Vector), camera_ (Vector), window_ (Vector), reflection_ (Vector)

        """
        node = Node('Texture Coordinate', from_instancer=from_instancer, object=object)
        return node

    @classmethod
    def environment_texture(cls,
                    vector: Vector = None,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR'):
        """ > Node <&ShaderNode Environment Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        image : NoneType
            parameter `image`
        
        interpolation : Literal['Linear', 'Closest', 'Cubic', 'Smart']
            parameter `interpolation`
        
        projection : Literal['Equirectangular', 'Mirror Ball']
            parameter `projection`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Environment Texture', 'interpolation', interpolation, 'environment_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Environment Texture', 'projection', projection, 'environment_texture', ('EQUIRECTANGULAR', 'MIRROR_BALL'))
        node = Node('Environment Texture', {'Vector': vector}, image=image, interpolation=interpolation, projection=projection)
        return node._out

    @classmethod
    def gabor_texture(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    orientation_1: Vector = None,
                    gabor_type: Literal['2D', '3D'] = '2D'):
        """ > Node <&ShaderNode Gabor Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        frequency : Float, optional
            socket 'Frequency' (id: Frequency)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        orientation : Float, optional
            socket 'Orientation' (id: Orientation 2D)
        
        orientation_1 : Vector, optional
            socket 'Orientation' (id: Orientation 3D)
        
        gabor_type : Literal['2D', '3D']
            parameter `gabor_type`
        

        Returns
        -------
        Float
            peer sockets: phase_ (Float), intensity_ (Float)

        """
        utils.check_enum_arg('Gabor Texture', 'gabor_type', gabor_type, 'gabor_texture', ('2D', '3D'))
        node = Node('Gabor Texture', {'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation 2D': orientation, 'Orientation 3D': orientation_1}, gabor_type=gabor_type)
        return node._out

    @classmethod
    def gradient_texture(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR'):
        """ > Node <&ShaderNode Gradient Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        gradient_type : Literal['Linear', 'Quadratic', 'Easing', 'Diagonal', 'Spherical', 'Quadratic Sphere', 'Radial']
            parameter `gradient_type`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        utils.check_enum_arg('Gradient Texture', 'gradient_type', gradient_type, 'gradient_texture', ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'))
        node = Node('Gradient Texture', {'Vector': vector}, gradient_type=gradient_type)
        return node._out

    @classmethod
    def ies_texture(cls,
                    vector: Vector = None,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL'):
        """ > Node <&ShaderNode IES Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        strength : Float, optional
            socket 'Strength' (id: Strength)
        
        filepath : str
            parameter `filepath`
        
        ies : NoneType
            parameter `ies`
        
        mode : Literal['Internal', 'External']
            parameter `mode`
        

        Returns
        -------
        Float
        """
        utils.check_enum_arg('IES Texture', 'mode', mode, 'ies_texture', ('INTERNAL', 'EXTERNAL'))
        node = Node('IES Texture', {'Vector': vector, 'Strength': strength}, filepath=filepath, ies=ies, mode=mode)
        return node._out

    @classmethod
    def image_texture(cls,
                    vector: Vector = None,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0):
        """ > Node <&ShaderNode Image Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        extension : Literal['Repeat', 'Extend', 'Clip', 'Mirror']
            parameter `extension`
        
        image : NoneType
            parameter `image`
        
        interpolation : Literal['Linear', 'Closest', 'Cubic', 'Smart']
            parameter `interpolation`
        
        projection : Literal['Flat', 'Box', 'Sphere', 'Tube']
            parameter `projection`
        
        projection_blend : float
            parameter `projection_blend`
        

        Returns
        -------
        Color
            peer sockets: alpha_ (Float)

        """
        utils.check_enum_arg('Image Texture', 'extension', extension, 'image_texture', ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'))
        utils.check_enum_arg('Image Texture', 'interpolation', interpolation, 'image_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Image Texture', 'projection', projection, 'image_texture', ('FLAT', 'BOX', 'SPHERE', 'TUBE'))
        node = Node('Image Texture', {'Vector': vector}, extension=extension, image=image, interpolation=interpolation, projection=projection, projection_blend=projection_blend)
        return node._out

    @classmethod
    def magic_texture(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2):
        """ > Node <&ShaderNode Magic Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        turbulence_depth : int
            parameter `turbulence_depth`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        node = Node('Magic Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return node._out

    @classmethod
    def noise_texture(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    offset: Float = None,
                    gain: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True):
        """ > Node <&ShaderNode Noise Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        w : Float, optional
            socket 'W' (id: W)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        lacunarity : Float, optional
            socket 'Lacunarity' (id: Lacunarity)
        
        offset : Float, optional
            socket 'Offset' (id: Offset)
        
        gain : Float, optional
            socket 'Gain' (id: Gain)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        noise_dimensions : Literal['1D', '2D', '3D', '4D']
            parameter `noise_dimensions`
        
        noise_type : Literal['Multifractal', 'Ridged Multifractal', 'Hybrid Multifractal', 'fBM', 'Hetero Terrain']
            parameter `noise_type`
        
        normalize : bool
            parameter `normalize`
        

        Returns
        -------
        Float
            peer sockets: color_ (Color)

        """
        utils.check_enum_arg('Noise Texture', 'noise_dimensions', noise_dimensions, 'noise_texture', ('1D', '2D', '3D', '4D'))
        utils.check_enum_arg('Noise Texture', 'noise_type', noise_type, 'noise_texture', ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'))
        node = Node('Noise Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Offset': offset, 'Gain': gain, 'Distortion': distortion}, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize)
        return node._out

    @classmethod
    def sky_texture(cls,
                    vector: Vector = None,
                    aerosol_density = 1.0,
                    air_density = 1.0,
                    altitude = 100.0,
                    ground_albedo = 0.30000001192092896,
                    ozone_density = 1.0,
                    sky_type: Literal['SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'] = 'MULTIPLE_SCATTERING',
                    sun_disc = True,
                    sun_elevation = 0.2617993950843811,
                    sun_intensity = 1.0,
                    sun_rotation = 0.0,
                    sun_size = 0.009512044489383698,
                    turbidity = 2.200000047683716):
        """ > Node <&ShaderNode Sky Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        aerosol_density : float
            parameter `aerosol_density`
        
        air_density : float
            parameter `air_density`
        
        altitude : float
            parameter `altitude`
        
        ground_albedo : float
            parameter `ground_albedo`
        
        ozone_density : float
            parameter `ozone_density`
        
        sky_type : Literal['Single Scattering', 'Multiple Scattering', 'Preetham', 'Hosek / Wilkie']
            parameter `sky_type`
        
        sun_disc : bool
            parameter `sun_disc`
        
        sun_elevation : float
            parameter `sun_elevation`
        
        sun_intensity : float
            parameter `sun_intensity`
        
        sun_rotation : float
            parameter `sun_rotation`
        
        sun_size : float
            parameter `sun_size`
        
        turbidity : float
            parameter `turbidity`
        

        Returns
        -------
        Color
        """
        utils.check_enum_arg('Sky Texture', 'sky_type', sky_type, 'sky_texture', ('SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'))
        node = Node('Sky Texture', {'Vector': vector}, aerosol_density=aerosol_density, air_density=air_density, altitude=altitude, ground_albedo=ground_albedo, ozone_density=ozone_density, sky_type=sky_type, sun_disc=sun_disc, sun_elevation=sun_elevation, sun_intensity=sun_intensity, sun_rotation=sun_rotation, sun_size=sun_size, turbidity=turbidity)
        return node._out

    @classmethod
    def voronoi_texture(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    smoothness: Float = None,
                    exponent: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&ShaderNode Voronoi Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        w : Float, optional
            socket 'W' (id: W)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        roughness : Float, optional
            socket 'Roughness' (id: Roughness)
        
        lacunarity : Float, optional
            socket 'Lacunarity' (id: Lacunarity)
        
        smoothness : Float, optional
            socket 'Smoothness' (id: Smoothness)
        
        exponent : Float, optional
            socket 'Exponent' (id: Exponent)
        
        randomness : Float, optional
            socket 'Randomness' (id: Randomness)
        
        distance : Literal['Euclidean', 'Manhattan', 'Chebychev', 'Minkowski']
            parameter `distance`
        
        feature : Literal['F1', 'F2', 'Smooth F1', 'Distance to Edge', 'N-Sphere Radius']
            parameter `feature`
        
        normalize : bool
            parameter `normalize`
        
        voronoi_dimensions : Literal['1D', '2D', '3D', '4D']
            parameter `voronoi_dimensions`
        

        Returns
        -------
        Float
            peer sockets: color_ (Color), position_ (Vector)

        """
        utils.check_enum_arg('Voronoi Texture', 'distance', distance, 'voronoi_texture', ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'))
        utils.check_enum_arg('Voronoi Texture', 'feature', feature, 'voronoi_texture', ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'))
        utils.check_enum_arg('Voronoi Texture', 'voronoi_dimensions', voronoi_dimensions, 'voronoi_texture', ('1D', '2D', '3D', '4D'))
        node = Node('Voronoi Texture', {'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Smoothness': smoothness, 'Exponent': exponent, 'Randomness': randomness}, distance=distance, feature=feature, normalize=normalize, voronoi_dimensions=voronoi_dimensions)
        return node._out

    @classmethod
    def wave_texture(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS'):
        """ > Node <&ShaderNode Wave Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        distortion : Float, optional
            socket 'Distortion' (id: Distortion)
        
        detail : Float, optional
            socket 'Detail' (id: Detail)
        
        detail_scale : Float, optional
            socket 'Detail Scale' (id: Detail Scale)
        
        detail_roughness : Float, optional
            socket 'Detail Roughness' (id: Detail Roughness)
        
        phase_offset : Float, optional
            socket 'Phase Offset' (id: Phase Offset)
        
        bands_direction : Literal['X', 'Y', 'Z', 'Diagonal']
            parameter `bands_direction`
        
        rings_direction : Literal['X', 'Y', 'Z', 'Spherical']
            parameter `rings_direction`
        
        wave_profile : Literal['Sine', 'Saw', 'Triangle']
            parameter `wave_profile`
        
        wave_type : Literal['Bands', 'Rings']
            parameter `wave_type`
        

        Returns
        -------
        Color
            peer sockets: factor_ (Float)

        """
        utils.check_enum_arg('Wave Texture', 'bands_direction', bands_direction, 'wave_texture', ('X', 'Y', 'Z', 'DIAGONAL'))
        utils.check_enum_arg('Wave Texture', 'rings_direction', rings_direction, 'wave_texture', ('X', 'Y', 'Z', 'SPHERICAL'))
        utils.check_enum_arg('Wave Texture', 'wave_profile', wave_profile, 'wave_texture', ('SIN', 'SAW', 'TRI'))
        utils.check_enum_arg('Wave Texture', 'wave_type', wave_type, 'wave_texture', ('BANDS', 'RINGS'))
        node = Node('Wave Texture', {'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node._out

    @classmethod
    def white_noise_texture(cls,
                    vector: Vector = None,
                    w: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D'):
        """ > Node <&ShaderNode White Noise Texture>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        w : Float, optional
            socket 'W' (id: W)
        
        noise_dimensions : Literal['1D', '2D', '3D', '4D']
            parameter `noise_dimensions`
        

        Returns
        -------
        Float
            peer sockets: color_ (Color)

        """
        utils.check_enum_arg('White Noise Texture', 'noise_dimensions', noise_dimensions, 'white_noise_texture', ('1D', '2D', '3D', '4D'))
        node = Node('White Noise Texture', {'Vector': vector, 'W': w}, noise_dimensions=noise_dimensions)
        return node._out

    @classmethod
    def uv_along_stroke(cls, use_tips = False):
        """ > Node <&ShaderNode UV Along Stroke>

        Parameters
        ----------
        use_tips : bool
            parameter `use_tips`
        

        Returns
        -------
        Vector
        """
        node = Node('UV Along Stroke', use_tips=use_tips)
        return node._out

    @classmethod
    def uv_map(cls, from_instancer = False, uv_map = ''):
        """ > Node <&ShaderNode UV Map>

        Parameters
        ----------
        from_instancer : bool
            parameter `from_instancer`
        
        uv_map : str
            parameter `uv_map`
        

        Returns
        -------
        Vector
        """
        node = Node('UV Map', from_instancer=from_instancer, uv_map=uv_map)
        return node._out

    @classmethod
    def color_ramp(cls, fac=None, stops=None, interpolation='LINEAR'):
        """ Node <&Node Color Ramp>

        Exposes utilities to manage the color ramp

        ``` python
        ramp1 = Float(.5).color_ramp(stops=[.1, .9])
        ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
        ```

        Parameters
        ----------
        fac : Float, optional

        stops : list[tuple[float, tuple]]
            Stops made of (float, color as tuple of floats)

        interpolation : {'EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT'}

        """
        node = ColorRamp(fac=fac, stops=stops, interpolation=interpolation)
        return node._out

    @utils.classproperty
    def value(self):
        """ > Node <&ShaderNode Value>

        Returns
        -------
        Float
        """
        node = Node('Value', )
        return node._out

    @classmethod
    def vector_curves(cls, vector: Vector = None, factor: Float = None):
        """ > Node <&ShaderNode Vector Curves>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        factor : Float, optional
            socket 'Factor' (id: Fac)
        

        Returns
        -------
        Vector
        """
        node = NodeCurves('Vector Curves', {'Vector': vector, 'Fac': factor})
        return node._out

    @classmethod
    def vector_displacement(cls,
                    vector: Color = None,
                    midlevel: Float = None,
                    scale: Float = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT'):
        """ > Node <&ShaderNode Vector Displacement>

        Parameters
        ----------
        vector : Color, optional
            socket 'Vector' (id: Vector)
        
        midlevel : Float, optional
            socket 'Midlevel' (id: Midlevel)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        space : Literal['Tangent Space', 'Object Space', 'World Space']
            parameter `space`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Displacement', 'space', space, 'vector_displacement', ('TANGENT', 'OBJECT', 'WORLD'))
        node = Node('Vector Displacement', {'Vector': vector, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out

    @classmethod
    def vector_math(cls,
                    vector: Vector = None,
                    vector_1: Vector = None,
                    vector_2: Vector = None,
                    scale: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD'):
        """ > Node <&ShaderNode Vector Math>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        vector_1 : Vector, optional
            socket 'Vector' (id: Vector_001)
        
        vector_2 : Vector, optional
            socket 'Vector' (id: Vector_002)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        operation : Literal['Add', 'Subtract', 'Multiply', 'Divide', 'Multiply Add', 'Cross Product', 'Project', 'Reflect', 'Refract', 'Faceforward', 'Dot Product', 'Distance', 'Length', 'Scale', 'Normalize', 'Absolute', 'Power', 'Sign', 'Minimum', 'Maximum', 'Round', 'Floor', 'Ceil', 'Fraction', 'Modulo', 'Wrap', 'Snap', 'Sine', 'Cosine', 'Tangent']
            parameter `operation`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Math', 'operation', operation, 'vector_math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'))
        node = Node('Vector Math', {'Vector': vector, 'Vector_001': vector_1, 'Vector_002': vector_2, 'Scale': scale}, operation=operation)
        return node._out

    @classmethod
    def vector_rotate(cls,
                    vector: Vector = None,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    rotation: Vector = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE'):
        """ > Node <&ShaderNode Vector Rotate>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        center : Vector, optional
            socket 'Center' (id: Center)
        
        axis : Vector, optional
            socket 'Axis' (id: Axis)
        
        angle : Float, optional
            socket 'Angle' (id: Angle)
        
        rotation : Vector, optional
            socket 'Rotation' (id: Rotation)
        
        invert : bool
            parameter `invert`
        
        rotation_type : Literal['Axis Angle', 'X Axis', 'Y Axis', 'Z Axis', 'Euler']
            parameter `rotation_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Rotate', 'rotation_type', rotation_type, 'vector_rotate', ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'))
        node = Node('Vector Rotate', {'Vector': vector, 'Center': center, 'Axis': axis, 'Angle': angle, 'Rotation': rotation}, invert=invert, rotation_type=rotation_type)
        return node._out

    @classmethod
    def vector_transform(cls,
                    vector: Vector = None,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR'):
        """ > Node <&ShaderNode Vector Transform>

        Parameters
        ----------
        vector : Vector, optional
            socket 'Vector' (id: Vector)
        
        convert_from : Literal['World', 'Object', 'Camera']
            parameter `convert_from`
        
        convert_to : Literal['World', 'Object', 'Camera']
            parameter `convert_to`
        
        vector_type : Literal['Point', 'Vector', 'Normal']
            parameter `vector_type`
        

        Returns
        -------
        Vector
        """
        utils.check_enum_arg('Vector Transform', 'convert_from', convert_from, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'convert_to', convert_to, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'vector_type', vector_type, 'vector_transform', ('POINT', 'VECTOR', 'NORMAL'))
        node = Node('Vector Transform', {'Vector': vector}, convert_from=convert_from, convert_to=convert_to, vector_type=vector_type)
        return node._out

    @classmethod
    def color_attribute(cls, layer_name = ''):
        """ > Node <&ShaderNode Color Attribute>

        Parameters
        ----------
        layer_name : str
            parameter `layer_name`
        

        Returns
        -------
        Color
            peer sockets: alpha_ (Float)

        """
        node = Node('Color Attribute', layer_name=layer_name)
        return node

    @classmethod
    def volume_absorption(cls, color: Color = None, density: Float = None, weight: Float = None):
        """ > Node <&ShaderNode Volume Absorption>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        density : Float, optional
            socket 'Density' (id: Density)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        VolumeShader
        """
        node = Node('Volume Absorption', {'Color': color, 'Density': density, 'Weight': weight})
        return node._out

    @classmethod
    def volume_coefficients(cls,
                    weight: Float = None,
                    absorption_coefficients: Vector = None,
                    scatter_coefficients: Vector = None,
                    anisotropy: Float = None,
                    ior: Float = None,
                    backscatter: Float = None,
                    alpha: Float = None,
                    diameter: Float = None,
                    emission_coefficients: Vector = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN'):
        """ > Node <&ShaderNode Volume Coefficients>

        Parameters
        ----------
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        absorption_coefficients : Vector, optional
            socket 'Absorption Coefficients' (id: Absorption Coefficients)
        
        scatter_coefficients : Vector, optional
            socket 'Scatter Coefficients' (id: Scatter Coefficients)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        backscatter : Float, optional
            socket 'Backscatter' (id: Backscatter)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        
        diameter : Float, optional
            socket 'Diameter' (id: Diameter)
        
        emission_coefficients : Vector, optional
            socket 'Emission Coefficients' (id: Emission Coefficients)
        
        phase : Literal['Henyey-Greenstein', 'Fournier-Forand', 'Draine', 'Rayleigh', 'Mie']
            parameter `phase`
        

        Returns
        -------
        VolumeShader
        """
        utils.check_enum_arg('Volume Coefficients', 'phase', phase, 'volume_coefficients', ('HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'))
        node = Node('Volume Coefficients', {'Weight': weight, 'Absorption Coefficients': absorption_coefficients, 'Scatter Coefficients': scatter_coefficients, 'Anisotropy': anisotropy, 'IOR': ior, 'Backscatter': backscatter, 'Alpha': alpha, 'Diameter': diameter, 'Emission Coefficients': emission_coefficients}, phase=phase)
        return node._out

    @classmethod
    def volume_info(cls):
        """ > Node <&ShaderNode Volume Info>

        Returns
        -------
        Color
            peer sockets: density_ (Float), flame_ (Float), temperature_ (Float)

        """
        node = Node('Volume Info', )
        return node

    @classmethod
    def principled_volume(cls,
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
                    temperature_attribute: String = None,
                    weight: Float = None):
        """ > Node <&ShaderNode Principled Volume>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        color_attribute : String, optional
            socket 'Color Attribute' (id: Color Attribute)
        
        density : Float, optional
            socket 'Density' (id: Density)
        
        density_attribute : String, optional
            socket 'Density Attribute' (id: Density Attribute)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        absorption_color : Color, optional
            socket 'Absorption Color' (id: Absorption Color)
        
        emission_strength : Float, optional
            socket 'Emission Strength' (id: Emission Strength)
        
        emission_color : Color, optional
            socket 'Emission Color' (id: Emission Color)
        
        blackbody_intensity : Float, optional
            socket 'Blackbody Intensity' (id: Blackbody Intensity)
        
        blackbody_tint : Color, optional
            socket 'Blackbody Tint' (id: Blackbody Tint)
        
        temperature : Float, optional
            socket 'Temperature' (id: Temperature)
        
        temperature_attribute : String, optional
            socket 'Temperature Attribute' (id: Temperature Attribute)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        

        Returns
        -------
        VolumeShader
        """
        node = Node('Principled Volume', {'Color': color, 'Color Attribute': color_attribute, 'Density': density, 'Density Attribute': density_attribute, 'Anisotropy': anisotropy, 'Absorption Color': absorption_color, 'Emission Strength': emission_strength, 'Emission Color': emission_color, 'Blackbody Intensity': blackbody_intensity, 'Blackbody Tint': blackbody_tint, 'Temperature': temperature, 'Temperature Attribute': temperature_attribute, 'Weight': weight})
        return node._out

    @classmethod
    def volume_scatter(cls,
                    color: Color = None,
                    density: Float = None,
                    anisotropy: Float = None,
                    ior: Float = None,
                    backscatter: Float = None,
                    alpha: Float = None,
                    diameter: Float = None,
                    weight: Float = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN'):
        """ > Node <&ShaderNode Volume Scatter>

        Parameters
        ----------
        color : Color, optional
            socket 'Color' (id: Color)
        
        density : Float, optional
            socket 'Density' (id: Density)
        
        anisotropy : Float, optional
            socket 'Anisotropy' (id: Anisotropy)
        
        ior : Float, optional
            socket 'IOR' (id: IOR)
        
        backscatter : Float, optional
            socket 'Backscatter' (id: Backscatter)
        
        alpha : Float, optional
            socket 'Alpha' (id: Alpha)
        
        diameter : Float, optional
            socket 'Diameter' (id: Diameter)
        
        weight : Float, optional
            socket 'Weight' (id: Weight)
        
        phase : Literal['Henyey-Greenstein', 'Fournier-Forand', 'Draine', 'Rayleigh', 'Mie']
            parameter `phase`
        

        Returns
        -------
        VolumeShader
        """
        utils.check_enum_arg('Volume Scatter', 'phase', phase, 'volume_scatter', ('HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'))
        node = Node('Volume Scatter', {'Color': color, 'Density': density, 'Anisotropy': anisotropy, 'IOR': ior, 'Backscatter': backscatter, 'Alpha': alpha, 'Diameter': diameter, 'Weight': weight}, phase=phase)
        return node._out

    @classmethod
    def wavelength(cls, wavelength: Float = None):
        """ > Node <&ShaderNode Wavelength>

        Parameters
        ----------
        wavelength : Float, optional
            socket 'Wavelength' (id: Wavelength)
        

        Returns
        -------
        Color
        """
        node = Node('Wavelength', {'Wavelength': wavelength})
        return node._out

    @classmethod
    def wireframe(cls, size: Float = None, use_pixel_size = False):
        """ > Node <&ShaderNode Wireframe>

        Parameters
        ----------
        size : Float, optional
            socket 'Size' (id: Size)
        
        use_pixel_size : bool
            parameter `use_pixel_size`
        

        Returns
        -------
        Float
        """
        node = Node('Wireframe', {'Size': size}, use_pixel_size=use_pixel_size)
        return node._out




# Create one single instance to access properties

snd = SND()

