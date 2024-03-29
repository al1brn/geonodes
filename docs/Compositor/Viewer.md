# Node Viewer

- Node name : 'Viewer'
- bl_idname : [CompositorNodeViewer](https://docs.blender.org/api/current/bpy.types.CompositorNodeViewer.html)


``` python
Viewer(image=None, alpha=None, center_x=0.5, center_y=0.5, tag_need_exec=None, tile_order='CENTEROUT', use_alpha=True, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- alpha : None
- center_x : 0.5
- center_y : 0.5
- tag_need_exec : None
- tile_order : 'CENTEROUT'
- use_alpha : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, alpha=None, center_x=0.5, center_y=0.5, tag_need_exec=None, tile_order='CENTEROUT', use_alpha=True, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeViewer', node_label=node_label, node_color=node_color, **kwargs)

    self.center_x        = center_x
    self.center_y        = center_y
    self.tag_need_exec   = tag_need_exec
    self.tile_order      = tile_order
    self.use_alpha       = use_alpha
    self.image           = image
    self.alpha           = alpha
```
