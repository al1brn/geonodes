# Node ZCombine

- Node name : 'Z Combine'
- bl_idname : [CompositorNodeZcombine](https://docs.blender.org/api/current/bpy.types.CompositorNodeZcombine.html)


``` python
ZCombine(image=None, image_1=None, z=None, z_1=None, tag_need_exec=None, use_alpha=False, use_antialias_z=True, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- image_1 : None
- z : None
- z_1 : None
- tag_need_exec : None
- use_alpha : False
- use_antialias_z : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, image_1=None, z=None, z_1=None, tag_need_exec=None, use_alpha=False, use_antialias_z=True, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeZcombine', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.use_alpha       = use_alpha
    self.use_antialias_z = use_antialias_z
    self.image           = image
    self.image_1         = image_1
    self.z               = z
    self.z_1             = z_1
```
