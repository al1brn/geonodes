from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class snd:
    """" Static class

    Exposes all nodes as static methods:

    ``` python
    a = snd.math(1, 2, operation='ADD')
    ```
    """

    @classmethod
    def frame(cls, label_size=20, shrink=True, text=None):
        """ > Node <&ShaderNode Frame>

        Arguments
        ---------
        - label_size (int): parameter 'label_size'
        - shrink (bool): parameter 'shrink'
        - text (NoneType): parameter 'text'

        Returns
        -------
        - None
        """
        node = Node('Frame', sockets={}, label_size=label_size, shrink=shrink, text=text)
        return node._out

    @classmethod
    @property
    def group_input(cls):
        """ > Node <&ShaderNode Group Input>

        Returns
        -------
        - None
        """
        node = Node('Group Input', sockets={})
        return node._out

    @classmethod
    def group_output(cls, is_active_output=True):
        """ > Node <&ShaderNode Group Output>

        Arguments
        ---------
        - is_active_output (bool): parameter 'is_active_output'

        Returns
        -------
        - None
        """
        node = Node('Group Output', sockets={}, is_active_output=is_active_output)
        return node._out

    @classmethod
    def reroute(cls, input=None, socket_idname='NodeSocketColor'):
        """ > Node <&ShaderNode Reroute>

        Arguments
        ---------
        - input (Color) : socket 'Input' (id: Input)
        - socket_idname (str): parameter 'socket_idname'

        Returns
        -------
        - Color
        """
        node = Node('Reroute', sockets={'Input': input}, socket_idname=socket_idname)
        return node._out

    @classmethod
    def add_shader(cls, shader=None, shader_1=None):
        """ > Node <&ShaderNode Add Shader>

        Arguments
        ---------
        - shader (Shader) : socket 'Shader' (id: Shader)
        - shader_1 (Shader) : socket 'Shader' (id: Shader_001)

        Returns
        -------
        - Shader
        """
        node = Node('Add Shader', sockets={'Shader': shader, 'Shader_001': shader_1})
        return node._out

    @classmethod
    def ambient_occlusion(cls, color=None, distance=None, normal=None, inside=False, only_local=False, samples=16):
        """ > Node <&ShaderNode Ambient Occlusion>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - distance (Float) : socket 'Distance' (id: Distance)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - inside (bool): parameter 'inside'
        - only_local (bool): parameter 'only_local'
        - samples (int): parameter 'samples'

        Returns
        -------
        - Color [ao_ (Float)]
        """
        node = Node('Ambient Occlusion', sockets={'Color': color, 'Distance': distance, 'Normal': normal}, inside=inside, only_local=only_local, samples=samples)
        return node._out

    @classmethod
    def attribute(cls, attribute_name='', attribute_type='GEOMETRY'):
        """ > Node <&ShaderNode Attribute>

        Arguments
        ---------
        - attribute_name (str): parameter 'attribute_name'
        - attribute_type (str): parameter 'attribute_type' in ['GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER']

        Returns
        -------
        - Color [vector_ (Vector), fac_ (Float), alpha_ (Float)]
        """
        utils.check_enum_arg('Attribute', 'attribute_type', attribute_type, 'attribute', ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER'))
        node = Node('Attribute', sockets={}, attribute_name=attribute_name, attribute_type=attribute_type)
        return node

    @classmethod
    def background(cls, color=None, strength=None, weight=None):
        """ > Node <&ShaderNode Background>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - strength (Float) : socket 'Strength' (id: Strength)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Background', sockets={'Color': color, 'Strength': strength, 'Weight': weight})
        return node._out

    @classmethod
    def bevel(cls, radius=None, normal=None, samples=4):
        """ > Node <&ShaderNode Bevel>

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - samples (int): parameter 'samples'

        Returns
        -------
        - Vector
        """
        node = Node('Bevel', sockets={'Radius': radius, 'Normal': normal}, samples=samples)
        return node._out

    @classmethod
    def blackbody(cls, temperature=None):
        """ > Node <&ShaderNode Blackbody>

        Arguments
        ---------
        - temperature (Float) : socket 'Temperature' (id: Temperature)

        Returns
        -------
        - Color
        """
        node = Node('Blackbody', sockets={'Temperature': temperature})
        return node._out

    @classmethod
    def brightness_contrast(cls, color=None, bright=None, contrast=None):
        """ > Node <&ShaderNode Brightness/Contrast>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - bright (Float) : socket 'Bright' (id: Bright)
        - contrast (Float) : socket 'Contrast' (id: Contrast)

        Returns
        -------
        - Color
        """
        node = Node('Brightness/Contrast', sockets={'Color': color, 'Bright': bright, 'Contrast': contrast})
        return node._out

    @classmethod
    def glossy_bsdf(cls, color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, weight=None, distribution='MULTI_GGX'):
        """ > Node <&ShaderNode Glossy BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - rotation (Float) : socket 'Rotation' (id: Rotation)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - weight (Float) : socket 'Weight' (id: Weight)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Glossy BSDF', 'distribution', distribution, 'glossy_bsdf', ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'))
        node = Node('Glossy BSDF', sockets={'Color': color, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def diffuse_bsdf(cls, color=None, roughness=None, normal=None, weight=None):
        """ > Node <&ShaderNode Diffuse BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Diffuse BSDF', sockets={'Color': color, 'Roughness': roughness, 'Normal': normal, 'Weight': weight})
        return node._out

    @classmethod
    def glass_bsdf(cls, color=None, roughness=None, ior=None, normal=None, weight=None, distribution='MULTI_GGX'):
        """ > Node <&ShaderNode Glass BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX', 'MULTI_GGX']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Glass BSDF', 'distribution', distribution, 'glass_bsdf', ('BECKMANN', 'GGX', 'MULTI_GGX'))
        node = Node('Glass BSDF', sockets={'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def hair_bsdf(cls, color=None, offset=None, roughnessu=None, roughnessv=None, tangent=None, weight=None, component='Reflection'):
        """ > Node <&ShaderNode Hair BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - offset (Float) : socket 'Offset' (id: Offset)
        - roughnessu (Float) : socket 'RoughnessU' (id: RoughnessU)
        - roughnessv (Float) : socket 'RoughnessV' (id: RoughnessV)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - weight (Float) : socket 'Weight' (id: Weight)
        - component (str): parameter 'component' in ['Reflection', 'Transmission']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Hair BSDF', 'component', component, 'hair_bsdf', ('Reflection', 'Transmission'))
        node = Node('Hair BSDF', sockets={'Color': color, 'Offset': offset, 'RoughnessU': roughnessu, 'RoughnessV': roughnessv, 'Tangent': tangent, 'Weight': weight}, component=component)
        return node._out

    @classmethod
    def principled_hair_bsdf(cls, color=None, melanin=None, melanin_redness=None, tint=None, absorption_coefficient=None, aspect_ratio=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_color=None, random_roughness=None, random=None, weight=None, reflection=None, transmission=None, secondary_reflection=None, model='CHIANG', parametrization='COLOR'):
        """ > Node <&ShaderNode Principled Hair BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - melanin (Float) : socket 'Melanin' (id: Melanin)
        - melanin_redness (Float) : socket 'Melanin Redness' (id: Melanin Redness)
        - tint (Color) : socket 'Tint' (id: Tint)
        - absorption_coefficient (Vector) : socket 'Absorption Coefficient' (id: Absorption Coefficient)
        - aspect_ratio (Float) : socket 'Aspect Ratio' (id: Aspect Ratio)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - radial_roughness (Float) : socket 'Radial Roughness' (id: Radial Roughness)
        - coat (Float) : socket 'Coat' (id: Coat)
        - ior (Float) : socket 'IOR' (id: IOR)
        - offset (Float) : socket 'Offset' (id: Offset)
        - random_color (Float) : socket 'Random Color' (id: Random Color)
        - random_roughness (Float) : socket 'Random Roughness' (id: Random Roughness)
        - random (Float) : socket 'Random' (id: Random)
        - weight (Float) : socket 'Weight' (id: Weight)
        - reflection (Float) : socket 'Reflection' (id: R lobe)
        - transmission (Float) : socket 'Transmission' (id: TT lobe)
        - secondary_reflection (Float) : socket 'Secondary Reflection' (id: TRT lobe)
        - model (str): parameter 'model' in ['CHIANG', 'HUANG']
        - parametrization (str): parameter 'parametrization' in ['ABSORPTION', 'MELANIN', 'COLOR']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Principled Hair BSDF', 'model', model, 'principled_hair_bsdf', ('CHIANG', 'HUANG'))
        utils.check_enum_arg('Principled Hair BSDF', 'parametrization', parametrization, 'principled_hair_bsdf', ('ABSORPTION', 'MELANIN', 'COLOR'))
        node = Node('Principled Hair BSDF', sockets={'Color': color, 'Melanin': melanin, 'Melanin Redness': melanin_redness, 'Tint': tint, 'Absorption Coefficient': absorption_coefficient, 'Aspect Ratio': aspect_ratio, 'Roughness': roughness, 'Radial Roughness': radial_roughness, 'Coat': coat, 'IOR': ior, 'Offset': offset, 'Random Color': random_color, 'Random Roughness': random_roughness, 'Random': random, 'Weight': weight, 'R lobe': reflection, 'TT lobe': transmission, 'TRT lobe': secondary_reflection}, model=model, parametrization=parametrization)
        return node._out

    @classmethod
    def metallic_bsdf(cls, base_color=None, edge_tint=None, ior=None, extinction=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, weight=None, distribution='MULTI_GGX', fresnel_type='F82'):
        """ > Node <&ShaderNode Metallic BSDF>

        Arguments
        ---------
        - base_color (Color) : socket 'Base Color' (id: Base Color)
        - edge_tint (Color) : socket 'Edge Tint' (id: Edge Tint)
        - ior (Vector) : socket 'IOR' (id: IOR)
        - extinction (Vector) : socket 'Extinction' (id: Extinction)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - rotation (Float) : socket 'Rotation' (id: Rotation)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - weight (Float) : socket 'Weight' (id: Weight)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX', 'MULTI_GGX']
        - fresnel_type (str): parameter 'fresnel_type' in ['PHYSICAL_CONDUCTOR', 'F82']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Metallic BSDF', 'distribution', distribution, 'metallic_bsdf', ('BECKMANN', 'GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Metallic BSDF', 'fresnel_type', fresnel_type, 'metallic_bsdf', ('PHYSICAL_CONDUCTOR', 'F82'))
        node = Node('Metallic BSDF', sockets={'Base Color': base_color, 'Edge Tint': edge_tint, 'IOR': ior, 'Extinction': extinction, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent, 'Weight': weight}, distribution=distribution, fresnel_type=fresnel_type)
        return node._out

    @classmethod
    def principled_bsdf(cls, base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, weight=None, diffuse_roughness=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_ior=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, thin_film_thickness=None, thin_film_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK'):
        """ > Node <&ShaderNode Principled BSDF>

        Arguments
        ---------
        - base_color (Color) : socket 'Base Color' (id: Base Color)
        - metallic (Float) : socket 'Metallic' (id: Metallic)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - alpha (Float) : socket 'Alpha' (id: Alpha)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)
        - diffuse_roughness (Float) : socket 'Diffuse Roughness' (id: Diffuse Roughness)
        - subsurface_weight (Float) : socket 'Subsurface Weight' (id: Subsurface Weight)
        - subsurface_radius (Vector) : socket 'Subsurface Radius' (id: Subsurface Radius)
        - subsurface_scale (Float) : socket 'Subsurface Scale' (id: Subsurface Scale)
        - subsurface_ior (Float) : socket 'Subsurface IOR' (id: Subsurface IOR)
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
        utils.check_enum_arg('Principled BSDF', 'distribution', distribution, 'principled_bsdf', ('GGX', 'MULTI_GGX'))
        utils.check_enum_arg('Principled BSDF', 'subsurface_method', subsurface_method, 'principled_bsdf', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Principled BSDF', sockets={'Base Color': base_color, 'Metallic': metallic, 'Roughness': roughness, 'IOR': ior, 'Alpha': alpha, 'Normal': normal, 'Weight': weight, 'Diffuse Roughness': diffuse_roughness, 'Subsurface Weight': subsurface_weight, 'Subsurface Radius': subsurface_radius, 'Subsurface Scale': subsurface_scale, 'Subsurface IOR': subsurface_ior, 'Subsurface Anisotropy': subsurface_anisotropy, 'Specular IOR Level': specular_ior_level, 'Specular Tint': specular_tint, 'Anisotropic': anisotropic, 'Anisotropic Rotation': anisotropic_rotation, 'Tangent': tangent, 'Transmission Weight': transmission_weight, 'Coat Weight': coat_weight, 'Coat Roughness': coat_roughness, 'Coat IOR': coat_ior, 'Coat Tint': coat_tint, 'Coat Normal': coat_normal, 'Sheen Weight': sheen_weight, 'Sheen Roughness': sheen_roughness, 'Sheen Tint': sheen_tint, 'Emission Color': emission_color, 'Emission Strength': emission_strength, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, subsurface_method=subsurface_method)
        return node._out

    @classmethod
    def ray_portal_bsdf(cls, color=None, position=None, direction=None, weight=None):
        """ > Node <&ShaderNode Ray Portal BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - position (Vector) : socket 'Position' (id: Position)
        - direction (Vector) : socket 'Direction' (id: Direction)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Ray Portal BSDF', sockets={'Color': color, 'Position': position, 'Direction': direction, 'Weight': weight})
        return node._out

    @classmethod
    def refraction_bsdf(cls, color=None, roughness=None, ior=None, normal=None, weight=None, distribution='BECKMANN'):
        """ > Node <&ShaderNode Refraction BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)
        - distribution (str): parameter 'distribution' in ['BECKMANN', 'GGX']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Refraction BSDF', 'distribution', distribution, 'refraction_bsdf', ('BECKMANN', 'GGX'))
        node = Node('Refraction BSDF', sockets={'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def sheen_bsdf(cls, color=None, roughness=None, normal=None, weight=None, distribution='MICROFIBER'):
        """ > Node <&ShaderNode Sheen BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)
        - distribution (str): parameter 'distribution' in ['ASHIKHMIN', 'MICROFIBER']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Sheen BSDF', 'distribution', distribution, 'sheen_bsdf', ('ASHIKHMIN', 'MICROFIBER'))
        node = Node('Sheen BSDF', sockets={'Color': color, 'Roughness': roughness, 'Normal': normal, 'Weight': weight}, distribution=distribution)
        return node._out

    @classmethod
    def toon_bsdf(cls, color=None, size=None, smooth=None, normal=None, weight=None, component='DIFFUSE'):
        """ > Node <&ShaderNode Toon BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - size (Float) : socket 'Size' (id: Size)
        - smooth (Float) : socket 'Smooth' (id: Smooth)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)
        - component (str): parameter 'component' in ['DIFFUSE', 'GLOSSY']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Toon BSDF', 'component', component, 'toon_bsdf', ('DIFFUSE', 'GLOSSY'))
        node = Node('Toon BSDF', sockets={'Color': color, 'Size': size, 'Smooth': smooth, 'Normal': normal, 'Weight': weight}, component=component)
        return node._out

    @classmethod
    def translucent_bsdf(cls, color=None, normal=None, weight=None):
        """ > Node <&ShaderNode Translucent BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Translucent BSDF', sockets={'Color': color, 'Normal': normal, 'Weight': weight})
        return node._out

    @classmethod
    def transparent_bsdf(cls, color=None, weight=None):
        """ > Node <&ShaderNode Transparent BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Transparent BSDF', sockets={'Color': color, 'Weight': weight})
        return node._out

    @classmethod
    def bump(cls, strength=None, distance=None, height=None, normal=None, invert=False):
        """ > Node <&ShaderNode Bump>

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - distance (Float) : socket 'Distance' (id: Distance)
        - height (Float) : socket 'Height' (id: Height)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - invert (bool): parameter 'invert'

        Returns
        -------
        - Vector
        """
        node = Node('Bump', sockets={'Strength': strength, 'Distance': distance, 'Height': height, 'Normal': normal}, invert=invert)
        return node._out

    @classmethod
    def camera_data(cls):
        """ > Node <&ShaderNode Camera Data>

        Returns
        -------
        - Vector [view_z_depth_ (Float), view_distance_ (Float)]
        """
        node = Node('Camera Data', sockets={})
        return node

    @classmethod
    def clamp(cls, value=None, min=None, max=None, clamp_type='MINMAX'):
        """ > Node <&ShaderNode Clamp>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - min (Float) : socket 'Min' (id: Min)
        - max (Float) : socket 'Max' (id: Max)
        - clamp_type (str): parameter 'clamp_type' in ['MINMAX', 'RANGE']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Clamp', 'clamp_type', clamp_type, 'clamp', ('MINMAX', 'RANGE'))
        node = Node('Clamp', sockets={'Value': value, 'Min': min, 'Max': max}, clamp_type=clamp_type)
        return node._out

    @classmethod
    def combine_color(cls, red=None, green=None, blue=None, mode='RGB'):
        """ > Node <&ShaderNode Combine Color>

        Arguments
        ---------
        - red (Float) : socket 'Red' (id: Red)
        - green (Float) : socket 'Green' (id: Green)
        - blue (Float) : socket 'Blue' (id: Blue)
        - mode (str): parameter 'mode' in ['RGB', 'HSV', 'HSL']

        Returns
        -------
        - Color
        """
        utils.check_enum_arg('Combine Color', 'mode', mode, 'combine_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Combine Color', sockets={'Red': red, 'Green': green, 'Blue': blue}, mode=mode)
        return node._out

    @classmethod
    def combine_xyz(cls, x=None, y=None, z=None):
        """ > Node <&ShaderNode Combine XYZ>

        Arguments
        ---------
        - x (Float) : socket 'X' (id: X)
        - y (Float) : socket 'Y' (id: Y)
        - z (Float) : socket 'Z' (id: Z)

        Returns
        -------
        - Vector
        """
        node = Node('Combine XYZ', sockets={'X': x, 'Y': y, 'Z': z})
        return node._out

    @classmethod
    def displacement(cls, height=None, midlevel=None, scale=None, normal=None, space='OBJECT'):
        """ > Node <&ShaderNode Displacement>

        Arguments
        ---------
        - height (Float) : socket 'Height' (id: Height)
        - midlevel (Float) : socket 'Midlevel' (id: Midlevel)
        - scale (Float) : socket 'Scale' (id: Scale)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - space (str): parameter 'space' in ['OBJECT', 'WORLD']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Displacement', 'space', space, 'displacement', ('OBJECT', 'WORLD'))
        node = Node('Displacement', sockets={'Height': height, 'Midlevel': midlevel, 'Scale': scale, 'Normal': normal}, space=space)
        return node._out

    @classmethod
    def specular_bsdf(cls, base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None, weight=None):
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
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Specular BSDF', sockets={'Base Color': base_color, 'Specular': specular, 'Roughness': roughness, 'Emissive Color': emissive_color, 'Transparency': transparency, 'Normal': normal, 'Clear Coat': clear_coat, 'Clear Coat Roughness': clear_coat_roughness, 'Clear Coat Normal': clear_coat_normal, 'Weight': weight})
        return node._out

    @classmethod
    def emission(cls, color=None, strength=None, weight=None):
        """ > Node <&ShaderNode Emission>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - strength (Float) : socket 'Strength' (id: Strength)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Emission', sockets={'Color': color, 'Strength': strength, 'Weight': weight})
        return node._out

    @classmethod
    def float_curve(cls, value=None, factor=None):
        """ > Node <&ShaderNode Float Curve>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - factor (Float) : socket 'Factor' (id: Factor)

        Returns
        -------
        - Float
        """
        node = NodeCurves('Float Curve', sockets={'Value': value, 'Factor': factor})
        return node._out

    @classmethod
    def fresnel(cls, ior=None, normal=None):
        """ > Node <&ShaderNode Fresnel>

        Arguments
        ---------
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Float
        """
        node = Node('Fresnel', sockets={'IOR': ior, 'Normal': normal})
        return node._out

    @classmethod
    def gamma(cls, color=None, gamma=None):
        """ > Node <&ShaderNode Gamma>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - gamma (Float) : socket 'Gamma' (id: Gamma)

        Returns
        -------
        - Color
        """
        node = Node('Gamma', sockets={'Color': color, 'Gamma': gamma})
        return node._out

    @classmethod
    def group(cls, node_tree=None):
        """ > Node <&ShaderNode Group>

        Arguments
        ---------
        - node_tree (NoneType): parameter 'node_tree'

        Returns
        -------
        - None
        """
        node = Node('Group', sockets={}, node_tree=node_tree)
        return node._out

    @classmethod
    def curves_info(cls):
        """ > Node <&ShaderNode Curves Info>

        Returns
        -------
        - Float [intercept_ (Float), length_ (Float), thickness_ (Float), tangent_normal_ (Vector), random_ (Float)]
        """
        node = Node('Curves Info', sockets={})
        return node

    @classmethod
    def holdout(cls, weight=None):
        """ > Node <&ShaderNode Holdout>

        Arguments
        ---------
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Shader
        """
        node = Node('Holdout', sockets={'Weight': weight})
        return node._out

    @classmethod
    def hue_saturation_value(cls, hue=None, saturation=None, value=None, color=None, fac=None):
        """ > Node <&ShaderNode Hue/Saturation/Value>

        Arguments
        ---------
        - hue (Float) : socket 'Hue' (id: Hue)
        - saturation (Float) : socket 'Saturation' (id: Saturation)
        - value (Float) : socket 'Value' (id: Value)
        - color (Color) : socket 'Color' (id: Color)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Color
        """
        node = Node('Hue/Saturation/Value', sockets={'Hue': hue, 'Saturation': saturation, 'Value': value, 'Color': color, 'Fac': fac})
        return node._out

    @classmethod
    def invert_color(cls, color=None, fac=None):
        """ > Node <&ShaderNode Invert Color>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Color
        """
        node = Node('Invert Color', sockets={'Color': color, 'Fac': fac})
        return node._out

    @classmethod
    def layer_weight(cls, blend=None, normal=None):
        """ > Node <&ShaderNode Layer Weight>

        Arguments
        ---------
        - blend (Float) : socket 'Blend' (id: Blend)
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Float [facing_ (Float)]
        """
        node = Node('Layer Weight', sockets={'Blend': blend, 'Normal': normal})
        return node._out

    @classmethod
    def light_falloff(cls, strength=None, smooth=None):
        """ > Node <&ShaderNode Light Falloff>

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - smooth (Float) : socket 'Smooth' (id: Smooth)

        Returns
        -------
        - Float [linear_ (Float), constant_ (Float)]
        """
        node = Node('Light Falloff', sockets={'Strength': strength, 'Smooth': smooth})
        return node._out

    @classmethod
    def light_path(cls):
        """ > Node <&ShaderNode Light Path>

        Returns
        -------
        - Float [is_shadow_ray_ (Float), is_diffuse_ray_ (Float), is_glossy_ray_ (Float), is_singular_ray_ (Float), is_reflection_ray_ (Float), is_transmission_ray_ (Float), ray_length_ (Float), ray_depth_ (Float), diffuse_depth_ (Float), glossy_depth_ (Float), transparent_depth_ (Float), transmission_depth_ (Float)]
        """
        node = Node('Light Path', sockets={})
        return node

    @classmethod
    def map_range(cls, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, from_min_1=None, from_max_1=None, to_min_1=None, to_max_1=None, steps_1=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR'):
        """ > Node <&ShaderNode Map Range>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - from_min (Float) : socket 'From Min' (id: From Min)
        - from_max (Float) : socket 'From Max' (id: From Max)
        - to_min (Float) : socket 'To Min' (id: To Min)
        - to_max (Float) : socket 'To Max' (id: To Max)
        - steps (Float) : socket 'Steps' (id: Steps)
        - vector (Vector) : socket 'Vector' (id: Vector)
        - from_min_1 (Vector) : socket 'From Min' (id: From_Min_FLOAT3)
        - from_max_1 (Vector) : socket 'From Max' (id: From_Max_FLOAT3)
        - to_min_1 (Vector) : socket 'To Min' (id: To_Min_FLOAT3)
        - to_max_1 (Vector) : socket 'To Max' (id: To_Max_FLOAT3)
        - steps_1 (Vector) : socket 'Steps' (id: Steps_FLOAT3)
        - clamp (bool): parameter 'clamp'
        - data_type (str): parameter 'data_type' in ['FLOAT', 'FLOAT_VECTOR']
        - interpolation_type (str): parameter 'interpolation_type' in ['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Map Range', 'data_type', data_type, 'map_range', ('FLOAT', 'FLOAT_VECTOR'))
        utils.check_enum_arg('Map Range', 'interpolation_type', interpolation_type, 'map_range', ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'))
        node = Node('Map Range', sockets={'Value': value, 'From Min': from_min, 'From Max': from_max, 'To Min': to_min, 'To Max': to_max, 'Steps': steps, 'Vector': vector, 'From_Min_FLOAT3': from_min_1, 'From_Max_FLOAT3': from_max_1, 'To_Min_FLOAT3': to_min_1, 'To_Max_FLOAT3': to_max_1, 'Steps_FLOAT3': steps_1}, clamp=clamp, data_type=data_type, interpolation_type=interpolation_type)
        return node._out

    @classmethod
    def mapping(cls, vector=None, location=None, rotation=None, scale=None, vector_type='POINT'):
        """ > Node <&ShaderNode Mapping>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - location (Vector) : socket 'Location' (id: Location)
        - rotation (Vector) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - vector_type (str): parameter 'vector_type' in ['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Mapping', 'vector_type', vector_type, 'mapping', ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL'))
        node = Node('Mapping', sockets={'Vector': vector, 'Location': location, 'Rotation': rotation, 'Scale': scale}, vector_type=vector_type)
        return node._out

    @classmethod
    def math(cls, value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False):
        """ > Node <&ShaderNode Math>

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - value_1 (Float) : socket 'Value' (id: Value_001)
        - value_2 (Float) : socket 'Value' (id: Value_002)
        - operation (str): parameter 'operation' in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES']
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Math', 'operation', operation, 'math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'))
        node = Node('Math', sockets={'Value': value, 'Value_001': value_1, 'Value_002': value_2}, operation=operation, use_clamp=use_clamp)
        return node._out

    @classmethod
    def mix(cls, a=None, b=None, a_1=None, b_1=None, a_2=None, b_2=None, a_3=None, b_3=None, factor=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM'):
        """ > Node <&ShaderNode Mix>

        Arguments
        ---------
        - a (Float) : socket 'A' (id: A_Float)
        - b (Float) : socket 'B' (id: B_Float)
        - a_1 (Vector) : socket 'A' (id: A_Vector)
        - b_1 (Vector) : socket 'B' (id: B_Vector)
        - a_2 (Color) : socket 'A' (id: A_Color)
        - b_2 (Color) : socket 'B' (id: B_Color)
        - a_3 (Rotation) : socket 'A' (id: A_Rotation)
        - b_3 (Rotation) : socket 'B' (id: B_Rotation)
        - factor (Vector) : socket 'Factor' (id: Factor_Vector)
        - blend_type (str): parameter 'blend_type' in ['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']
        - clamp_factor (bool): parameter 'clamp_factor'
        - clamp_result (bool): parameter 'clamp_result'
        - data_type (str): parameter 'data_type' in ['FLOAT', 'VECTOR', 'RGBA']
        - factor_mode (str): parameter 'factor_mode' in ['UNIFORM', 'NON_UNIFORM']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('Mix', 'blend_type', blend_type, 'mix', ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'))
        utils.check_enum_arg('Mix', 'data_type', data_type, 'mix', ('FLOAT', 'VECTOR', 'RGBA'))
        utils.check_enum_arg('Mix', 'factor_mode', factor_mode, 'mix', ('UNIFORM', 'NON_UNIFORM'))
        node = Node('Mix', sockets={'A_Float': a, 'B_Float': b, 'A_Vector': a_1, 'B_Vector': b_1, 'A_Color': a_2, 'B_Color': b_2, 'A_Rotation': a_3, 'B_Rotation': b_3, 'Factor_Vector': factor}, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type=data_type, factor_mode=factor_mode)
        return node._out

    @classmethod
    def mix_shader(cls, shader=None, shader_1=None, fac=None):
        """ > Node <&ShaderNode Mix Shader>

        Arguments
        ---------
        - shader (Shader) : socket 'Shader' (id: Shader)
        - shader_1 (Shader) : socket 'Shader' (id: Shader_001)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Shader
        """
        node = Node('Mix Shader', sockets={'Shader': shader, 'Shader_001': shader_1, 'Fac': fac})
        return node._out

    @classmethod
    def geometry(cls):
        """ > Node <&ShaderNode Geometry>

        Returns
        -------
        - Vector [normal_ (Vector), tangent_ (Vector), true_normal_ (Vector), incoming_ (Vector), parametric_ (Vector), backfacing_ (Float), pointiness_ (Float), random_per_island_ (Float)]
        """
        node = Node('Geometry', sockets={})
        return node

    @classmethod
    def normal(cls, normal=None):
        """ > Node <&ShaderNode Normal>

        Arguments
        ---------
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Vector [dot_ (Float)]
        """
        node = Node('Normal', sockets={'Normal': normal})
        return node._out

    @classmethod
    def normal_map(cls, strength=None, color=None, space='TANGENT', uv_map=''):
        """ > Node <&ShaderNode Normal Map>

        Arguments
        ---------
        - strength (Float) : socket 'Strength' (id: Strength)
        - color (Color) : socket 'Color' (id: Color)
        - space (str): parameter 'space' in ['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD']
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Normal Map', 'space', space, 'normal_map', ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'))
        node = Node('Normal Map', sockets={'Strength': strength, 'Color': color}, space=space, uv_map=uv_map)
        return node._out

    @classmethod
    def object_info(cls):
        """ > Node <&ShaderNode Object Info>

        Returns
        -------
        - Vector [color_ (Color), alpha_ (Float), object_index_ (Float), material_index_ (Float), random_ (Float)]
        """
        node = Node('Object Info', sockets={})
        return node

    @classmethod
    def aov_output(cls, color=None, value=None, aov_name=''):
        """ > Node <&ShaderNode AOV Output>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - value (Float) : socket 'Value' (id: Value)
        - aov_name (str): parameter 'aov_name'

        Returns
        -------
        - None
        """
        node = Node('AOV Output', sockets={'Color': color, 'Value': value}, aov_name=aov_name)
        return node._out

    @classmethod
    def light_output(cls, surface=None, is_active_output=True, target='ALL'):
        """ > Node <&ShaderNode Light Output>

        Arguments
        ---------
        - surface (Shader) : socket 'Surface' (id: Surface)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Light Output', 'target', target, 'light_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Light Output', sockets={'Surface': surface}, is_active_output=is_active_output, target=target)
        return node._out

    @classmethod
    def line_style_output(cls, color=None, color_fac=None, alpha=None, alpha_fac=None, blend_type='MIX', is_active_output=True, target='ALL', use_alpha=False, use_clamp=False):
        """ > Node <&ShaderNode Line Style Output>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - color_fac (Float) : socket 'Color Fac' (id: Color Fac)
        - alpha (Float) : socket 'Alpha' (id: Alpha)
        - alpha_fac (Float) : socket 'Alpha Fac' (id: Alpha Fac)
        - blend_type (str): parameter 'blend_type' in ['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']
        - use_alpha (bool): parameter 'use_alpha'
        - use_clamp (bool): parameter 'use_clamp'

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Line Style Output', 'blend_type', blend_type, 'line_style_output', ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'))
        utils.check_enum_arg('Line Style Output', 'target', target, 'line_style_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Line Style Output', sockets={'Color': color, 'Color Fac': color_fac, 'Alpha': alpha, 'Alpha Fac': alpha_fac}, blend_type=blend_type, is_active_output=is_active_output, target=target, use_alpha=use_alpha, use_clamp=use_clamp)
        return node._out

    @classmethod
    def material_output(cls, surface=None, volume=None, displacement=None, thickness=None, is_active_output=True, target='ALL'):
        """ > Node <&ShaderNode Material Output>

        Arguments
        ---------
        - surface (Shader) : socket 'Surface' (id: Surface)
        - volume (Shader) : socket 'Volume' (id: Volume)
        - displacement (Vector) : socket 'Displacement' (id: Displacement)
        - thickness (Float) : socket 'Thickness' (id: Thickness)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Material Output', 'target', target, 'material_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('Material Output', sockets={'Surface': surface, 'Volume': volume, 'Displacement': displacement, 'Thickness': thickness}, is_active_output=is_active_output, target=target)
        return node._out

    @classmethod
    def world_output(cls, surface=None, volume=None, is_active_output=True, target='ALL'):
        """ > Node <&ShaderNode World Output>

        Arguments
        ---------
        - surface (Shader) : socket 'Surface' (id: Surface)
        - volume (Shader) : socket 'Volume' (id: Volume)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ['ALL', 'EEVEE', 'CYCLES']

        Returns
        -------
        - None
        """
        utils.check_enum_arg('World Output', 'target', target, 'world_output', ('ALL', 'EEVEE', 'CYCLES'))
        node = Node('World Output', sockets={'Surface': surface, 'Volume': volume}, is_active_output=is_active_output, target=target)
        return node._out

    @classmethod
    def particle_info(cls):
        """ > Node <&ShaderNode Particle Info>

        Returns
        -------
        - Float [random_ (Float), age_ (Float), lifetime_ (Float), location_ (Vector), size_ (Float), velocity_ (Vector), angular_velocity_ (Vector)]
        """
        node = Node('Particle Info', sockets={})
        return node

    @classmethod
    def point_info(cls):
        """ > Node <&ShaderNode Point Info>

        Returns
        -------
        - Vector [radius_ (Float), random_ (Float)]
        """
        node = Node('Point Info', sockets={})
        return node

    @classmethod
    @property
    def rgb(cls):
        """ > Node <&ShaderNode RGB>

        Returns
        -------
        - Color
        """
        node = Node('RGB', sockets={})
        return node._out

    @classmethod
    def rgb_curves(cls, color=None, fac=None):
        """ > Node <&ShaderNode RGB Curves>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Color
        """
        node = NodeCurves('RGB Curves', sockets={'Color': color, 'Fac': fac})
        return node._out

    @classmethod
    def rgb_to_bw(cls, color=None):
        """ > Node <&ShaderNode RGB to BW>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)

        Returns
        -------
        - Float
        """
        node = Node('RGB to BW', sockets={'Color': color})
        return node._out

    @classmethod
    def script(cls, bytecode='', bytecode_hash='', filepath='', mode='INTERNAL', script=None, use_auto_update=False):
        """ > Node <&ShaderNode Script>

        Arguments
        ---------
        - bytecode (str): parameter 'bytecode'
        - bytecode_hash (str): parameter 'bytecode_hash'
        - filepath (str): parameter 'filepath'
        - mode (str): parameter 'mode' in ['INTERNAL', 'EXTERNAL']
        - script (NoneType): parameter 'script'
        - use_auto_update (bool): parameter 'use_auto_update'

        Returns
        -------
        - None
        """
        utils.check_enum_arg('Script', 'mode', mode, 'script', ('INTERNAL', 'EXTERNAL'))
        node = Node('Script', sockets={}, bytecode=bytecode, bytecode_hash=bytecode_hash, filepath=filepath, mode=mode, script=script, use_auto_update=use_auto_update)
        return node._out

    @classmethod
    def separate_color(cls, color=None, mode='RGB'):
        """ > Node <&ShaderNode Separate Color>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - mode (str): parameter 'mode' in ['RGB', 'HSV', 'HSL']

        Returns
        -------
        - Float [green_ (Float), blue_ (Float)]
        """
        utils.check_enum_arg('Separate Color', 'mode', mode, 'separate_color', ('RGB', 'HSV', 'HSL'))
        node = Node('Separate Color', sockets={'Color': color}, mode=mode)
        return node._out

    @classmethod
    def separate_xyz(cls, vector=None):
        """ > Node <&ShaderNode Separate XYZ>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)

        Returns
        -------
        - Float [y_ (Float), z_ (Float)]
        """
        node = Node('Separate XYZ', sockets={'Vector': vector})
        return node._out

    @classmethod
    def shader_to_rgb(cls, shader=None):
        """ > Node <&ShaderNode Shader to RGB>

        Arguments
        ---------
        - shader (Shader) : socket 'Shader' (id: Shader)

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        node = Node('Shader to RGB', sockets={'Shader': shader})
        return node._out

    @classmethod
    def subsurface_scattering(cls, color=None, scale=None, radius=None, ior=None, roughness=None, anisotropy=None, normal=None, weight=None, falloff='RANDOM_WALK'):
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
        - weight (Float) : socket 'Weight' (id: Weight)
        - falloff (str): parameter 'falloff' in ['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN']

        Returns
        -------
        - Shader
        """
        utils.check_enum_arg('Subsurface Scattering', 'falloff', falloff, 'subsurface_scattering', ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'))
        node = Node('Subsurface Scattering', sockets={'Color': color, 'Scale': scale, 'Radius': radius, 'IOR': ior, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Normal': normal, 'Weight': weight}, falloff=falloff)
        return node._out

    @classmethod
    def tangent(cls, axis='Z', direction_type='RADIAL', uv_map=''):
        """ > Node <&ShaderNode Tangent>

        Arguments
        ---------
        - axis (str): parameter 'axis' in ['X', 'Y', 'Z']
        - direction_type (str): parameter 'direction_type' in ['RADIAL', 'UV_MAP']
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Tangent', 'axis', axis, 'tangent', ('X', 'Y', 'Z'))
        utils.check_enum_arg('Tangent', 'direction_type', direction_type, 'tangent', ('RADIAL', 'UV_MAP'))
        node = Node('Tangent', sockets={}, axis=axis, direction_type=direction_type, uv_map=uv_map)
        return node._out

    @classmethod
    def brick_texture(cls, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """ > Node <&ShaderNode Brick Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - mortar (Color) : socket 'Mortar' (id: Mortar)
        - scale (Float) : socket 'Scale' (id: Scale)
        - mortar_size (Float) : socket 'Mortar Size' (id: Mortar Size)
        - mortar_smooth (Float) : socket 'Mortar Smooth' (id: Mortar Smooth)
        - bias (Float) : socket 'Bias' (id: Bias)
        - brick_width (Float) : socket 'Brick Width' (id: Brick Width)
        - row_height (Float) : socket 'Row Height' (id: Row Height)
        - offset (float): parameter 'offset'
        - offset_frequency (int): parameter 'offset_frequency'
        - squash (float): parameter 'squash'
        - squash_frequency (int): parameter 'squash_frequency'

        Returns
        -------
        - Color [fac_ (Float)]
        """
        node = Node('Brick Texture', sockets={'Vector': vector, 'Color1': color1, 'Color2': color2, 'Mortar': mortar, 'Scale': scale, 'Mortar Size': mortar_size, 'Mortar Smooth': mortar_smooth, 'Bias': bias, 'Brick Width': brick_width, 'Row Height': row_height}, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node._out

    @classmethod
    def checker_texture(cls, vector=None, color1=None, color2=None, scale=None):
        """ > Node <&ShaderNode Checker Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - color1 (Color) : socket 'Color1' (id: Color1)
        - color2 (Color) : socket 'Color2' (id: Color2)
        - scale (Float) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Color [fac_ (Float)]
        """
        node = Node('Checker Texture', sockets={'Vector': vector, 'Color1': color1, 'Color2': color2, 'Scale': scale})
        return node._out

    @classmethod
    def texture_coordinate(cls, from_instancer=False, object=None):
        """ > Node <&ShaderNode Texture Coordinate>

        Arguments
        ---------
        - from_instancer (bool): parameter 'from_instancer'
        - object (NoneType): parameter 'object'

        Returns
        -------
        - Vector [normal_ (Vector), uv_ (Vector), object_ (Vector), camera_ (Vector), window_ (Vector), reflection_ (Vector)]
        """
        node = Node('Texture Coordinate', sockets={}, from_instancer=from_instancer, object=object)
        return node

    @classmethod
    def environment_texture(cls, vector=None, image=None, interpolation='Linear', projection='EQUIRECTANGULAR'):
        """ > Node <&ShaderNode Environment Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - image (NoneType): parameter 'image'
        - interpolation (str): parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
        - projection (str): parameter 'projection' in ['EQUIRECTANGULAR', 'MIRROR_BALL']

        Returns
        -------
        - Color
        """
        utils.check_enum_arg('Environment Texture', 'interpolation', interpolation, 'environment_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Environment Texture', 'projection', projection, 'environment_texture', ('EQUIRECTANGULAR', 'MIRROR_BALL'))
        node = Node('Environment Texture', sockets={'Vector': vector}, image=image, interpolation=interpolation, projection=projection)
        return node._out

    @classmethod
    def gabor_texture(cls, vector=None, scale=None, frequency=None, anisotropy=None, orientation=None, orientation_1=None, gabor_type='2D'):
        """ > Node <&ShaderNode Gabor Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - frequency (Float) : socket 'Frequency' (id: Frequency)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - orientation (Float) : socket 'Orientation' (id: Orientation 2D)
        - orientation_1 (Vector) : socket 'Orientation' (id: Orientation 3D)
        - gabor_type (str): parameter 'gabor_type' in ['2D', '3D']

        Returns
        -------
        - Float [phase_ (Float), intensity_ (Float)]
        """
        utils.check_enum_arg('Gabor Texture', 'gabor_type', gabor_type, 'gabor_texture', ('2D', '3D'))
        node = Node('Gabor Texture', sockets={'Vector': vector, 'Scale': scale, 'Frequency': frequency, 'Anisotropy': anisotropy, 'Orientation 2D': orientation, 'Orientation 3D': orientation_1}, gabor_type=gabor_type)
        return node._out

    @classmethod
    def gradient_texture(cls, vector=None, gradient_type='LINEAR'):
        """ > Node <&ShaderNode Gradient Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - gradient_type (str): parameter 'gradient_type' in ['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']

        Returns
        -------
        - Color [fac_ (Float)]
        """
        utils.check_enum_arg('Gradient Texture', 'gradient_type', gradient_type, 'gradient_texture', ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'))
        node = Node('Gradient Texture', sockets={'Vector': vector}, gradient_type=gradient_type)
        return node._out

    @classmethod
    def ies_texture(cls, vector=None, strength=None, filepath='', ies=None, mode='INTERNAL'):
        """ > Node <&ShaderNode IES Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - strength (Float) : socket 'Strength' (id: Strength)
        - filepath (str): parameter 'filepath'
        - ies (NoneType): parameter 'ies'
        - mode (str): parameter 'mode' in ['INTERNAL', 'EXTERNAL']

        Returns
        -------
        - Float
        """
        utils.check_enum_arg('IES Texture', 'mode', mode, 'ies_texture', ('INTERNAL', 'EXTERNAL'))
        node = Node('IES Texture', sockets={'Vector': vector, 'Strength': strength}, filepath=filepath, ies=ies, mode=mode)
        return node._out

    @classmethod
    def image_texture(cls, vector=None, extension='REPEAT', image=None, interpolation='Linear', projection='FLAT', projection_blend=0.0):
        """ > Node <&ShaderNode Image Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - extension (str): parameter 'extension' in ['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
        - image (NoneType): parameter 'image'
        - interpolation (str): parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
        - projection (str): parameter 'projection' in ['FLAT', 'BOX', 'SPHERE', 'TUBE']
        - projection_blend (float): parameter 'projection_blend'

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        utils.check_enum_arg('Image Texture', 'extension', extension, 'image_texture', ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'))
        utils.check_enum_arg('Image Texture', 'interpolation', interpolation, 'image_texture', ('Linear', 'Closest', 'Cubic', 'Smart'))
        utils.check_enum_arg('Image Texture', 'projection', projection, 'image_texture', ('FLAT', 'BOX', 'SPHERE', 'TUBE'))
        node = Node('Image Texture', sockets={'Vector': vector}, extension=extension, image=image, interpolation=interpolation, projection=projection, projection_blend=projection_blend)
        return node._out

    @classmethod
    def magic_texture(cls, vector=None, scale=None, distortion=None, turbulence_depth=2):
        """ > Node <&ShaderNode Magic Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - turbulence_depth (int): parameter 'turbulence_depth'

        Returns
        -------
        - Color [fac_ (Float)]
        """
        node = Node('Magic Texture', sockets={'Vector': vector, 'Scale': scale, 'Distortion': distortion}, turbulence_depth=turbulence_depth)
        return node._out

    @classmethod
    def noise_texture(cls, vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, offset=None, gain=None, distortion=None, noise_dimensions='3D', noise_type='FBM', normalize=True):
        """ > Node <&ShaderNode Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - w (Float) : socket 'W' (id: W)
        - scale (Float) : socket 'Scale' (id: Scale)
        - detail (Float) : socket 'Detail' (id: Detail)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (id: Lacunarity)
        - offset (Float) : socket 'Offset' (id: Offset)
        - gain (Float) : socket 'Gain' (id: Gain)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - noise_dimensions (str): parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']
        - noise_type (str): parameter 'noise_type' in ['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']
        - normalize (bool): parameter 'normalize'

        Returns
        -------
        - Float [color_ (Color)]
        """
        utils.check_enum_arg('Noise Texture', 'noise_dimensions', noise_dimensions, 'noise_texture', ('1D', '2D', '3D', '4D'))
        utils.check_enum_arg('Noise Texture', 'noise_type', noise_type, 'noise_texture', ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'))
        node = Node('Noise Texture', sockets={'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Offset': offset, 'Gain': gain, 'Distortion': distortion}, noise_dimensions=noise_dimensions, noise_type=noise_type, normalize=normalize)
        return node._out

    @classmethod
    def point_density(cls, vector=None, interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM', radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR'):
        """ > Node <&ShaderNode Point Density>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - interpolation (str): parameter 'interpolation' in ['Closest', 'Linear', 'Cubic']
        - object (NoneType): parameter 'object'
        - particle_color_source (str): parameter 'particle_color_source' in ['PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY']
        - particle_system (NoneType): parameter 'particle_system'
        - point_source (str): parameter 'point_source' in ['PARTICLE_SYSTEM', 'OBJECT']
        - radius (float): parameter 'radius'
        - resolution (int): parameter 'resolution'
        - space (str): parameter 'space' in ['OBJECT', 'WORLD']
        - vertex_attribute_name (str): parameter 'vertex_attribute_name'
        - vertex_color_source (str): parameter 'vertex_color_source' in ['VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL']

        Returns
        -------
        - Color [density_ (Float)]
        """
        utils.check_enum_arg('Point Density', 'interpolation', interpolation, 'point_density', ('Closest', 'Linear', 'Cubic'))
        utils.check_enum_arg('Point Density', 'particle_color_source', particle_color_source, 'point_density', ('PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY'))
        utils.check_enum_arg('Point Density', 'point_source', point_source, 'point_density', ('PARTICLE_SYSTEM', 'OBJECT'))
        utils.check_enum_arg('Point Density', 'space', space, 'point_density', ('OBJECT', 'WORLD'))
        utils.check_enum_arg('Point Density', 'vertex_color_source', vertex_color_source, 'point_density', ('VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL'))
        node = Node('Point Density', sockets={'Vector': vector}, interpolation=interpolation, object=object, particle_color_source=particle_color_source, particle_system=particle_system, point_source=point_source, radius=radius, resolution=resolution, space=space, vertex_attribute_name=vertex_attribute_name, vertex_color_source=vertex_color_source)
        return node._out

    @classmethod
    def sky_texture(cls, vector=None, air_density=1.0, altitude=0.0, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_disc=True, sun_elevation=0.2617993950843811, sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, turbidity=2.200000047683716):
        """ > Node <&ShaderNode Sky Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - air_density (float): parameter 'air_density'
        - altitude (float): parameter 'altitude'
        - dust_density (float): parameter 'dust_density'
        - ground_albedo (float): parameter 'ground_albedo'
        - ozone_density (float): parameter 'ozone_density'
        - sky_type (str): parameter 'sky_type' in ['PREETHAM', 'HOSEK_WILKIE', 'NISHITA']
        - sun_disc (bool): parameter 'sun_disc'
        - sun_elevation (float): parameter 'sun_elevation'
        - sun_intensity (float): parameter 'sun_intensity'
        - sun_rotation (float): parameter 'sun_rotation'
        - sun_size (float): parameter 'sun_size'
        - turbidity (float): parameter 'turbidity'

        Returns
        -------
        - Color
        """
        utils.check_enum_arg('Sky Texture', 'sky_type', sky_type, 'sky_texture', ('PREETHAM', 'HOSEK_WILKIE', 'NISHITA'))
        node = Node('Sky Texture', sockets={'Vector': vector}, air_density=air_density, altitude=altitude, dust_density=dust_density, ground_albedo=ground_albedo, ozone_density=ozone_density, sky_type=sky_type, sun_disc=sun_disc, sun_elevation=sun_elevation, sun_intensity=sun_intensity, sun_rotation=sun_rotation, sun_size=sun_size, turbidity=turbidity)
        return node._out

    @classmethod
    def voronoi_texture(cls, vector=None, w=None, scale=None, detail=None, roughness=None, lacunarity=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', normalize=False, voronoi_dimensions='3D'):
        """ > Node <&ShaderNode Voronoi Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - w (Float) : socket 'W' (id: W)
        - scale (Float) : socket 'Scale' (id: Scale)
        - detail (Float) : socket 'Detail' (id: Detail)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - lacunarity (Float) : socket 'Lacunarity' (id: Lacunarity)
        - smoothness (Float) : socket 'Smoothness' (id: Smoothness)
        - exponent (Float) : socket 'Exponent' (id: Exponent)
        - randomness (Float) : socket 'Randomness' (id: Randomness)
        - distance (str): parameter 'distance' in ['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']
        - feature (str): parameter 'feature' in ['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']
        - normalize (bool): parameter 'normalize'
        - voronoi_dimensions (str): parameter 'voronoi_dimensions' in ['1D', '2D', '3D', '4D']

        Returns
        -------
        - Float [color_ (Color), position_ (Vector)]
        """
        utils.check_enum_arg('Voronoi Texture', 'distance', distance, 'voronoi_texture', ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'))
        utils.check_enum_arg('Voronoi Texture', 'feature', feature, 'voronoi_texture', ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'))
        utils.check_enum_arg('Voronoi Texture', 'voronoi_dimensions', voronoi_dimensions, 'voronoi_texture', ('1D', '2D', '3D', '4D'))
        node = Node('Voronoi Texture', sockets={'Vector': vector, 'W': w, 'Scale': scale, 'Detail': detail, 'Roughness': roughness, 'Lacunarity': lacunarity, 'Smoothness': smoothness, 'Exponent': exponent, 'Randomness': randomness}, distance=distance, feature=feature, normalize=normalize, voronoi_dimensions=voronoi_dimensions)
        return node._out

    @classmethod
    def wave_texture(cls, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """ > Node <&ShaderNode Wave Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - scale (Float) : socket 'Scale' (id: Scale)
        - distortion (Float) : socket 'Distortion' (id: Distortion)
        - detail (Float) : socket 'Detail' (id: Detail)
        - detail_scale (Float) : socket 'Detail Scale' (id: Detail Scale)
        - detail_roughness (Float) : socket 'Detail Roughness' (id: Detail Roughness)
        - phase_offset (Float) : socket 'Phase Offset' (id: Phase Offset)
        - bands_direction (str): parameter 'bands_direction' in ['X', 'Y', 'Z', 'DIAGONAL']
        - rings_direction (str): parameter 'rings_direction' in ['X', 'Y', 'Z', 'SPHERICAL']
        - wave_profile (str): parameter 'wave_profile' in ['SIN', 'SAW', 'TRI']
        - wave_type (str): parameter 'wave_type' in ['BANDS', 'RINGS']

        Returns
        -------
        - Color [fac_ (Float)]
        """
        utils.check_enum_arg('Wave Texture', 'bands_direction', bands_direction, 'wave_texture', ('X', 'Y', 'Z', 'DIAGONAL'))
        utils.check_enum_arg('Wave Texture', 'rings_direction', rings_direction, 'wave_texture', ('X', 'Y', 'Z', 'SPHERICAL'))
        utils.check_enum_arg('Wave Texture', 'wave_profile', wave_profile, 'wave_texture', ('SIN', 'SAW', 'TRI'))
        utils.check_enum_arg('Wave Texture', 'wave_type', wave_type, 'wave_texture', ('BANDS', 'RINGS'))
        node = Node('Wave Texture', sockets={'Vector': vector, 'Scale': scale, 'Distortion': distortion, 'Detail': detail, 'Detail Scale': detail_scale, 'Detail Roughness': detail_roughness, 'Phase Offset': phase_offset}, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node._out

    @classmethod
    def white_noise_texture(cls, vector=None, w=None, noise_dimensions='3D'):
        """ > Node <&ShaderNode White Noise Texture>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - w (Float) : socket 'W' (id: W)
        - noise_dimensions (str): parameter 'noise_dimensions' in ['1D', '2D', '3D', '4D']

        Returns
        -------
        - Float [color_ (Color)]
        """
        utils.check_enum_arg('White Noise Texture', 'noise_dimensions', noise_dimensions, 'white_noise_texture', ('1D', '2D', '3D', '4D'))
        node = Node('White Noise Texture', sockets={'Vector': vector, 'W': w}, noise_dimensions=noise_dimensions)
        return node._out

    @classmethod
    def uv_along_stroke(cls, use_tips=False):
        """ > Node <&ShaderNode UV Along Stroke>

        Arguments
        ---------
        - use_tips (bool): parameter 'use_tips'

        Returns
        -------
        - Vector
        """
        node = Node('UV Along Stroke', sockets={}, use_tips=use_tips)
        return node._out

    @classmethod
    def uv_map(cls, from_instancer=False, uv_map=''):
        """ > Node <&ShaderNode UV Map>

        Arguments
        ---------
        - from_instancer (bool): parameter 'from_instancer'
        - uv_map (str): parameter 'uv_map'

        Returns
        -------
        - Vector
        """
        node = Node('UV Map', sockets={}, from_instancer=from_instancer, uv_map=uv_map)
        return node._out

    @classmethod
    def color_ramp(cls, fac=None, stops=None, interpolation='LINEAR'):
        """ Node <&Node Color Ramp>

        Exposes utilities to manage the color ramp

        ``` python
        ramp1 = Float(.5).color_ramp(stops=[.1, .9])
        ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
        ```

        Arguments
        ---------
        - fac (Float = None)
        - stops (list of tuple(float, tuple)) : stops made of (float, color as tuple of floats)
        - interpolation in ('EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT')
        """
        node = ColorRamp(fac=fac, stops=stops, interpolation=interpolation)
        return node._out

    @classmethod
    @property
    def value(cls):
        """ > Node <&ShaderNode Value>

        Returns
        -------
        - Float
        """
        node = Node('Value', sockets={})
        return node._out

    @classmethod
    def vector_curves(cls, vector=None, fac=None):
        """ > Node <&ShaderNode Vector Curves>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Vector
        """
        node = NodeCurves('Vector Curves', sockets={'Vector': vector, 'Fac': fac})
        return node._out

    @classmethod
    def vector_displacement(cls, vector=None, midlevel=None, scale=None, space='TANGENT'):
        """ > Node <&ShaderNode Vector Displacement>

        Arguments
        ---------
        - vector (Color) : socket 'Vector' (id: Vector)
        - midlevel (Float) : socket 'Midlevel' (id: Midlevel)
        - scale (Float) : socket 'Scale' (id: Scale)
        - space (str): parameter 'space' in ['TANGENT', 'OBJECT', 'WORLD']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Displacement', 'space', space, 'vector_displacement', ('TANGENT', 'OBJECT', 'WORLD'))
        node = Node('Vector Displacement', sockets={'Vector': vector, 'Midlevel': midlevel, 'Scale': scale}, space=space)
        return node._out

    @classmethod
    def vector_math(cls, vector=None, vector_1=None, vector_2=None, scale=None, operation='ADD'):
        """ > Node <&ShaderNode Vector Math>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - vector_1 (Vector) : socket 'Vector' (id: Vector_001)
        - vector_2 (Vector) : socket 'Vector' (id: Vector_002)
        - scale (Float) : socket 'Scale' (id: Scale)
        - operation (str): parameter 'operation' in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Math', 'operation', operation, 'vector_math', ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'))
        node = Node('Vector Math', sockets={'Vector': vector, 'Vector_001': vector_1, 'Vector_002': vector_2, 'Scale': scale}, operation=operation)
        return node._out

    @classmethod
    def vector_rotate(cls, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE'):
        """ > Node <&ShaderNode Vector Rotate>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)
        - angle (Float) : socket 'Angle' (id: Angle)
        - rotation (Vector) : socket 'Rotation' (id: Rotation)
        - invert (bool): parameter 'invert'
        - rotation_type (str): parameter 'rotation_type' in ['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Rotate', 'rotation_type', rotation_type, 'vector_rotate', ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'))
        node = Node('Vector Rotate', sockets={'Vector': vector, 'Center': center, 'Axis': axis, 'Angle': angle, 'Rotation': rotation}, invert=invert, rotation_type=rotation_type)
        return node._out

    @classmethod
    def vector_transform(cls, vector=None, convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR'):
        """ > Node <&ShaderNode Vector Transform>

        Arguments
        ---------
        - vector (Vector) : socket 'Vector' (id: Vector)
        - convert_from (str): parameter 'convert_from' in ['WORLD', 'OBJECT', 'CAMERA']
        - convert_to (str): parameter 'convert_to' in ['WORLD', 'OBJECT', 'CAMERA']
        - vector_type (str): parameter 'vector_type' in ['POINT', 'VECTOR', 'NORMAL']

        Returns
        -------
        - Vector
        """
        utils.check_enum_arg('Vector Transform', 'convert_from', convert_from, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'convert_to', convert_to, 'vector_transform', ('WORLD', 'OBJECT', 'CAMERA'))
        utils.check_enum_arg('Vector Transform', 'vector_type', vector_type, 'vector_transform', ('POINT', 'VECTOR', 'NORMAL'))
        node = Node('Vector Transform', sockets={'Vector': vector}, convert_from=convert_from, convert_to=convert_to, vector_type=vector_type)
        return node._out

    @classmethod
    def color_attribute(cls, layer_name=''):
        """ > Node <&ShaderNode Color Attribute>

        Arguments
        ---------
        - layer_name (str): parameter 'layer_name'

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        node = Node('Color Attribute', sockets={}, layer_name=layer_name)
        return node

    @classmethod
    def volume_absorption(cls, color=None, density=None, weight=None):
        """ > Node <&ShaderNode Volume Absorption>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - density (Float) : socket 'Density' (id: Density)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - VolumeShader
        """
        node = Node('Volume Absorption', sockets={'Color': color, 'Density': density, 'Weight': weight})
        return node._out

    @classmethod
    def volume_info(cls):
        """ > Node <&ShaderNode Volume Info>

        Returns
        -------
        - Color [density_ (Float), flame_ (Float), temperature_ (Float)]
        """
        node = Node('Volume Info', sockets={})
        return node

    @classmethod
    def principled_volume(cls, color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None, weight=None):
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
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - VolumeShader
        """
        node = Node('Principled Volume', sockets={'Color': color, 'Color Attribute': color_attribute, 'Density': density, 'Density Attribute': density_attribute, 'Anisotropy': anisotropy, 'Absorption Color': absorption_color, 'Emission Strength': emission_strength, 'Emission Color': emission_color, 'Blackbody Intensity': blackbody_intensity, 'Blackbody Tint': blackbody_tint, 'Temperature': temperature, 'Temperature Attribute': temperature_attribute, 'Weight': weight})
        return node._out

    @classmethod
    def volume_scatter(cls, color=None, density=None, anisotropy=None, ior=None, backscatter=None, alpha=None, diameter=None, weight=None, phase='HENYEY_GREENSTEIN'):
        """ > Node <&ShaderNode Volume Scatter>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - density (Float) : socket 'Density' (id: Density)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - ior (Float) : socket 'IOR' (id: IOR)
        - backscatter (Float) : socket 'Backscatter' (id: Backscatter)
        - alpha (Float) : socket 'Alpha' (id: Alpha)
        - diameter (Float) : socket 'Diameter' (id: Diameter)
        - weight (Float) : socket 'Weight' (id: Weight)
        - phase (str): parameter 'phase' in ['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE']

        Returns
        -------
        - VolumeShader
        """
        utils.check_enum_arg('Volume Scatter', 'phase', phase, 'volume_scatter', ('HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'))
        node = Node('Volume Scatter', sockets={'Color': color, 'Density': density, 'Anisotropy': anisotropy, 'IOR': ior, 'Backscatter': backscatter, 'Alpha': alpha, 'Diameter': diameter, 'Weight': weight}, phase=phase)
        return node._out

    @classmethod
    def wavelength(cls, wavelength=None):
        """ > Node <&ShaderNode Wavelength>

        Arguments
        ---------
        - wavelength (Float) : socket 'Wavelength' (id: Wavelength)

        Returns
        -------
        - Color
        """
        node = Node('Wavelength', sockets={'Wavelength': wavelength})
        return node._out

    @classmethod
    def wireframe(cls, size=None, use_pixel_size=False):
        """ > Node <&ShaderNode Wireframe>

        Arguments
        ---------
        - size (Float) : socket 'Size' (id: Size)
        - use_pixel_size (bool): parameter 'use_pixel_size'

        Returns
        -------
        - Float
        """
        node = Node('Wireframe', sockets={'Size': size}, use_pixel_size=use_pixel_size)
        return node._out

