# Node PlaneTrackDeform

- Node name : 'Plane Track Deform'
- bl_idname : [CompositorNodePlaneTrackDeform](https://docs.blender.org/api/current/bpy.types.CompositorNodePlaneTrackDeform.html)


``` python
PlaneTrackDeform(image=None, clip=None, motion_blur_samples=16, motion_blur_shutter=0.5, plane_track_name='', tag_need_exec=None, tracking_object='', use_motion_blur=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- clip : None
- motion_blur_samples : 16
- motion_blur_shutter : 0.5
- plane_track_name : ''
- tag_need_exec : None
- tracking_object : ''
- use_motion_blur : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, clip=None, motion_blur_samples=16, motion_blur_shutter=0.5, plane_track_name='', tag_need_exec=None, tracking_object='', use_motion_blur=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodePlaneTrackDeform', node_label=node_label, node_color=node_color, **kwargs)

    self.clip            = clip
    self.motion_blur_samples = motion_blur_samples
    self.motion_blur_shutter = motion_blur_shutter
    self.plane_track_name = plane_track_name
    self.tag_need_exec   = tag_need_exec
    self.tracking_object = tracking_object
    self.use_motion_blur = use_motion_blur
    self.image           = image
```
