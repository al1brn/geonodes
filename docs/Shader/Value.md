# Node Value

- Node name : 'Value'
- bl_idname : [ShaderNodeValue](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)


``` python
Value(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeValue', node_label=node_label, node_color=node_color, **kwargs)
```
