# Node MapUV

- Node name : 'Map UV'
- bl_idname : [CompositorNodeMapUV](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
MapUV(image=None, uv=None, alpha=0, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- uv : None
- alpha : 0
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, uv=None, alpha=0, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeMapUV', node_label=node_label, node_color=node_color)

    self.alpha           = alpha
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.uv              = uv
```
