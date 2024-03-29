# Node LuminanceKey

- Node name : 'Luminance Key'
- bl_idname : [CompositorNodeLumaMatte](https://docs.blender.org/api/current/bpy.types.CompositorNodeLumaMatte.html)


``` python
LuminanceKey(image=None, limit_max=1.0, limit_min=0.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- limit_max : 1.0
- limit_min : 0.0
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, limit_max=1.0, limit_min=0.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeLumaMatte', node_label=node_label, node_color=node_color, **kwargs)

    self.limit_max       = limit_max
    self.limit_min       = limit_min
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
