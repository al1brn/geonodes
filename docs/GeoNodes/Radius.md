# Node Radius

- Node name : 'Radius'
- bl_idname : [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)


``` python
Radius(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [radius](/docs/GeoNodes/socket_GEOMETRY.md#radius)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputRadius', node_label=node_label, node_color=node_color, **kwargs)
```
