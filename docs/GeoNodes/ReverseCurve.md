# Node ReverseCurve

- Node name : 'Reverse Curve'
- bl_idname : [GeometryNodeReverseCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)


``` python
ReverseCurve(curve=None, selection=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curve : None
- selection : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [reverse_curve](/docs/GeoNodes/socket_GEOMETRY.md#reverse_curve)

## Init

``` python
def __init__(self, curve=None, selection=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeReverseCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.curve           = curve
    self.selection       = selection
```
