# Node SetPointRadius

- Node name : 'Set Point Radius'
- bl_idname : [Set Point Radius](https://docs.blender.org/api/current/bpy.types.Set Point Radius.html)


``` python
SetPointRadius(points=None, selection=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- points : None
- selection : None
- radius : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [point_radius](/docs/GeoNodes/Geometry.md#point_radius) [set_point_radius](/docs/GeoNodes/Geometry.md#set_point_radius)

## Init

``` python
def __init__(self, points=None, selection=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetPointRadius', node_label=node_label, node_color=node_color)

    self.points          = points
    self.selection       = selection
    self.radius          = radius
```
