# Node Image

- Node name : 'Image'
- bl_idname : [CompositorNodeImage](https://docs.blender.org/api/current/bpy.types.CompositorNodeImage.html)


``` python
Image(frame_duration=1, frame_offset=0, frame_start=1, has_layers=False, has_views=False, image=None, layer='', tag_need_exec=None, use_auto_refresh=True, use_cyclic=False, use_straight_alpha_output=False, view='', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- frame_duration : 1
- frame_offset : 0
- frame_start : 1
- has_layers : False
- has_views : False
- image : None
- layer : ''
- tag_need_exec : None
- use_auto_refresh : True
- use_cyclic : False
- use_straight_alpha_output : False
- view : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, frame_duration=1, frame_offset=0, frame_start=1, has_layers=False, has_views=False, image=None, layer='', tag_need_exec=None, use_auto_refresh=True, use_cyclic=False, use_straight_alpha_output=False, view='', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeImage', node_label=node_label, node_color=node_color, **kwargs)

    self.frame_duration  = frame_duration
    self.frame_offset    = frame_offset
    self.frame_start     = frame_start
    self.has_layers      = has_layers
    self.has_views       = has_views
    self.image           = image
    self.layer           = layer
    self.tag_need_exec   = tag_need_exec
    self.use_auto_refresh = use_auto_refresh
    self.use_cyclic      = use_cyclic
    self.use_straight_alpha_output = use_straight_alpha_output
    self.view            = view
```
