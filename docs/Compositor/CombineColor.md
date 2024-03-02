# Node CombineColor

- Node name : 'Combine Color'
- bl_idname : [CompositorNodeCombineColor](https://docs.blender.org/api/current/bpy.types.CompositorNodeCombineColor.html)


``` python
CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None)
```
##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- mode : 'RGB'
- tag_need_exec : None
- ycc_mode : 'ITUBT709'

## Implementation

- Functions : [combine_color](/docs/Compositor/CompositorTree.md#combine_color)

## Init

``` python
def __init__(self, red=None, green=None, blue=None, alpha=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeCombineColor', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.tag_need_exec   = tag_need_exec
    self.ycc_mode        = ycc_mode
    self.red             = red
    self.green           = green
    self.blue            = blue
    self.alpha           = alpha
```
