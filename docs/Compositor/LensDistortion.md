# Node LensDistortion

- Node name : 'Lens Distortion'
- bl_idname : [CompositorNodeLensdist](https://docs.blender.org/api/current/bpy.types.CompositorNodeLensdist.html)


``` python
LensDistortion(image=None, distortion=None, dispersion=None, tag_need_exec=None, use_fit=False, use_jitter=False, use_projector=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- distortion : None
- dispersion : None
- tag_need_exec : None
- use_fit : False
- use_jitter : False
- use_projector : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, distortion=None, dispersion=None, tag_need_exec=None, use_fit=False, use_jitter=False, use_projector=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeLensdist', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.use_fit         = use_fit
    self.use_jitter      = use_jitter
    self.use_projector   = use_projector
    self.image           = image
    self.distortion      = distortion
    self.dispersion      = dispersion
```
