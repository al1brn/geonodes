#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Shader Nodes
-----------------------------------------------------

module : shaderclass
-------------------
- Implement Shader class

classes
-------
- Shader   : Shader class in Material nodes

functions
---------

updates
-------
- creation : 2024/08/07
- update : 2024/09/04
"""

import numpy as np

import bpy
from ..core import utils
from ..core.treeclass import Tree, Node
from ..core.socket_class import Attribute

# =============================================================================================================================
# Shader Root

class ShaderRoot(Attribute):

    def surface_out(self, target='ALL'):
        self._tree.set_surface(self, target=target)

    def volume_out(self, target='ALL'):
        self._tree.set_volume(self, target=target)

    # =============================================================================================================================
    # Properties

    def to_rgb(self):
        node = Node('Shader to RGB', {'Shader': self})
        col = node._out
        col._alpha = node.alpha
        return col

    # =============================================================================================================================
    # Methods

    def add(self, other=None):
        node = Node('Add Shader', {0: self, 1: other})
        return node._out

    def mix(self, fac=None, other=None):
        node = Node('Mix Shader', {0: fac, 1: self, 2: other})
        return node._out

    # =============================================================================================================================
    # Operations

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)

# =============================================================================================================================
# Surface Shader

class Shader(ShaderRoot):

    def out(self, name=None):
        if self._tree._is_group:
            super().out(name=name)
        else:
            self._tree.surface=self

    # =============================================================================================================================
    # Constructors

    @classmethod
    def Diffuse(cls, color=None, roughness=None, normal=None):
        """ Node 'Diffuse BSDF' (ShaderNodeBsdfDiffuse)
        """

        node = Node('Diffuse BSDF', {'Color': color, 'Roughness': roughness, 'Normal': normal})
        return node._out

    @classmethod
    def Emission(cls, color=None, strength=None):
        """ Node 'Emission' (ShaderNodeEmission)
        """

        node = Node('Emission', {'Color': color, 'Strength': strength})
        return node._out

    @classmethod
    def Glass(cls, color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX'):
        """ Node 'Glass BSDF' (ShaderNodeBsdfGlass)
        - distribution in ('BECKMANN', 'GGX', 'MULTI_GGX')
        """

        node = Node('Glass BSDF', {'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal}, distribution=distribution)
        return node._out

    @classmethod
    def Glossy(cls, color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX'):
        """ Node 'Glossy BSDF' (ShaderNodeBsdfAnisotropic)
        - distribution in ('BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX')
        """

        node = Node('Glossy BSDF', {'Color': color, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Rotation': rotation, 'Normal': normal, 'Tangent': tangent}, distribution=distribution)
        return node._out

    @classmethod
    def Holdout(cls):
        """ Node 'Holdout' (ShaderNodeHoldout)
        """

        node = Node('Holdout')
        return node._out

    @classmethod
    def Principled(cls, base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, thin_film_thickness=None, thin_film_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK'):
        """ Node 'Principled BSDF' (ShaderNodeBsdfPrincipled)
        - distribution in ('GGX', 'MULTI_GGX')
        - subsurface_method in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')
        """

        node = Node('Principled BSDF', {'Base Color': base_color, 'Metallic': metallic, 'Roughness': roughness, 'IOR': ior, 'Alpha': alpha, 'Normal': normal, 'Subsurface Weight': subsurface_weight, 'Subsurface Radius': subsurface_radius, 'Subsurface Scale': subsurface_scale, 'Subsurface Anisotropy': subsurface_anisotropy, 'Specular IOR Level': specular_ior_level, 'Specular Tint': specular_tint, 'Anisotropic': anisotropic, 'Anisotropic Rotation': anisotropic_rotation, 'Tangent': tangent, 'Transmission Weight': transmission_weight, 'Coat Weight': coat_weight, 'Coat Roughness': coat_roughness, 'Coat IOR': coat_ior, 'Coat Tint': coat_tint, 'Coat Normal': coat_normal, 'Sheen Weight': sheen_weight, 'Sheen Roughness': sheen_roughness, 'Sheen Tint': sheen_tint, 'Emission Color': emission_color, 'Emission Strength': emission_strength, 'Thin Film Thickness': thin_film_thickness, 'Thin Film IOR': thin_film_ior}, distribution=distribution, subsurface_method=subsurface_method)
        return node._out

    @classmethod
    def Refraction(cls, color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN'):
        """ Node 'Refraction BSDF' (ShaderNodeBsdfRefraction)
        - distribution in ('BECKMANN', 'GGX')
        """

        node = Node('Refraction BSDF', {'Color': color, 'Roughness': roughness, 'IOR': ior, 'Normal': normal}, distribution=distribution)
        return node._out

    @classmethod
    def Specular(cls, base_color=None, specular=None, roughness=None, emissive_color=None, transparency=None, normal=None, clear_coat=None, clear_coat_roughness=None, clear_coat_normal=None):
        """ Node 'Specular BSDF' (ShaderNodeEeveeSpecular)
        """

        node = Node('Specular BSDF', {'Base Color': base_color, 'Specular': specular, 'Roughness': roughness, 'Emissive Color': emissive_color, 'Transparency': transparency, 'Normal': normal, 'Clear Coat': clear_coat, 'Clear Coat Roughness': clear_coat_roughness, 'Clear Coat Normal': clear_coat_normal})
        return node._out

    @classmethod
    def SubsurfaceScattering(cls, color=None, scale=None, radius=None, ior=None, roughness=None, anisotropy=None, normal=None, falloff='RANDOM_WALK'):
        """ Node 'Subsurface Scattering' (ShaderNodeSubsurfaceScattering)
        - falloff in ('BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN')
        """

        node = Node('Subsurface Scattering', {'Color': color, 'Scale': scale, 'Radius': radius, 'IOR': ior, 'Roughness': roughness, 'Anisotropy': anisotropy, 'Normal': normal}, falloff=falloff)
        return node._out

    @classmethod
    def Translucent(cls, color=None, normal=None):
        """ Node 'Translucent BSDF' (ShaderNodeBsdfTranslucent)
        """

        node = Node('Translucent BSDF', {'Color': color, 'Normal': normal})
        return node._out

    @classmethod
    def Transparent(cls, color=None):
        """ Node 'Transparent BSDF' (ShaderNodeBsdfTransparent)
        """

        node = Node('Transparent BSDF', {'Color': color})
        return node._out

# =============================================================================================================================
# Volume Shader

class VolumeShader(ShaderRoot):

    def out(self, name=None):
        if self._tree._is_group:
            super().out(name=name)
        else:
            self._tree.volume=self

    @classmethod
    def Principled(cls, color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None):
        """ Node 'Principled Volume' (ShaderNodeVolumePrincipled)
        """

        node = Node('Principled Volume', {'Color': color, 'Color Attribute': color_attribute, 'Density': density, 'Density Attribute': density_attribute, 'Anisotropy': anisotropy, 'Absorption Color': absorption_color, 'Emission Strength': emission_strength, 'Emission Color': emission_color, 'Blackbody Intensity': blackbody_intensity, 'Blackbody Tint': blackbody_tint, 'Temperature': temperature, 'Temperature Attribute': temperature_attribute})
        return cls(node._out)

    @classmethod
    def Absorption(cls, color=None, density=None):
        """ Node 'Volume Absorption' (ShaderNodeVolumeAbsorption)
        """

        node = Node('Volume Absorption', {'Color': color, 'Density': density})
        return cls(node._out)

    @classmethod
    def Scatter(cls, color=None, density=None, anisotropy=None):
        """ Node 'Volume Scatter' (ShaderNodeVolumeScatter)
        """

        node = Node('Volume Scatter', {'Color': color, 'Density': density, 'Anisotropy': anisotropy})
        return cls(node._out)
