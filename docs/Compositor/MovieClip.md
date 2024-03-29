# Node MovieClip

- Node name : 'Movie Clip'
- bl_idname : [CompositorNodeMovieClip](https://docs.blender.org/api/current/bpy.types.CompositorNodeMovieClip.html)


``` python
MovieClip(clip=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- clip : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, clip=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMovieClip', node_label=node_label, node_color=node_color, **kwargs)

    self.clip            = clip
    self.tag_need_exec   = tag_need_exec
```
