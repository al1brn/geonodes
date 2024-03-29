# Node Translate

- Node name : 'Translate'
- bl_idname : [CompositorNodeTranslate](https://docs.blender.org/api/current/bpy.types.CompositorNodeTranslate.html)


``` python
Translate(image=None, x=None, y=None, tag_need_exec=None, use_relative=False, wrap_axis='NONE', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- x : None
- y : None
- tag_need_exec : None
- use_relative : False
- wrap_axis : 'NONE'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, x=None, y=None, tag_need_exec=None, use_relative=False, wrap_axis='NONE', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeTranslate', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.use_relative    = use_relative
    self.wrap_axis       = wrap_axis
    self.image           = image
    self.x               = x
    self.y               = y
```
