# Node RGBToBW

- Node name : 'RGB to BW'
- bl_idname : [ShaderNodeRGBToBW](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBToBW.html)


``` python
RGBToBW(color=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- color : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, color=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeRGBToBW', node_label=node_label, node_color=node_color, **kwargs)

    self.color           = color
```
