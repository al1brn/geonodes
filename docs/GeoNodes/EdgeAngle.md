# Node EdgeAngle

- Node name : 'Edge Angle'
- bl_idname : [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)


``` python
EdgeAngle(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edge_angle](/docs/GeoNodes/socket_GEOMETRY.md#edge_angle)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshEdgeAngle', node_label=node_label, node_color=node_color, **kwargs)
```
