# Node VectorBlur

- Node name : 'Vector Blur'
- bl_idname : [CompositorNodeVecBlur](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
VectorBlur(image=None, z=None, speed=None, factor=1.0, samples=32, speed_max=0, speed_min=0, tag_need_exec=None, use_curved=False, node_label=None, node_color=None)
```
##### Arguments

- image : None
- z : None
- speed : None
- factor : 1.0
- samples : 32
- speed_max : 0
- speed_min : 0
- tag_need_exec : None
- use_curved : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, z=None, speed=None, factor=1.0, samples=32, speed_max=0, speed_min=0, tag_need_exec=None, use_curved=False, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeVecBlur', node_label=node_label, node_color=node_color)

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
