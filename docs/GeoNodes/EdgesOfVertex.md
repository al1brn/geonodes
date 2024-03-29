# Node EdgesOfVertex

- Node name : 'Edges of Vertex'
- bl_idname : [GeometryNodeEdgesOfVertex](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)


``` python
EdgesOfVertex(vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vertex_index : None
- weights : None
- sort_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [edges_of_vertex](/docs/GeoNodes/socket_GEOMETRY.md#edges_of_vertex)

## Init

``` python
def __init__(self, vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeEdgesOfVertex', node_label=node_label, node_color=node_color, **kwargs)

    self.vertex_index    = vertex_index
    self.weights         = weights
    self.sort_index      = sort_index
```
