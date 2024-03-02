# Node SetPointRadius

- Node name : 'Set Point Radius'
- bl_idname : [GeometryNodeSetPointRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)


``` python
SetPointRadius(points=None, selection=None, radius=None, node_label=None, node_color=None)
```
##### Arguments

- points : None
- selection : None
- radius : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [point_radius](/docs/GeoNodes/GEOMETRY.md#point_radius) [point_radius](/docs/GeoNodes/GEOMETRY.md#point_radius) [set_point_radius](/docs/GeoNodes/GEOMETRY.md#set_point_radius) [set_point_radius](/docs/GeoNodes/GEOMETRY.md#set_point_radius)

## Init

``` python
def __init__(self, points=None, selection=None, radius=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetPointRadius', node_label=node_label, node_color=node_color)

    self.points          = points
    self.selection       = selection
    self.radius          = radius
```
