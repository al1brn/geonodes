# Node Composite

- Node name : 'Composite'
- bl_idname : [Composite](https://docs.blender.org/api/current/bpy.types.Composite.html)


``` python
Composite(image=None, alpha=None, tag_need_exec=None, use_alpha=True, node_label=None, node_color=None)
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
def __init__(self, image=None, alpha=None, tag_need_exec=None, use_alpha=True, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeComposite', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.use_alpha       = use_alpha
    self.image           = image
    self.alpha           = alpha
```
