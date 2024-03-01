# Node CornersOfVertex

- Node name : 'Corners of Vertex'
- bl_idname : [Corners of Vertex](https://docs.blender.org/api/current/bpy.types.Corners of Vertex.html)


``` python
CornersOfVertex(vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None)
```
##### Arguments

- vertex_index : None
- weights : None
- sort_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [corners_of_vertex](/docs/GeoNodes/Geometry.md#corners_of_vertex)

## Init

``` python
def __init__(self, vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCornersOfVertex', node_label=node_label, node_color=node_color)

    self.vertex_index    = vertex_index
    self.weights         = weights
    self.sort_index      = sort_index
```
