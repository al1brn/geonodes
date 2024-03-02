# Node ShortestEdgePaths

- Node name : 'Shortest Edge Paths'
- bl_idname : [GeometryNodeInputShortestEdgePaths](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)


``` python
ShortestEdgePaths(end_vertex=None, edge_cost=None, node_label=None, node_color=None)
```
##### Arguments

- end_vertex : None
- edge_cost : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [shortest_edge_paths](/docs/GeoNodes/socket_GEOMETRY.md#shortest_edge_paths) [shortest_edge_paths](/docs/GeoNodes/socket_GEOMETRY.md#shortest_edge_paths)

## Init

``` python
def __init__(self, end_vertex=None, edge_cost=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputShortestEdgePaths', node_label=node_label, node_color=node_color)

    self.end_vertex      = end_vertex
    self.edge_cost       = edge_cost
```
