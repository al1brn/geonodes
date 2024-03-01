# Node _3DCursor

- Node name : '3D Cursor'
- bl_idname : [3D Cursor](https://docs.blender.org/api/current/bpy.types.3D Cursor.html)


``` python
_3DCursor(node_label=None, node_color=None)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeTool3DCursor', node_label=node_label, node_color=node_color)
```
