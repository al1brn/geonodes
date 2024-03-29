# Node EdgeVertices

- Node name : 'Edge Vertices'
- bl_idname : [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)


``` python
EdgeVertices(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edge_vertices](/docs/GeoNodes/socket_GEOMETRY.md#edge_vertices)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshEdgeVertices', node_label=node_label, node_color=node_color, **kwargs)
```
