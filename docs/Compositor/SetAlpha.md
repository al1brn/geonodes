# Node SetAlpha

- Node name : 'Set Alpha'
- bl_idname : CompositorNodeSetAlpha


``` python
SetAlpha(image=None, alpha=None, mode='APPLY', tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- alpha : None
- mode : 'APPLY'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, alpha=None, mode='APPLY', tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeSetAlpha', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.alpha           = alpha
```
