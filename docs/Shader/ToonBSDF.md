# Node ToonBSDF

- Node name : 'Toon BSDF'
- bl_idname : [ShaderNodeBsdfToon](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfToon.html)


``` python
ToonBSDF(color=None, size=None, smooth=None, normal=None, component='DIFFUSE', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- size : None
- smooth : None
- normal : None
- component : 'DIFFUSE'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, size=None, smooth=None, normal=None, component='DIFFUSE', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfToon', node_label=node_label, node_color=node_color, **kwargs)

    self.component       = component
    self.color           = color
    self.size            = size
    self.smooth          = smooth
    self.normal          = normal
```
