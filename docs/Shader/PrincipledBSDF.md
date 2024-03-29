# Node PrincipledBSDF

- Node name : 'Principled BSDF'
- bl_idname : [ShaderNodeBsdfPrincipled](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfPrincipled.html)


``` python
PrincipledBSDF(base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, subsurface_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- base_color : None
- metallic : None
- roughness : None
- ior : None
- alpha : None
- normal : None
- subsurface_weight : None
- subsurface_radius : None
- subsurface_scale : None
- subsurface_anisotropy : None
- specular_ior_level : None
- specular_tint : None
- anisotropic : None
- anisotropic_rotation : None
- tangent : None
- transmission_weight : None
- coat_weight : None
- coat_roughness : None
- coat_ior : None
- coat_tint : None
- coat_normal : None
- sheen_weight : None
- sheen_roughness : None
- sheen_tint : None
- emission_color : None
- emission_strength : None
- subsurface_ior : None
- distribution : 'MULTI_GGX'
- subsurface_method : 'RANDOM_WALK'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None, specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None, sheen_tint=None, emission_color=None, emission_strength=None, subsurface_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfPrincipled', node_label=node_label, node_color=node_color, **kwargs)

    self.distribution    = distribution
    self.subsurface_method = subsurface_method
    self.base_color      = base_color
    self.metallic        = metallic
    self.roughness       = roughness
    self.ior             = ior
    self.alpha           = alpha
    self.normal          = normal
    self.subsurface_weight = subsurface_weight
    self.subsurface_radius = subsurface_radius
    self.subsurface_scale = subsurface_scale
    self.subsurface_anisotropy = subsurface_anisotropy
    self.specular_ior_level = specular_ior_level
    self.specular_tint   = specular_tint
    self.anisotropic     = anisotropic
    self.anisotropic_rotation = anisotropic_rotation
    self.tangent         = tangent
    self.transmission_weight = transmission_weight
    self.coat_weight     = coat_weight
    self.coat_roughness  = coat_roughness
    self.coat_ior        = coat_ior
    self.coat_tint       = coat_tint
    self.coat_normal     = coat_normal
    self.sheen_weight    = sheen_weight
    self.sheen_roughness = sheen_roughness
    self.sheen_tint      = sheen_tint
    self.emission_color  = emission_color
    self.emission_strength = emission_strength
    self.subsurface_ior  = subsurface_ior
```
