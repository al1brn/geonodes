# Node SeparateColor

- Node name : 'Separate Color'
- bl_idname : [FunctionNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)


``` python
SeparateColor(color=None, mode='RGB', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None
- mode : 'RGB'

## Implementation

- [RGBA](/docs/GeoNodes/socket_RGBA.md) : [separate_color](/docs/GeoNodes/socket_RGBA.md#separate_color)

## Init

``` python
def __init__(self, color=None, mode='RGB', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeSeparateColor', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.color           = color
```
