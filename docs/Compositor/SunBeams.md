# Node SunBeams

- Node name : 'Sun Beams'
- bl_idname : [CompositorNodeSunBeams](https://docs.blender.org/api/current/bpy.types.CompositorNodeSunBeams.html)


``` python
SunBeams(image=None, ray_length=0.0, source=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- ray_length : 0.0
- source : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, ray_length=0.0, source=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeSunBeams', node_label=node_label, node_color=node_color, **kwargs)

    self.ray_length      = ray_length
    self.source          = source
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
