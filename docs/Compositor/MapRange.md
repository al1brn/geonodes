# Node MapRange

- Node name : 'Map Range'
- bl_idname : [CompositorNodeMapRange](https://docs.blender.org/api/current/bpy.types.CompositorNodeMapRange.html)


``` python
MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- from_min : None
- from_max : None
- to_min : None
- to_max : None
- tag_need_exec : None
- use_clamp : False

## Implementation

- [VALUE](/docs/Compositor/socket_VALUE.md) : [map_range](/docs/Compositor/socket_VALUE.md#map_range)
- [VECTOR](/docs/Compositor/socket_VECTOR.md) : [map_range](/docs/Compositor/socket_VECTOR.md#map_range)

## Init

``` python
def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, tag_need_exec=None, use_clamp=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMapRange', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.use_clamp       = use_clamp
    self.value           = value
    self.from_min        = from_min
    self.from_max        = from_max
    self.to_min          = to_min
    self.to_max          = to_max
```
