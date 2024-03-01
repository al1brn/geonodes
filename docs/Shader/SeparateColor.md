# Node SeparateColor

- Node name : 'Separate Color'
- bl_idname : [Separate Color](https://docs.blender.org/api/current/bpy.types.Separate Color.html)


``` python
SeparateColor(color=None, mode='RGB', node_label=None, node_color=None)
```
##### Arguments

- color : None
- mode : 'RGB'

## Implementation

- [Col](/docs/Shader/Col.md) : [separate_color](/docs/Shader/Col.md#separate_color)

## Init

``` python
def __init__(self, color=None, mode='RGB', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeSeparateColor', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.color           = color
```
