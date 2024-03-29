# Node ResampleCurve

- Node name : 'Resample Curve'
- bl_idname : [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)


``` python
ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- selection : None
- count : None
- length : None
- mode : 'COUNT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [resample_curve](/docs/GeoNodes/socket_GEOMETRY.md#resample_curve)

## Init

``` python
def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeResampleCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
    self.count           = count
    self.length          = length
```
