# Node Mask

- Node name : 'Mask'
- bl_idname : [CompositorNodeMask](https://docs.blender.org/api/current/bpy.types.CompositorNodeMask.html)


``` python
Mask(mask=None, motion_blur_samples=16, motion_blur_shutter=0.5, size_source='SCENE', size_x=256, size_y=256, tag_need_exec=None, use_feather=True, use_motion_blur=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mask : None
- motion_blur_samples : 16
- motion_blur_shutter : 0.5
- size_source : 'SCENE'
- size_x : 256
- size_y : 256
- tag_need_exec : None
- use_feather : True
- use_motion_blur : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, mask=None, motion_blur_samples=16, motion_blur_shutter=0.5, size_source='SCENE', size_x=256, size_y=256, tag_need_exec=None, use_feather=True, use_motion_blur=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMask', node_label=node_label, node_color=node_color, **kwargs)

    self.mask            = mask
    self.motion_blur_samples = motion_blur_samples
    self.motion_blur_shutter = motion_blur_shutter
    self.size_source     = size_source
    self.size_x          = size_x
    self.size_y          = size_y
    self.tag_need_exec   = tag_need_exec
    self.use_feather     = use_feather
    self.use_motion_blur = use_motion_blur
```
