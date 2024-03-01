# Node CurveLength

- Node name : 'Curve Length'
- bl_idname : [Curve Length](https://docs.blender.org/api/current/bpy.types.Curve Length.html)


``` python
CurveLength(curve=None, node_label=None, node_color=None)
```
##### Arguments

- curve : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [curve_length](/docs/GeoNodes/Geometry.md#curve_length)

## Init

``` python
def __init__(self, curve=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveLength', node_label=node_label, node_color=node_color)

    self.curve           = curve
```
