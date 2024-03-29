# Node SetCurveNormal

- Node name : 'Set Curve Normal'
- bl_idname : [GeometryNodeSetCurveNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)


``` python
SetCurveNormal(curve=None, selection=None, normal=None, mode='MINIMUM_TWIST', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- selection : None
- normal : None
- mode : 'MINIMUM_TWIST'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [normal](/docs/GeoNodes/socket_GEOMETRY.md#normal) [set_curve_normal](/docs/GeoNodes/socket_GEOMETRY.md#set_curve_normal)

## Init

``` python
def __init__(self, curve=None, selection=None, normal=None, mode='MINIMUM_TWIST', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetCurveNormal', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
    self.normal          = normal
```
