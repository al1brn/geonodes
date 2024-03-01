# Node ResampleCurve

- Node name : 'Resample Curve'
- bl_idname : [Resample Curve](https://docs.blender.org/api/current/bpy.types.Resample Curve.html)


``` python
ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- count : None
- length : None
- mode : 'COUNT'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [resample_curve](/docs/GeoNodes/Geometry.md#resample_curve)

## Init

``` python
def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeResampleCurve', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
    self.count           = count
    self.length          = length
```
