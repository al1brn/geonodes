# Node Texture

- Node name : 'Texture'
- bl_idname : [CompositorNodeTexture](https://docs.blender.org/api/current/bpy.types.CompositorNodeTexture.html)


``` python
Texture(offset=None, scale=None, node_output=0, tag_need_exec=None, texture=None, node_label=None, node_color=None, **kwargs)
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
def __init__(self, offset=None, scale=None, node_output=0, tag_need_exec=None, texture=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeTexture', node_label=node_label, node_color=node_color, **kwargs)

    self.node_output     = node_output
    self.tag_need_exec   = tag_need_exec
    self.texture         = texture
    self.offset          = offset
    self.scale           = scale
```
