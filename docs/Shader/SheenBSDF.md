# Node SheenBSDF

- Node name : 'Sheen BSDF'
- bl_idname : [ShaderNodeBsdfSheen](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfSheen.html)


``` python
SheenBSDF(color=None, roughness=None, normal=None, distribution='MICROFIBER', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- roughness : None
- normal : None
- distribution : 'MICROFIBER'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, normal=None, distribution='MICROFIBER', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfSheen', node_label=node_label, node_color=node_color, **kwargs)

    self.distribution    = distribution
    self.color           = color
    self.roughness       = roughness
    self.normal          = normal
```
