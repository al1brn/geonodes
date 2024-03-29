# Node PointsToVertices

- Node name : 'Points to Vertices'
- bl_idname : [GeometryNodePointsToVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)


``` python
PointsToVertices(points=None, selection=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- points : None
- selection : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [points_to_vertices](/docs/GeoNodes/socket_GEOMETRY.md#points_to_vertices)

## Init

``` python
def __init__(self, points=None, selection=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodePointsToVertices', node_label=node_label, node_color=node_color, **kwargs)

    self.points          = points
    self.selection       = selection
```
