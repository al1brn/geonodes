# Node DoubleEdgeMask

- Node name : 'Double Edge Mask'
- bl_idname : [CompositorNodeDoubleEdgeMask](https://docs.blender.org/api/current/bpy.types.CompositorNodeDoubleEdgeMask.html)


``` python
DoubleEdgeMask(inner_mask=None, outer_mask=None, edge_mode='BLEED_OUT', inner_mode='ALL', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- inner_mask : None
- outer_mask : None
- edge_mode : 'BLEED_OUT'
- inner_mode : 'ALL'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, inner_mask=None, outer_mask=None, edge_mode='BLEED_OUT', inner_mode='ALL', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDoubleEdgeMask', node_label=node_label, node_color=node_color, **kwargs)

    self.edge_mode       = edge_mode
    self.inner_mode      = inner_mode
    self.tag_need_exec   = tag_need_exec
    self.inner_mask      = inner_mask
    self.outer_mask      = outer_mask
```
