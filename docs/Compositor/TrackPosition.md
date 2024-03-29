# Node TrackPosition

- Node name : 'Track Position'
- bl_idname : [CompositorNodeTrackPos](https://docs.blender.org/api/current/bpy.types.CompositorNodeTrackPos.html)


``` python
TrackPosition(clip=None, frame_relative=0, position='ABSOLUTE', tag_need_exec=None, track_name='', tracking_object='', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- clip : None
- frame_relative : 0
- position : 'ABSOLUTE'
- tag_need_exec : None
- track_name : ''
- tracking_object : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, clip=None, frame_relative=0, position='ABSOLUTE', tag_need_exec=None, track_name='', tracking_object='', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeTrackPos', node_label=node_label, node_color=node_color, **kwargs)

    self.clip            = clip
    self.frame_relative  = frame_relative
    self.position        = position
    self.tag_need_exec   = tag_need_exec
    self.track_name      = track_name
    self.tracking_object = tracking_object
```
