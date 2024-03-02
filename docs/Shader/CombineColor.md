# Node CombineColor

- Node name : 'Combine Color'
- bl_idname : [ShaderNodeCombineColor](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineColor.html)


``` python
CombineColor(red=None, green=None, blue=None, mode='RGB', node_label=None, node_color=None)
```
##### Arguments

- red : None
- green : None
- blue : None
- mode : 'RGB'

## Implementation

- Functions : [combine_color](/docs/Shader/ShaderTree.md#combine_color)

## Init

``` python
def __init__(self, red=None, green=None, blue=None, mode='RGB', node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeCombineColor', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.red             = red
    self.green           = green
    self.blue            = blue
```