# Node BokehBlur

- Node name : 'Bokeh Blur'
- bl_idname : [CompositorNodeBokehBlur](https://docs.blender.org/api/current/bpy.types.CompositorNodeBokehBlur.html)


``` python
BokehBlur(image=None, bokeh=None, size=None, bounding_box=None, blur_max=16.0, tag_need_exec=None, use_extended_bounds=False, use_variable_size=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- bokeh : None
- size : None
- bounding_box : None
- blur_max : 16.0
- tag_need_exec : None
- use_extended_bounds : False
- use_variable_size : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, bokeh=None, size=None, bounding_box=None, blur_max=16.0, tag_need_exec=None, use_extended_bounds=False, use_variable_size=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeBokehBlur', node_label=node_label, node_color=node_color, **kwargs)

    self.blur_max        = blur_max
    self.tag_need_exec   = tag_need_exec
    self.use_extended_bounds = use_extended_bounds
    self.use_variable_size = use_variable_size
    self.image           = image
    self.bokeh           = bokeh
    self.size            = size
    self.bounding_box    = bounding_box
```
