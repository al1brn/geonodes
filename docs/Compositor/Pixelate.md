# Node Pixelate

- Node name : 'Pixelate'
- bl_idname : [CompositorNodePixelate](https://docs.blender.org/api/current/bpy.types.CompositorNodePixelate.html)


``` python
Pixelate(color=None, tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- color : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, tag_need_exec=None, node_label=None, node_color=None):

    Node.__init__(self, 'CompositorNodePixelate', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.color           = color
```
