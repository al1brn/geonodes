# Node Posterize

- Node name : 'Posterize'
- bl_idname : [CompositorNodePosterize](https://docs.blender.org/api/current/bpy.types.CompositorNodePosterize.html)


``` python
Posterize(image=None, steps=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- steps : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, steps=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodePosterize', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.steps           = steps
```
