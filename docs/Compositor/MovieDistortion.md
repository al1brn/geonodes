# Node MovieDistortion

- Node name : 'Movie Distortion'
- bl_idname : CompositorNodeMovieDistortion


``` python
MovieDistortion(image=None, clip=None, distortion_type='UNDISTORT', tag_need_exec=None, node_label=None, node_color=None)
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
def __init__(self, image=None, clip=None, distortion_type='UNDISTORT', tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeMovieDistortion', node_label=node_label, node_color=node_color)

    self.clip            = clip
    self.distortion_type = distortion_type
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
