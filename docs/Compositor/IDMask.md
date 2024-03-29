# Node IDMask

- Node name : 'ID Mask'
- bl_idname : [CompositorNodeIDMask](https://docs.blender.org/api/current/bpy.types.CompositorNodeIDMask.html)


``` python
IDMask(id_value=None, index=0, tag_need_exec=None, use_antialiasing=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- id_value : None
- index : 0
- tag_need_exec : None
- use_antialiasing : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, id_value=None, index=0, tag_need_exec=None, use_antialiasing=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeIDMask', node_label=node_label, node_color=node_color, **kwargs)

    self.index           = index
    self.tag_need_exec   = tag_need_exec
    self.use_antialiasing = use_antialiasing
    self.id_value        = id_value
```
