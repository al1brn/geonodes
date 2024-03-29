# Node TrimCurve

- Node name : 'Trim Curve'
- bl_idname : [GeometryNodeTrimCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)


``` python
TrimCurve(curve=None, selection=None, start=None, end=None, mode='FACTOR', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- selection : None
- start : None
- end : None
- mode : 'FACTOR'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [trim_curve](/docs/GeoNodes/socket_GEOMETRY.md#trim_curve)

## Init

``` python
def __init__(self, curve=None, selection=None, start=None, end=None, mode='FACTOR', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeTrimCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
    self.start           = start
    self.end             = end
```
