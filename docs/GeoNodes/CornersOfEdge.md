# Node CornersOfEdge

- Node name : 'Corners of Edge'
- bl_idname : [GeometryNodeCornersOfEdge](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
CornersOfEdge(edge_index=None, weights=None, sort_index=None, node_label=None, node_color=None)
```
##### Arguments

- edge_index : None
- weights : None
- sort_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [corners_of_edge](/docs/GeoNodes/Geometry.md#corners_of_edge)

## Init

``` python
def __init__(self, edge_index=None, weights=None, sort_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCornersOfEdge', node_label=node_label, node_color=node_color)

    self.edge_index      = edge_index
    self.weights         = weights
    self.sort_index      = sort_index
```
