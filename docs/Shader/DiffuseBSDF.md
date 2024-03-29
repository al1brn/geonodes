# Node DiffuseBSDF

- Node name : 'Diffuse BSDF'
- bl_idname : [ShaderNodeBsdfDiffuse](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfDiffuse.html)


``` python
DiffuseBSDF(color=None, roughness=None, normal=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- roughness : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, normal=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfDiffuse', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.roughness       = roughness
    self.normal          = normal
```
