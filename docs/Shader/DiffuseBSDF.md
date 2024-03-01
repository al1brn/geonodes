# Node DiffuseBSDF

- Node name : 'Diffuse BSDF'
- bl_idname : ShaderNodeBsdfDiffuse


``` python
DiffuseBSDF(color=None, roughness=None, normal=None, node_label=None, node_color=None)
```
##### Arguments

- color : None
- roughness : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, roughness=None, normal=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeBsdfDiffuse', node_label=node_label, node_color=node_color)

    self.color           = color
    self.roughness       = roughness
    self.normal          = normal
```
