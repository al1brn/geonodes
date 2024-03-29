# Node IsEdgeSmooth

- Node name : 'Is Edge Smooth'
- bl_idname : [GeometryNodeInputEdgeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputEdgeSmooth.html)


``` python
IsEdgeSmooth(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edge_smooth](/docs/GeoNodes/socket_GEOMETRY.md#edge_smooth)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputEdgeSmooth', node_label=node_label, node_color=node_color, **kwargs)
```
