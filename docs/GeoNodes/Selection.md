# Node Selection

- Node name : 'Selection'
- bl_idname : [GeometryNodeToolSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeToolSelection.html)


``` python
Selection(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeToolSelection', node_label=node_label, node_color=node_color, **kwargs)
```
