# Node SetCurveTilt

- Node name : 'Set Curve Tilt'
- bl_idname : [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)


``` python
SetCurveTilt(curve=None, selection=None, tilt=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- selection : None
- tilt : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [set_curve_tilt](/docs/GeoNodes/socket_GEOMETRY.md#set_curve_tilt) [tilt](/docs/GeoNodes/socket_GEOMETRY.md#tilt)

## Init

``` python
def __init__(self, curve=None, selection=None, tilt=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetCurveTilt', node_label=node_label, node_color=node_color, **kwargs)

    self.curve           = curve
    self.selection       = selection
    self.tilt            = tilt
```
