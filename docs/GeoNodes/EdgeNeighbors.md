# Node EdgeNeighbors

- Node name : 'Edge Neighbors'
- bl_idname : [GeometryNodeInputMeshEdgeNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)


``` python
EdgeNeighbors(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edge_neighbors](/docs/GeoNodes/socket_GEOMETRY.md#edge_neighbors)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshEdgeNeighbors', node_label=node_label, node_color=node_color, **kwargs)
```
