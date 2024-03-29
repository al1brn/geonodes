# Node Normalize

- Node name : 'Normalize'
- bl_idname : [CompositorNodeNormalize](https://docs.blender.org/api/current/bpy.types.CompositorNodeNormalize.html)


``` python
Normalize(value=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, value=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeNormalize', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.value           = value
```
