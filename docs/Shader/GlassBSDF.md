# Node GlassBSDF

- Node name : 'Glass BSDF'
- bl_idname : [ShaderNodeBsdfGlass](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
GlassBSDF(color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX', node_label=None, node_color=None)
```
##### Arguments

- color : None
- roughness : None
- ior : None
- normal : None
- distribution : 'MULTI_GGX'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, ior=None, normal=None, distribution='MULTI_GGX', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBsdfGlass', node_label=node_label, node_color=node_color)

    self.distribution    = distribution
    self.color           = color
    self.roughness       = roughness
    self.ior             = ior
    self.normal          = normal
```
