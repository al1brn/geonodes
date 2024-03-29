# Node Gamma

- Node name : 'Gamma'
- bl_idname : [CompositorNodeGamma](https://docs.blender.org/api/current/bpy.types.CompositorNodeGamma.html)


``` python
Gamma(image=None, gamma=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- gamma : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, gamma=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeGamma', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.gamma           = gamma
```
