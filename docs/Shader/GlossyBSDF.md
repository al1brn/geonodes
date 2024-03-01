# Node GlossyBSDF

- Node name : 'Glossy BSDF'
- bl_idname : [ShaderNodeBsdfAnisotropic](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
GlossyBSDF(color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX', node_label=None, node_color=None)
```
##### Arguments

- color : None
- roughness : None
- anisotropy : None
- rotation : None
- normal : None
- tangent : None
- distribution : 'MULTI_GGX'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, anisotropy=None, rotation=None, normal=None, tangent=None, distribution='MULTI_GGX', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBsdfAnisotropic', node_label=node_label, node_color=node_color)

    self.distribution    = distribution
    self.color           = color
    self.roughness       = roughness
    self.anisotropy      = anisotropy
    self.rotation        = rotation
    self.normal          = normal
    self.tangent         = tangent
```
