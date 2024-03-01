# Node CombineColor

- Node name : 'Combine Color'
- bl_idname : [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB', node_label=None, node_color=None)
```
##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- mode : 'RGB'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, red=None, green=None, blue=None, alpha=None, mode='RGB', node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeCombineColor', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.red             = red
    self.green           = green
    self.blue            = blue
    self.alpha           = alpha
```
