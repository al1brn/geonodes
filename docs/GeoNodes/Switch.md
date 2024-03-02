# Node Switch

- Node name : 'Switch'
- bl_idname : [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)


``` python
Switch(switch=None, false=None, true=None, input_type='GEOMETRY', node_label=None, node_color=None)
```
##### Arguments

- switch : None
- false : None
- true : None
- input_type : 'GEOMETRY'

## Implementation

- [BOOLEAN](/docs/GeoNodes/socket_BOOLEAN.md) : [switch](/docs/GeoNodes/socket_BOOLEAN.md#switch) [switch](/docs/GeoNodes/socket_BOOLEAN.md#switch)
- [COLLECTION](/docs/GeoNodes/socket_COLLECTION.md) : [switch](/docs/GeoNodes/socket_COLLECTION.md#switch) [switch](/docs/GeoNodes/socket_COLLECTION.md#switch)
- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [switch](/docs/GeoNodes/socket_GEOMETRY.md#switch) [switch](/docs/GeoNodes/socket_GEOMETRY.md#switch)
- [IMAGE](/docs/GeoNodes/socket_IMAGE.md) : [switch](/docs/GeoNodes/socket_IMAGE.md#switch) [switch](/docs/GeoNodes/socket_IMAGE.md#switch)
- [INT](/docs/GeoNodes/socket_INT.md) : [switch](/docs/GeoNodes/socket_INT.md#switch) [switch](/docs/GeoNodes/socket_INT.md#switch)
- [MATERIAL](/docs/GeoNodes/socket_MATERIAL.md) : [switch](/docs/GeoNodes/socket_MATERIAL.md#switch) [switch](/docs/GeoNodes/socket_MATERIAL.md#switch)
- [OBJECT](/docs/GeoNodes/socket_OBJECT.md) : [switch](/docs/GeoNodes/socket_OBJECT.md#switch) [switch](/docs/GeoNodes/socket_OBJECT.md#switch)
- [RGBA](/docs/GeoNodes/socket_RGBA.md) : [switch](/docs/GeoNodes/socket_RGBA.md#switch) [switch](/docs/GeoNodes/socket_RGBA.md#switch)
- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [switch](/docs/GeoNodes/socket_ROTATION.md#switch) [switch](/docs/GeoNodes/socket_ROTATION.md#switch)
- [STRING](/docs/GeoNodes/socket_STRING.md) : [switch](/docs/GeoNodes/socket_STRING.md#switch) [switch](/docs/GeoNodes/socket_STRING.md#switch)
- [TEXTURE](/docs/GeoNodes/socket_TEXTURE.md) : [switch](/docs/GeoNodes/socket_TEXTURE.md#switch) [switch](/docs/GeoNodes/socket_TEXTURE.md#switch)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [switch](/docs/GeoNodes/socket_VALUE.md#switch) [switch](/docs/GeoNodes/socket_VALUE.md#switch)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [switch](/docs/GeoNodes/socket_VECTOR.md#switch) [switch](/docs/GeoNodes/socket_VECTOR.md#switch)

## Init

``` python
def __init__(self, switch=None, false=None, true=None, input_type='GEOMETRY', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSwitch', node_label=node_label, node_color=node_color)

    self.input_type      = input_type
    self.switch          = switch
    self.false           = false
    self.true            = true
```
