# Node _3DCursor

- Node name : '3D Cursor'
- bl_idname : [GeometryNodeTool3DCursor](https://docs.blender.org/api/current/bpy.types.GeometryNodeTool3DCursor.html)


``` python
_3DCursor(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeTool3DCursor', node_label=node_label, node_color=node_color, **kwargs)
```
