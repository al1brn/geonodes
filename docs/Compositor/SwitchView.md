# Node SwitchView

- Node name : 'Switch View'
- bl_idname : [CompositorNodeSwitchView](https://docs.blender.org/api/current/bpy.types.CompositorNodeSwitchView.html)


``` python
SwitchView(left=None, right=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- left : None
- right : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, left=None, right=None, tag_need_exec=None, node_label=None, node_color=None):

    Node.__init__(self, 'CompositorNodeSwitchView', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.left            = left
    self.right           = right
```