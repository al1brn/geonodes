# Node ConvexHull

- Node name : 'Convex Hull'
- bl_idname : [GeometryNodeConvexHull](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)


``` python
ConvexHull(geometry=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [convex_hull](/docs/GeoNodes/socket_GEOMETRY.md#convex_hull)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeConvexHull', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
```
