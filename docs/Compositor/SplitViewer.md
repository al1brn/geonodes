# Node SplitViewer

- Node name : 'Split Viewer'
- bl_idname : [CompositorNodeSplitViewer](https://docs.blender.org/api/current/bpy.types.CompositorNodeSplitViewer.html)


``` python
SplitViewer(image=None, image_1=None, axis='X', factor=50, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- image_1 : None
- axis : 'X'
- factor : 50
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, image_1=None, axis='X', factor=50, tag_need_exec=None, node_label=None, node_color=None):

    Node.__init__(self, 'CompositorNodeSplitViewer', node_label=node_label, node_color=node_color)

    self.axis            = axis
    self.factor          = factor
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.image_1         = image_1
```
