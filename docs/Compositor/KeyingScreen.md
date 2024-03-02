# Node KeyingScreen

- Node name : 'Keying Screen'
- bl_idname : [CompositorNodeKeyingScreen](https://docs.blender.org/api/current/bpy.types.CompositorNodeKeyingScreen.html)


``` python
KeyingScreen(clip=None, tag_need_exec=None, tracking_object='', node_label=None, node_color=None)
```
##### Arguments

- clip : None
- tag_need_exec : None
- tracking_object : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, clip=None, tag_need_exec=None, tracking_object='', node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeKeyingScreen', node_label=node_label, node_color=node_color)

    self.clip            = clip
    self.tag_need_exec   = tag_need_exec
    self.tracking_object = tracking_object
```
