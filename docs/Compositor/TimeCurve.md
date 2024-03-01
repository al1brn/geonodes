# Node TimeCurve

- Node name : 'Time Curve'
- bl_idname : [CompositorNodeTime](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
TimeCurve(curve=None, frame_end=250, frame_start=1, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- frame_end : 250
- frame_start : 1
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, curve=None, frame_end=250, frame_start=1, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeTime', node_label=node_label, node_color=node_color)

    self.curve           = curve
    self.frame_end       = frame_end
    self.frame_start     = frame_start
    self.tag_need_exec   = tag_need_exec
```
