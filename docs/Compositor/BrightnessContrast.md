# Node BrightnessContrast

- Node name : 'Brightness/Contrast'
- bl_idname : [CompositorNodeBrightContrast](https://docs.blender.org/api/current/bpy.types.CompositorNodeBrightContrast.html)


``` python
BrightnessContrast(image=None, bright=None, contrast=None, tag_need_exec=None, use_premultiply=True, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- bright : None
- contrast : None
- tag_need_exec : None
- use_premultiply : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, bright=None, contrast=None, tag_need_exec=None, use_premultiply=True, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeBrightContrast', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.use_premultiply = use_premultiply
    self.image           = image
    self.bright          = bright
    self.contrast        = contrast
```
