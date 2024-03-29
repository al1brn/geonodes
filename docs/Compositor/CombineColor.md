# Node CombineColor

- Node name : 'Combine Color'
- bl_idname : [CompositorNodeCombineColor](https://docs.blender.org/api/current/bpy.types.CompositorNodeCombineColor.html)


``` python
CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs)
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

- Functions : [combine_color](/docs/Compositor/CompositorTree.md#combine_color) [hsl](/docs/Compositor/CompositorTree.md#hsl) [hsv](/docs/Compositor/CompositorTree.md#hsv) [rgb](/docs/Compositor/CompositorTree.md#rgb) [ycc](/docs/Compositor/CompositorTree.md#ycc) [yuv](/docs/Compositor/CompositorTree.md#yuv)

## Init

``` python
def __init__(self, red=None, green=None, blue=None, alpha=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeCombineColor', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.tag_need_exec   = tag_need_exec
    self.ycc_mode        = ycc_mode
    self.red             = red
    self.green           = green
    self.blue            = blue
    self.alpha           = alpha
```
