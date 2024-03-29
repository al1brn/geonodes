# Node CaptureAttribute

- Node name : 'Capture Attribute'
- bl_idname : [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)


``` python
CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- value : None
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [capture_attribute](/docs/GeoNodes/socket_GEOMETRY.md#capture_attribute) [capture_boolean](/docs/GeoNodes/socket_GEOMETRY.md#capture_boolean) [capture_color](/docs/GeoNodes/socket_GEOMETRY.md#capture_color) [capture_float](/docs/GeoNodes/socket_GEOMETRY.md#capture_float) [capture_int](/docs/GeoNodes/socket_GEOMETRY.md#capture_int) [capture_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#capture_quaternion) [capture_vector](/docs/GeoNodes/socket_GEOMETRY.md#capture_vector)

## Init

``` python
def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCaptureAttribute', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.value           = value
```
