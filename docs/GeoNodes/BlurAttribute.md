# Node BlurAttribute

- Node name : 'Blur Attribute'
- bl_idname : [GeometryNodeBlurAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)


``` python
BlurAttribute(value=None, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- value : None
- iterations : None
- weight : None
- data_type : 'FLOAT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [blur_attribute](/docs/GeoNodes/socket_GEOMETRY.md#blur_attribute)
- [INT](/docs/GeoNodes/socket_INT.md) : [blur_attribute](/docs/GeoNodes/socket_INT.md#blur_attribute)
- [RGBA](/docs/GeoNodes/socket_RGBA.md) : [blur_attribute](/docs/GeoNodes/socket_RGBA.md#blur_attribute)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [blur_attribute](/docs/GeoNodes/socket_VALUE.md#blur_attribute)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [blur_attribute](/docs/GeoNodes/socket_VECTOR.md#blur_attribute)

## Init

``` python
def __init__(self, value=None, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeBlurAttribute', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.value           = value
    self.iterations      = iterations
    self.weight          = weight
```
