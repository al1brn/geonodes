# Node LayerWeight

- Node name : 'Layer Weight'
- bl_idname : [Layer Weight](https://docs.blender.org/api/current/bpy.types.Layer Weight.html)


``` python
LayerWeight(blend=None, normal=None, node_label=None, node_color=None)
```
##### Arguments

- blend : None
- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, blend=None, normal=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeLayerWeight', node_label=node_label, node_color=node_color)

    self.blend           = blend
    self.normal          = normal
```
