# Node FloatCurve

- Node name : 'Float Curve'
- bl_idname : [ShaderNodeFloatCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)


``` python
FloatCurve(factor=None, value=None, mapping=None, node_label=None, node_color=None)
```
##### Arguments

- factor : None
- value : None
- mapping : None

## Implementation

- [INT](/docs/GeoNodes/socket_INT.md) : [float_curve](/docs/GeoNodes/socket_INT.md#float_curve) [float_curve](/docs/GeoNodes/socket_INT.md#float_curve)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [float_curve](/docs/GeoNodes/socket_VALUE.md#float_curve) [float_curve](/docs/GeoNodes/socket_VALUE.md#float_curve)

## Init

``` python
def __init__(self, factor=None, value=None, mapping=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeFloatCurve', node_label=node_label, node_color=node_color)

    self.mapping         = mapping
    self.factor          = factor
    self.value           = value
```
