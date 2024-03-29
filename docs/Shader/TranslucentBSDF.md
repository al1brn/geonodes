# Node TranslucentBSDF

- Node name : 'Translucent BSDF'
- bl_idname : [ShaderNodeBsdfTranslucent](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfTranslucent.html)


``` python
TranslucentBSDF(color=None, normal=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, normal=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeBsdfTranslucent', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
    self.normal          = normal
```
