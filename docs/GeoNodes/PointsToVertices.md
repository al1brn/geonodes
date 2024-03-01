# Node PointsToVertices

- Node name : 'Points to Vertices'
- bl_idname : GeometryNodePointsToVertices


``` python
PointsToVertices(points=None, selection=None, node_label=None, node_color=None)
```
##### Arguments

- points : None
- selection : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [points_to_vertices](/docs/GeoNodes/Geometry.md#points_to_vertices)

## Init

``` python
def __init__(self, points=None, selection=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodePointsToVertices', node_label=node_label, node_color=node_color)

    self.points          = points
    self.selection       = selection
```
