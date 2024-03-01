# Node Kuwahara

- Node name : 'Kuwahara'
- bl_idname : [CompositorNodeKuwahara](https://docs.blender.org/api/current/bpy.types.CompositorNodeKuwahara.html)


``` python
Kuwahara(image=None, eccentricity=1.0, sharpness=0.5, size=6, tag_need_exec=None, uniformity=4, variation='CLASSIC', node_label=None, node_color=None)
```
##### Arguments

- image : None
- eccentricity : 1.0
- sharpness : 0.5
- size : 6
- tag_need_exec : None
- uniformity : 4
- variation : 'CLASSIC'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, eccentricity=1.0, sharpness=0.5, size=6, tag_need_exec=None, uniformity=4, variation='CLASSIC', node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeKuwahara', node_label=node_label, node_color=node_color)

    self.eccentricity    = eccentricity
    self.sharpness       = sharpness
    self.size            = size
    self.tag_need_exec   = tag_need_exec
    self.uniformity      = uniformity
    self.variation       = variation
    self.image           = image
```
