# Node RefractionBSDF

- Node name : 'Refraction BSDF'
- bl_idname : [ShaderNodeBsdfRefraction](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfRefraction.html)


``` python
RefractionBSDF(color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- roughness : None
- ior : None
- normal : None
- distribution : 'BECKMANN'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, ior=None, normal=None, distribution='BECKMANN', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfRefraction', node_label=node_label, node_color=node_color, **kwargs)

    self.distribution    = distribution
    self.color           = color
    self.roughness       = roughness
    self.ior             = ior
    self.normal          = normal
```
