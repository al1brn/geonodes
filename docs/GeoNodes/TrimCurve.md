# Node TrimCurve

- Node name : 'Trim Curve'
- bl_idname : [GeometryNodeTrimCurve](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
TrimCurve(curve=None, selection=None, start=None, end=None, mode='FACTOR', node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- start : None
- end : None
- mode : 'FACTOR'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [trim_curve](/docs/GeoNodes/Geometry.md#trim_curve)

## Init

``` python
def __init__(self, curve=None, selection=None, start=None, end=None, mode='FACTOR', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeTrimCurve', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
    self.start           = start
    self.end             = end
```
