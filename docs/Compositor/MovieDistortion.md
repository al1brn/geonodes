# Node MovieDistortion

- Node name : 'Movie Distortion'
- bl_idname : [CompositorNodeMovieDistortion](https://docs.blender.org/api/current/bpy.types.CompositorNodeMovieDistortion.html)


``` python
MovieDistortion(image=None, clip=None, distortion_type='UNDISTORT', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- clip : None
- distortion_type : 'UNDISTORT'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, clip=None, distortion_type='UNDISTORT', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMovieDistortion', node_label=node_label, node_color=node_color, **kwargs)

    self.clip            = clip
    self.distortion_type = distortion_type
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
