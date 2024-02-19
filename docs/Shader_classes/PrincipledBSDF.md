# class PrincipledBSDF (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : PrincipledBSDF
 - bl_idname : ShaderNodeBsdfPrincipled

Node parameters
 - distribution : 'MULTI_GGX'
 - subsurface_method : 'RANDOM_WALK'

Input sockets
 - base_color : Col
 - metallic : Float
 - roughness : Float
 - ior : Float
 - alpha : Float
 - normal : Vect
 - weight : Float
 - subsurface_weight : Float
 - subsurface_radius : Vect
 - subsurface_scale : Float
 - subsurface_ior : Float
 - subsurface_anisotropy : Float
 - specular_ior_level : Float
 - specular_tint : Col
 - anisotropic : Float
 - anisotropic_rotation : Float
 - tangent : Vect
 - transmission_weight : Float
 - coat_weight : Float
 - coat_roughness : Float
 - coat_ior : Float
 - coat_tint : Col
 - coat_normal : Vect
 - sheen_weight : Float
 - sheen_roughness : Float
 - sheen_tint : Col
 - emission_color : Col
 - emission_strength : Float

Output sockets
 - bsdf : Shader

### Header

``` python
def PrincipledBSDF(self, base_color=None, metallic=None, roughness=None, ior=None, alpha=None, normal=None, subsurface_weight=None, subsurface_radius=None, subsurface_scale=None, subsurface_anisotropy=None, specular_ior_level=None,
specular_tint=None, anisotropic=None, anisotropic_rotation=None, tangent=None, transmission_weight=None, coat_weight=None, coat_roughness=None, coat_ior=None, coat_tint=None, coat_normal=None, sheen_weight=None, sheen_roughness=None,
sheen_tint=None, emission_color=None, emission_strength=None, subsurface_ior=None, distribution='MULTI_GGX', subsurface_method='RANDOM_WALK', node_label=None, node_color=None):
```

## Implementations

o functions : [principled_bsdf](/docs/Shader_classes/GLOBAL.md#principled_bsdf)

