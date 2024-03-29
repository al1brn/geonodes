# Node Position

- Node name : 'Position'
- bl_idname : [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)


``` python
Position(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [position](/docs/GeoNodes/socket_GEOMETRY.md#position)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputPosition', node_label=node_label, node_color=node_color, **kwargs)
```
