# Node Texture

- Node name : 'Texture'
- bl_idname : CompositorNodeTexture


``` python
Texture(offset=None, scale=None, node_output=0, tag_need_exec=None, texture=None, node_label=None, node_color=None)
```
##### Arguments

- offset : None
- scale : None
- node_output : 0
- tag_need_exec : None
- texture : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, offset=None, scale=None, node_output=0, tag_need_exec=None, texture=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeTexture', node_label=node_label, node_color=node_color)

    self.node_output     = node_output
    self.tag_need_exec   = tag_need_exec
    self.texture         = texture
    self.offset          = offset
    self.scale           = scale
```
