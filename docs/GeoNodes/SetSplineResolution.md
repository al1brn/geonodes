# Node SetSplineResolution

- Node name : 'Set Spline Resolution'
- bl_idname : [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)


``` python
SetSplineResolution(geometry=None, selection=None, resolution=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- resolution : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [set_spline_resolution](/docs/GeoNodes/socket_GEOMETRY.md#set_spline_resolution) [spline_resolution](/docs/GeoNodes/socket_GEOMETRY.md#spline_resolution)

## Init

``` python
def __init__(self, geometry=None, selection=None, resolution=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetSplineResolution', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.selection       = selection
    self.resolution      = resolution
```
