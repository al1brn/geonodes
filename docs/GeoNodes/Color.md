# Node Color

- Node name : 'Color'
- bl_idname : [FunctionNodeInputColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)


``` python
Color(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeInputColor', node_label=node_label, node_color=node_color, **kwargs)
```
