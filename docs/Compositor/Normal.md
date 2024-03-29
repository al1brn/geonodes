# Node Normal

- Node name : 'Normal'
- bl_idname : [CompositorNodeNormal](https://docs.blender.org/api/current/bpy.types.CompositorNodeNormal.html)


``` python
Normal(normal=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- normal : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, normal=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeNormal', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.normal          = normal
```
