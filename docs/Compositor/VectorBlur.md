# Node VectorBlur

- Node name : 'Vector Blur'
- bl_idname : [CompositorNodeVecBlur](https://docs.blender.org/api/current/bpy.types.CompositorNodeVecBlur.html)


``` python
VectorBlur(image=None, z=None, speed=None, factor=0.25, samples=32, speed_max=0, speed_min=0, tag_need_exec=None, use_curved=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- z : None
- speed : None
- factor : 0.25
- samples : 32
- speed_max : 0
- speed_min : 0
- tag_need_exec : None
- use_curved : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, z=None, speed=None, factor=0.25, samples=32, speed_max=0, speed_min=0, tag_need_exec=None, use_curved=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeVecBlur', node_label=node_label, node_color=node_color, **kwargs)

    self.factor          = factor
    self.samples         = samples
    self.speed_max       = speed_max
    self.speed_min       = speed_min
    self.tag_need_exec   = tag_need_exec
    self.use_curved      = use_curved
    self.image           = image
    self.z               = z
    self.speed           = speed
```
