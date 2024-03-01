# Node Value

- Node name : 'Value'
- bl_idname : [Value](https://docs.blender.org/api/current/bpy.types.Value.html)


``` python
Value(node_label=None, node_color=None)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeValue', node_label=node_label, node_color=node_color)
```
