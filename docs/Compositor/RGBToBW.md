# Node RGBToBW

- Node name : 'RGB to BW'
- bl_idname : [CompositorNodeRGBToBW](https://docs.blender.org/api/current/bpy.types.CompositorNodeRGBToBW.html)


``` python
RGBToBW(image=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeRGBToBW', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
    self.image           = image
```
