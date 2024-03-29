# Node Defocus

- Node name : 'Defocus'
- bl_idname : [CompositorNodeDefocus](https://docs.blender.org/api/current/bpy.types.CompositorNodeDefocus.html)


``` python
Defocus(image=None, z=None, angle=0.0, blur_max=16.0, bokeh='CIRCLE', f_stop=128.0, scene=None, tag_need_exec=None, threshold=1.0, use_gamma_correction=False, use_preview=True, use_zbuffer=False, z_scale=1.0, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- z : None
- angle : 0.0
- blur_max : 16.0
- bokeh : 'CIRCLE'
- f_stop : 128.0
- scene : None
- tag_need_exec : None
- threshold : 1.0
- use_gamma_correction : False
- use_preview : True
- use_zbuffer : False
- z_scale : 1.0

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, z=None, angle=0.0, blur_max=16.0, bokeh='CIRCLE', f_stop=128.0, scene=None, tag_need_exec=None, threshold=1.0, use_gamma_correction=False, use_preview=True, use_zbuffer=False, z_scale=1.0, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDefocus', node_label=node_label, node_color=node_color, **kwargs)

    self.angle           = angle
    self.blur_max        = blur_max
    self.bokeh           = bokeh
    self.f_stop          = f_stop
    self.scene           = scene
    self.tag_need_exec   = tag_need_exec
    self.threshold       = threshold
    self.use_gamma_correction = use_gamma_correction
    self.use_preview     = use_preview
    self.use_zbuffer     = use_zbuffer
    self.z_scale         = z_scale
    self.image           = image
    self.z               = z
```
