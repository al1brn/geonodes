# Node EdgesOfVertex

- Node name : 'Edges of Vertex'
- bl_idname : [GeometryNodeEdgesOfVertex](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
EdgesOfVertex(vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None)
```
##### Arguments

- vertex_index : None
- weights : None
- sort_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [edges_of_vertex](/docs/GeoNodes/Geometry.md#edges_of_vertex)

## Init

``` python
def __init__(self, vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeEdgesOfVertex', node_label=node_label, node_color=node_color)

    self.vertex_index    = vertex_index
    self.weights         = weights
    self.sort_index      = sort_index
```
