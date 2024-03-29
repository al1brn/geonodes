# Node ID

- Node name : 'ID'
- bl_idname : [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)


``` python
ID(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [id](/docs/GeoNodes/socket_GEOMETRY.md#id)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputID', node_label=node_label, node_color=node_color, **kwargs)
```
