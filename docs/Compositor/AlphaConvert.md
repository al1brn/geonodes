# Node AlphaConvert

- Node name : 'Alpha Convert'
- bl_idname : [CompositorNodePremulKey](https://docs.blender.org/api/current/bpy.types.CompositorNodePremulKey.html)


``` python
AlphaConvert(image=None, mapping='STRAIGHT_TO_PREMUL', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- mapping : 'STRAIGHT_TO_PREMUL'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, mapping='STRAIGHT_TO_PREMUL', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodePremulKey', node_label=node_label, node_color=node_color, **kwargs)

    self.mapping         = mapping
    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
