# Node SampleCurve

- Node name : 'Sample Curve'
- bl_idname : [GeometryNodeSampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)


``` python
SampleCurve(curves=None, value=None, factor=None, curve_index=None, length=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- curves : None
- value : None
- factor : None
- curve_index : None
- length : None
- data_type : 'FLOAT'
- mode : 'FACTOR'
- use_all_curves : False

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [sample_curve](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve) [sample_curve_boolean](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_boolean) [sample_curve_boolean_factor](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_boolean_factor) [sample_curve_boolean_length](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_boolean_length) [sample_curve_color](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_color) [sample_curve_color_factor](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_color_factor) [sample_curve_color_length](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_color_length) [sample_curve_float](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_float) [sample_curve_float_factor](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_float_factor) [sample_curve_float_length](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_float_length) [sample_curve_int](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_int) [sample_curve_int_factor](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_int_factor) [sample_curve_int_length](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_int_length) [sample_curve_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_quaternion) [sample_curve_quaternion_factor](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_quaternion_factor) [sample_curve_quaternion_length](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_quaternion_length) [sample_curve_vector](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_vector) [sample_curve_vector_factor](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_vector_factor) [sample_curve_vector_length](/docs/GeoNodes/socket_GEOMETRY.md#sample_curve_vector_length)

## Init

``` python
def __init__(self, curves=None, value=None, factor=None, curve_index=None, length=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSampleCurve', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.mode            = mode
    self.use_all_curves  = use_all_curves
    self.curves          = curves
    self.value           = value
    self.factor          = factor
    self.curve_index     = curve_index
    self.length          = length
```
