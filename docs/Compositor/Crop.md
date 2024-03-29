# Node Crop

- Node name : 'Crop'
- bl_idname : [CompositorNodeCrop](https://docs.blender.org/api/current/bpy.types.CompositorNodeCrop.html)


``` python
Crop(image=None, max_x=0, max_y=0, min_x=0, min_y=0, rel_max_x=0.0, rel_max_y=0.0, rel_min_x=0.0, rel_min_y=0.0, relative=False, tag_need_exec=None, use_crop_size=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- max_x : 0
- max_y : 0
- min_x : 0
- min_y : 0
- rel_max_x : 0.0
- rel_max_y : 0.0
- rel_min_x : 0.0
- rel_min_y : 0.0
- relative : False
- tag_need_exec : None
- use_crop_size : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, max_x=0, max_y=0, min_x=0, min_y=0, rel_max_x=0.0, rel_max_y=0.0, rel_min_x=0.0, rel_min_y=0.0, relative=False, tag_need_exec=None, use_crop_size=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeCrop', node_label=node_label, node_color=node_color, **kwargs)

    self.max_x           = max_x
    self.max_y           = max_y
    self.min_x           = min_x
    self.min_y           = min_y
    self.rel_max_x       = rel_max_x
    self.rel_max_y       = rel_max_y
    self.rel_min_x       = rel_min_x
    self.rel_min_y       = rel_min_y
    self.relative        = relative
    self.tag_need_exec   = tag_need_exec
    self.use_crop_size   = use_crop_size
    self.image           = image
```
