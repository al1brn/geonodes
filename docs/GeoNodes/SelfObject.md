# Node SelfObject

- Node name : 'Self Object'
- bl_idname : [Self Object](https://docs.blender.org/api/current/bpy.types.Self Object.html)


``` python
SelfObject(node_label=None, node_color=None)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSelfObject', node_label=node_label, node_color=node_color)
```
