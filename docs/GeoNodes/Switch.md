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

- [BOOLEAN](/docs/GeoNodes/BOOLEAN.md) : [switch](/docs/GeoNodes/BOOLEAN.md#switch) [switch](/docs/GeoNodes/BOOLEAN.md#switch)
- [COLLECTION](/docs/GeoNodes/COLLECTION.md) : [switch](/docs/GeoNodes/COLLECTION.md#switch) [switch](/docs/GeoNodes/COLLECTION.md#switch)
- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [switch](/docs/GeoNodes/GEOMETRY.md#switch) [switch](/docs/GeoNodes/GEOMETRY.md#switch)
- [IMAGE](/docs/GeoNodes/IMAGE.md) : [switch](/docs/GeoNodes/IMAGE.md#switch) [switch](/docs/GeoNodes/IMAGE.md#switch)
- [INT](/docs/GeoNodes/INT.md) : [switch](/docs/GeoNodes/INT.md#switch) [switch](/docs/GeoNodes/INT.md#switch)
- [MATERIAL](/docs/GeoNodes/MATERIAL.md) : [switch](/docs/GeoNodes/MATERIAL.md#switch) [switch](/docs/GeoNodes/MATERIAL.md#switch)
- [OBJECT](/docs/GeoNodes/OBJECT.md) : [switch](/docs/GeoNodes/OBJECT.md#switch) [switch](/docs/GeoNodes/OBJECT.md#switch)
- [RGBA](/docs/GeoNodes/RGBA.md) : [switch](/docs/GeoNodes/RGBA.md#switch) [switch](/docs/GeoNodes/RGBA.md#switch)
- [ROTATION](/docs/GeoNodes/ROTATION.md) : [switch](/docs/GeoNodes/ROTATION.md#switch) [switch](/docs/GeoNodes/ROTATION.md#switch)
- [STRING](/docs/GeoNodes/STRING.md) : [switch](/docs/GeoNodes/STRING.md#switch) [switch](/docs/GeoNodes/STRING.md#switch)
- [TEXTURE](/docs/GeoNodes/TEXTURE.md) : [switch](/docs/GeoNodes/TEXTURE.md#switch) [switch](/docs/GeoNodes/TEXTURE.md#switch)
- [VALUE](/docs/GeoNodes/VALUE.md) : [switch](/docs/GeoNodes/VALUE.md#switch) [switch](/docs/GeoNodes/VALUE.md#switch)
- [VECTOR](/docs/GeoNodes/VECTOR.md) : [switch](/docs/GeoNodes/VECTOR.md#switch) [switch](/docs/GeoNodes/VECTOR.md#switch)

## Init

``` python
def __init__(self, switch=None, false=None, true=None, input_type='GEOMETRY', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSwitch', node_label=node_label, node_color=node_color)

    self.input_type      = input_type
    self.switch          = switch
    self.false           = false
    self.true            = true
```
