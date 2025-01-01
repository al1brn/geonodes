from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Shader(Socket):

    def add_shader(self, shader=None):
        """ > Method <&ShaderNode Add Shader>

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
        node = Node('Add Shader', sockets={'Shader': self, 'Shader_001': shader})
        return node._out

    @classmethod
    def Glossy(cls, color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX'):
        """ > Class Method <&ShaderNode Glossy BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - rotation (Float) : socket 'Rotation' (id: Rotation)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - distribution (str): parameter 'distribution' in ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX')

        Returns
        -------
        - Shader
        """
        node = Node('Glossy BSDF', sockets={'Color': color, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent}, distribution=distribution)
        return node._out

    @classmethod
    def Diffuse(cls, color=None, roughness=None, normal=None):
        """ > Class Method <&ShaderNode Diffuse BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Shader
        """
        node = Node('Diffuse BSDF', sockets={'Color': color, 'Roughness': roughness, 'Normal': normal})
        return node._out

    @classmethod
    def Glass(cls, color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX'):
        """ > Class Method <&ShaderNode Glass BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - distribution (str): parameter 'distribution' in ('BECKMANN', 'GGX', 'MULTI_GGX')

        Returns
        -------
        - Shader
        """
        node = Node('Glass BSDF', sockets={'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal}, distribution=distribution)
        return node._out

    @classmethod
    def Hair(cls, color=None, offset=None, roughnessu=None, roughnessv=None, tangent=None, component='Reflection'):
        """ > Class Method <&ShaderNode Hair BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - offset (Float) : socket 'Offset' (id: Offset)
        - roughnessu (Float) : socket 'RoughnessU' (id: RoughnessU)
        - roughnessv (Float) : socket 'RoughnessV' (id: RoughnessV)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - component (str): parameter 'component' in ('Reflection', 'Transmission')

        Returns
        -------
        - Shader
        """
        node = Node('Hair BSDF', sockets={'Color': color, 'Offset': offset, 'RoughnessU': roughnessu, 'RoughnessV': roughnessv, 'Tangent': tangent}, component=component)
        return node._out

    @classmethod
    def PrincipledHair(cls, color=None, roughness=None, radial_roughness=None, coat=None, ior=None, offset=None, random_roughness=None, random=None, model='CHIANG', parametrization='COLOR'):
        """ > Class Method <&ShaderNode Principled Hair BSDF>

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
        - model (str): parameter 'model' in ('CHIANG', 'HUANG')
        - parametrization (str): parameter 'parametrization' in ('ABSORPTION', 'MELANIN', 'COLOR')

        Returns
        -------
        - Shader
        """
        node = Node('Principled Hair BSDF', sockets={'Color': color, 'Roughness': roughness, 'Radial Roughness': radial_roughness, 'Coat': coat, 'IOR': ior, 'Offset': offset, 'Random Roughness': random_roughness, 'Random': random}, model=model, parametrization=parametrization)
        return node._out

    @classmethod
    def Metallic(cls, base_color=None, edge_tint=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX', fresnel_type='F82'):
        """ > Class Method <&ShaderNode Metallic BSDF>

        Arguments
        ---------
        - base_color (Color) : socket 'Base Color' (id: Base Color)
        - edge_tint (Color) : socket 'Edge Tint' (id: Edge Tint)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - anisotropy (Float) : socket 'Anisotropy' (id: Anisotropy)
        - rotation (Float) : socket 'Rotation' (id: Rotation)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - tangent (Vector) : socket 'Tangent' (id: Tangent)
        - distribution (str): parameter 'distribution' in ('BECKMANN', 'GGX', 'MULTI_GGX')
        - fresnel_type (str): parameter 'fresnel_type' in ('PHYSICAL_CONDUCTOR', 'F82')

        Returns
        -------
        - Shader
        """
        node = Node('Metallic BSDF', sockets={'Base Color': base_color, 'Edge Tint': edge_tint, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent}, distribution=distribution, fresnel_type=fresnel_type)
        return node._out

    @classmethod
    def Principled(cls, base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, diffuse_roughness=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, thin_film_thickness=None, thin_film_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK'):
        """ > Class Method <&ShaderNode Principled BSDF>

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
        - distribution (str): parameter 'distribution' in ('GGX', 'MULTI_GGX')
        - subsurface_method (str): parameter 'subsurface_method' in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')

        Returns
        -------
        - Shader
        """
        node = Node('Principled BSDF', sockets={'Base Color': base_color, 'Metallic': metallic, 'Roughness': roughness, 'IOR': ior, 'Alpha': alpha, 'Normal': normal, 'Diffuse Roughness': diffuse_roughness, 'Subsurface Weight': subsurface_weight, 'Subsurface Radius': subsurface_radius, 'Subsurface Scale': subsurface_scale, 'Subsurface Anisotropy': subsurface_anisotropy, 'Specular IOR Level': specular_ior_level, 'Specular Tint': specular_tint, 'Anisotropic': anisotropic, 'Anisotropic Rotation': anisotropic_rotation, 'Tangent': tangent, 'Transmission Weight': transmission_weight, 'Coat Weight': coat_weight, 'Coat Roughness': coat_roughness, 'Coat IOR': coat_ior, 'Coat Tint': coat_tint, 'Coat Normal': coat_normal, 'Sheen Weight': sheen_weight, 'Sheen Roughness': sheen_roughness, 'Sheen Tint': sheen_tint, 'Emission Color': emission_color, 'Emission Strength': emission_strength, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, subsurface_method=subsurface_method)
        return node._out

    @classmethod
    def RayPortal(cls, color=None, position=None, direction=None):
        """ > Class Method <&ShaderNode Ray Portal BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - position (Vector) : socket 'Position' (id: Position)
        - direction (Vector) : socket 'Direction' (id: Direction)

        Returns
        -------
        - Shader
        """
        node = Node('Ray Portal BSDF', sockets={'Color': color, 'Position': position, 'Direction': direction})
        return node._out

    @classmethod
    def Refraction(cls, color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN'):
        """ > Class Method <&ShaderNode Refraction BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - ior (Float) : socket 'IOR' (id: IOR)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - distribution (str): parameter 'distribution' in ('BECKMANN', 'GGX')

        Returns
        -------
        - Shader
        """
        node = Node('Refraction BSDF', sockets={'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal}, distribution=distribution)
        return node._out

    @classmethod
    def Sheen(cls, color=None, roughness=None, normal=None, distribution='MICROFIBER'):
        """ > Class Method <&ShaderNode Sheen BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - roughness (Float) : socket 'Roughness' (id: Roughness)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - distribution (str): parameter 'distribution' in ('ASHIKHMIN', 'MICROFIBER')

        Returns
        -------
        - Shader
        """
        node = Node('Sheen BSDF', sockets={'Color': color, 'Roughness': roughness, 'Normal': normal}, distribution=distribution)
        return node._out

    @classmethod
    def Toon(cls, color=None, size=None, smooth=None, normal=None, component='DIFFUSE'):
        """ > Class Method <&ShaderNode Toon BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - size (Float) : socket 'Size' (id: Size)
        - smooth (Float) : socket 'Smooth' (id: Smooth)
        - normal (Vector) : socket 'Normal' (id: Normal)
        - component (str): parameter 'component' in ('DIFFUSE', 'GLOSSY')

        Returns
        -------
        - Shader
        """
        node = Node('Toon BSDF', sockets={'Color': color, 'Size': size, 'Smooth': smooth, 'Normal': normal}, component=component)
        return node._out

    @classmethod
    def Translucent(cls, color=None, normal=None):
        """ > Class Method <&ShaderNode Translucent BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Shader
        """
        node = Node('Translucent BSDF', sockets={'Color': color, 'Normal': normal})
        return node._out

    @classmethod
    def Transparent(cls, color=None):
        """ > Class Method <&ShaderNode Transparent BSDF>

        Arguments
        ---------
        - color (Color) : socket 'Color' (id: Color)

        Returns
        -------
        - Shader
        """
        node = Node('Transparent BSDF', sockets={'Color': color})
        return node._out

    @classmethod
    def Specular(cls, base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None):
        """ > Class Method <&ShaderNode Specular BSDF>

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
        node = Node('Specular BSDF', sockets={'Base Color': base_color, 'Specular': specular, 'Roughness': roughness, 'Emissive Color': emissive_color, 'Transparency': transparency, 'Normal': normal, 'Clear Coat': clear_coat, 'Clear Coat Roughness': clear_coat_roughness, 'Clear Coat Normal': clear_coat_normal})
        return node._out

    @classmethod
    @property
    def Holdout(cls):
        """ > Constructor <&ShaderNode Holdout>

        Returns
        -------
        - Shader
        """
        node = Node('Holdout', sockets={})
        return cls(node._out)

    def mix_shader(self, shader=None, fac=None):
        """ > Method <&ShaderNode Mix Shader>

        Information
        -----------
        - Socket 'Shader' : self

        Arguments
        ---------
        - shader (Shader) : socket 'Shader' (id: Shader_001)
        - fac (Float) : socket 'Fac' (id: Fac)

        Returns
        -------
        - Shader
        """
        node = Node('Mix Shader', sockets={'Shader': self, 'Shader_001': shader, 'Fac': fac})
        return node._out

    def light_output(self, is_active_output=True, target='ALL'):
        """ > Method <&ShaderNode Light Output>

        Information
        -----------
        - Socket 'Surface' : self

        Arguments
        ---------
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')

        Returns
        -------
        - None
        """
        node = Node('Light Output', sockets={'Surface': self}, is_active_output=is_active_output, target=target)
        return node._out

    def material_output(self, volume=None, displacement=None, thickness=None, is_active_output=True, target='ALL'):
        """ > Method <&ShaderNode Material Output>

        Information
        -----------
        - Socket 'Surface' : self

        Arguments
        ---------
        - volume (Shader) : socket 'Volume' (id: Volume)
        - displacement (Vector) : socket 'Displacement' (id: Displacement)
        - thickness (Float) : socket 'Thickness' (id: Thickness)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')

        Returns
        -------
        - None
        """
        node = Node('Material Output', sockets={'Surface': self, 'Volume': volume, 'Displacement': displacement, 'Thickness': thickness}, is_active_output=is_active_output, target=target)
        return node._out

    def world_output(self, volume=None, is_active_output=True, target='ALL'):
        """ > Method <&ShaderNode World Output>

        Information
        -----------
        - Socket 'Surface' : self

        Arguments
        ---------
        - volume (Shader) : socket 'Volume' (id: Volume)
        - is_active_output (bool): parameter 'is_active_output'
        - target (str): parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')

        Returns
        -------
        - None
        """
        node = Node('World Output', sockets={'Surface': self, 'Volume': volume}, is_active_output=is_active_output, target=target)
        return node._out

    def shader_to_rgb(self):
        """ > Method <&ShaderNode Shader to RGB>

        Information
        -----------
        - Socket 'Shader' : self

        Returns
        -------
        - Color [alpha_ (Float)]
        """
        node = Node('Shader to RGB', sockets={'Shader': self})
        return node._out
