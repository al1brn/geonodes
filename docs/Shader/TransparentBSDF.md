# Node TransparentBSDF

- Node name : 'Transparent BSDF'
- bl_idname : [ShaderNodeBsdfTransparent](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfTransparent.html)


``` python
TransparentBSDF(color=None, node_label=None, node_color=None)
```
##### Arguments

- color : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeBsdfTransparent', node_label=node_label, node_color=node_color)

    self.color           = color
```