# Node LayerWeight

- Node name : 'Layer Weight'
- bl_idname : [ShaderNodeLayerWeight](https://docs.blender.org/api/current/bpy.types.ShaderNodeLayerWeight.html)


``` python
LayerWeight(blend=None, normal=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- blend : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, blend=None, normal=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeLayerWeight', node_label=node_label, node_color=node_color, **kwargs)

    self.blend           = blend
    self.normal          = normal
```
