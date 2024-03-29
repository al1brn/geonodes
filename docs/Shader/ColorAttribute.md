# Node ColorAttribute

- Node name : 'Color Attribute'
- bl_idname : [ShaderNodeVertexColor](https://docs.blender.org/api/current/bpy.types.ShaderNodeVertexColor.html)


``` python
ColorAttribute(layer_name='', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- layer_name : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, layer_name='', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVertexColor', node_label=node_label, node_color=node_color, **kwargs)

    self.layer_name      = layer_name
```
