# Node KeyingScreen

- Node name : 'Keying Screen'
- bl_idname : [CompositorNodeKeyingScreen](https://docs.blender.org/api/current/bpy.types.CompositorNodeKeyingScreen.html)


``` python
KeyingScreen(clip=None, smoothness=0.0, tag_need_exec=None, tracking_object='', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- clip : None
- smoothness : 0.0
- tag_need_exec : None
- tracking_object : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, clip=None, smoothness=0.0, tag_need_exec=None, tracking_object='', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeKeyingScreen', node_label=node_label, node_color=node_color, **kwargs)

    self.clip            = clip
    self.smoothness      = smoothness
    self.tag_need_exec   = tag_need_exec
    self.tracking_object = tracking_object
```
