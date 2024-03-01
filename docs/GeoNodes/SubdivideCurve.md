# Node SubdivideCurve

- Node name : 'Subdivide Curve'
- bl_idname : [GeometryNodeSubdivideCurve](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
SubdivideCurve(curve=None, cuts=None, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- cuts : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [subdivide_curve](/docs/GeoNodes/Geometry.md#subdivide_curve)

## Init

``` python
def __init__(self, curve=None, cuts=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSubdivideCurve', node_label=node_label, node_color=node_color)

    self.curve           = curve
    self.cuts            = cuts
```
