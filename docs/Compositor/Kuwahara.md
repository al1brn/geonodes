# Node Kuwahara

- Node name : 'Kuwahara'
- bl_idname : [CompositorNodeKuwahara](https://docs.blender.org/api/current/bpy.types.CompositorNodeKuwahara.html)


``` python
Kuwahara(image=None, size=None, eccentricity=1.0, sharpness=0.5, tag_need_exec=None, uniformity=4, use_high_precision=False, variation='CLASSIC', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- size : None
- eccentricity : 1.0
- sharpness : 0.5
- tag_need_exec : None
- uniformity : 4
- use_high_precision : False
- variation : 'CLASSIC'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, size=None, eccentricity=1.0, sharpness=0.5, tag_need_exec=None, uniformity=4, use_high_precision=False, variation='CLASSIC', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeKuwahara', node_label=node_label, node_color=node_color, **kwargs)

    self.eccentricity    = eccentricity
    self.sharpness       = sharpness
    self.tag_need_exec   = tag_need_exec
    self.uniformity      = uniformity
    self.use_high_precision = use_high_precision
    self.variation       = variation
    self.image           = image
    self.size            = size
```
