# Node AlphaOver

- Node name : 'Alpha Over'
- bl_idname : [CompositorNodeAlphaOver](https://docs.blender.org/api/current/bpy.types.CompositorNodeAlphaOver.html)


``` python
AlphaOver(fac=None, image=None, image_1=None, premul=0.0, tag_need_exec=None, use_premultiply=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- image : None
- image_1 : None
- premul : 0.0
- tag_need_exec : None
- use_premultiply : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, image=None, image_1=None, premul=0.0, tag_need_exec=None, use_premultiply=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeAlphaOver', node_label=node_label, node_color=node_color, **kwargs)

    self.premul          = premul
    self.tag_need_exec   = tag_need_exec
    self.use_premultiply = use_premultiply
    self.fac             = fac
    self.image           = image
    self.image_1         = image_1
```
