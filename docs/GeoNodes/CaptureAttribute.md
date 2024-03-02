# Node CaptureAttribute

- Node name : 'Capture Attribute'
- bl_idname : [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)


``` python
CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- value : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [capture_attribute](/docs/GeoNodes/GEOMETRY.md#capture_attribute) [capture_attribute](/docs/GeoNodes/GEOMETRY.md#capture_attribute) [capture_boolean](/docs/GeoNodes/GEOMETRY.md#capture_boolean) [capture_boolean](/docs/GeoNodes/GEOMETRY.md#capture_boolean) [capture_color](/docs/GeoNodes/GEOMETRY.md#capture_color) [capture_color](/docs/GeoNodes/GEOMETRY.md#capture_color) [capture_float](/docs/GeoNodes/GEOMETRY.md#capture_float) [capture_float](/docs/GeoNodes/GEOMETRY.md#capture_float) [capture_int](/docs/GeoNodes/GEOMETRY.md#capture_int) [capture_int](/docs/GeoNodes/GEOMETRY.md#capture_int) [capture_quaternion](/docs/GeoNodes/GEOMETRY.md#capture_quaternion) [capture_quaternion](/docs/GeoNodes/GEOMETRY.md#capture_quaternion) [capture_vector](/docs/GeoNodes/GEOMETRY.md#capture_vector) [capture_vector](/docs/GeoNodes/GEOMETRY.md#capture_vector)

## Init

``` python
def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCaptureAttribute', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.value           = value
```
