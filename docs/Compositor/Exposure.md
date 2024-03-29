# Node Exposure

- Node name : 'Exposure'
- bl_idname : [CompositorNodeExposure](https://docs.blender.org/api/current/bpy.types.CompositorNodeExposure.html)


``` python
Exposure(image=None, exposure=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- exposure : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, exposure=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeExposure', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.exposure        = exposure
```
