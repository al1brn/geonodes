# Node VertexNeighbors

- Node name : 'Vertex Neighbors'
- bl_idname : [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)


``` python
VertexNeighbors(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [vertex_neighbors](/docs/GeoNodes/socket_GEOMETRY.md#vertex_neighbors)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshVertexNeighbors', node_label=node_label, node_color=node_color, **kwargs)
```
