# Node SetPointRadius

- Node name : 'Set Point Radius'
- bl_idname : [GeometryNodeSetPointRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)


``` python
SetPointRadius(points=None, selection=None, radius=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- points : None
- selection : None
- radius : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [point_radius](/docs/GeoNodes/socket_GEOMETRY.md#point_radius) [set_point_radius](/docs/GeoNodes/socket_GEOMETRY.md#set_point_radius)

## Init

``` python
def __init__(self, points=None, selection=None, radius=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetPointRadius', node_label=node_label, node_color=node_color, **kwargs)

    self.points          = points
    self.selection       = selection
    self.radius          = radius
```
