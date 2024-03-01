# Node ConvexHull

- Node name : 'Convex Hull'
- bl_idname : [Convex Hull](https://docs.blender.org/api/current/bpy.types.Convex Hull.html)


``` python
ConvexHull(geometry=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [convex_hull](/docs/GeoNodes/Geometry.md#convex_hull)

## Init

``` python
def __init__(self, geometry=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeConvexHull', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
```
