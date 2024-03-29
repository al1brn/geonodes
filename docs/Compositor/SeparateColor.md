# Node SeparateColor

- Node name : 'Separate Color'
- bl_idname : [CompositorNodeSeparateColor](https://docs.blender.org/api/current/bpy.types.CompositorNodeSeparateColor.html)


``` python
SeparateColor(image=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- mode : 'RGB'
- tag_need_exec : None
- ycc_mode : 'ITUBT709'

## Implementation

- [RGBA](/docs/Compositor/socket_RGBA.md) : [separate_color](/docs/Compositor/socket_RGBA.md#separate_color)

## Init

``` python
def __init__(self, image=None, mode='RGB', tag_need_exec=None, ycc_mode='ITUBT709', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeSeparateColor', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.tag_need_exec   = tag_need_exec
    self.ycc_mode        = ycc_mode
    self.image           = image
```
