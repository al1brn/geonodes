# Node Composite

- Node name : 'Composite'
- bl_idname : [CompositorNodeComposite](https://docs.blender.org/api/current/bpy.types.CompositorNodeComposite.html)


``` python
Composite(image=None, alpha=None, tag_need_exec=None, use_alpha=True, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- alpha : None
- tag_need_exec : None
- use_alpha : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, alpha=None, tag_need_exec=None, use_alpha=True, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeComposite', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.use_alpha       = use_alpha
    self.image           = image
    self.alpha           = alpha
```
