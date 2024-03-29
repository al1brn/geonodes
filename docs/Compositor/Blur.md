# Node Blur

- Node name : 'Blur'
- bl_idname : [CompositorNodeBlur](https://docs.blender.org/api/current/bpy.types.CompositorNodeBlur.html)


``` python
Blur(image=None, size=None, aspect_correction='NONE', factor=0.0, factor_x=0.0, factor_y=0.0, filter_type='GAUSS', size_x=0, size_y=0, tag_need_exec=None, use_bokeh=False, use_extended_bounds=False, use_gamma_correction=False, use_relative=False, use_variable_size=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- size : None
- aspect_correction : 'NONE'
- factor : 0.0
- factor_x : 0.0
- factor_y : 0.0
- filter_type : 'GAUSS'
- size_x : 0
- size_y : 0
- tag_need_exec : None
- use_bokeh : False
- use_extended_bounds : False
- use_gamma_correction : False
- use_relative : False
- use_variable_size : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, size=None, aspect_correction='NONE', factor=0.0, factor_x=0.0, factor_y=0.0, filter_type='GAUSS', size_x=0, size_y=0, tag_need_exec=None, use_bokeh=False, use_extended_bounds=False, use_gamma_correction=False, use_relative=False, use_variable_size=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeBlur', node_label=node_label, node_color=node_color, **kwargs)

    self.aspect_correction = aspect_correction
    self.factor          = factor
    self.factor_x        = factor_x
    self.factor_y        = factor_y
    self.filter_type     = filter_type
    self.size_x          = size_x
    self.size_y          = size_y
    self.tag_need_exec   = tag_need_exec
    self.use_bokeh       = use_bokeh
    self.use_extended_bounds = use_extended_bounds
    self.use_gamma_correction = use_gamma_correction
    self.use_relative    = use_relative
    self.use_variable_size = use_variable_size
    self.image           = image
    self.size            = size
```
