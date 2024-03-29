# Node MapValue

- Node name : 'Map Value'
- bl_idname : [CompositorNodeMapValue](https://docs.blender.org/api/current/bpy.types.CompositorNodeMapValue.html)


``` python
MapValue(value=None, max=None, min=None, offset=None, size=None, tag_need_exec=None, use_max=False, use_min=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- max : None
- min : None
- offset : None
- size : None
- tag_need_exec : None
- use_max : False
- use_min : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, value=None, max=None, min=None, offset=None, size=None, tag_need_exec=None, use_max=False, use_min=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMapValue', node_label=node_label, node_color=node_color, **kwargs)

    self.max             = max
    self.min             = min
    self.offset          = offset
    self.size            = size
    self.tag_need_exec   = tag_need_exec
    self.use_max         = use_max
    self.use_min         = use_min
    self.value           = value
```
