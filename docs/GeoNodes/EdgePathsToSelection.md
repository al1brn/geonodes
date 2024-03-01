# Node EdgePathsToSelection

- Node name : 'Edge Paths to Selection'
- bl_idname : [GeometryNodeEdgePathsToSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)


``` python
EdgePathsToSelection(start_vertices=None, next_vertex_index=None, node_label=None, node_color=None)
```
##### Arguments

- start_vertices : None
- next_vertex_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [edge_paths_to_selection](/docs/GeoNodes/Geometry.md#edge_paths_to_selection)

## Init

``` python
def __init__(self, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeEdgePathsToSelection', node_label=node_label, node_color=node_color)

    self.start_vertices  = start_vertices
    self.next_vertex_index = next_vertex_index
```
