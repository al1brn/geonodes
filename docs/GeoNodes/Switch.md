# Node Switch

- Node name : 'Switch'
- bl_idname : GeometryNodeSwitch


``` python
Switch(switch=None, false=None, true=None, input_type='GEOMETRY', node_label=None, node_color=None)
```
##### Arguments

- switch : None
- false : None
- true : None
- input_type : 'GEOMETRY'

## Implementation

- [Bool](/docs/GeoNodes/Bool.md) : [switch](/docs/GeoNodes/Bool.md#switch)
- [Col](/docs/GeoNodes/Col.md) : [switch](/docs/GeoNodes/Col.md#switch)
- [Collection](/docs/GeoNodes/Collection.md) : [switch](/docs/GeoNodes/Collection.md#switch)
- [Float](/docs/GeoNodes/Float.md) : [switch](/docs/GeoNodes/Float.md#switch)
- [Geometry](/docs/GeoNodes/Geometry.md) : [switch](/docs/GeoNodes/Geometry.md#switch)
- [Img](/docs/GeoNodes/Img.md) : [switch](/docs/GeoNodes/Img.md#switch)
- [Int](/docs/GeoNodes/Int.md) : [switch](/docs/GeoNodes/Int.md#switch)
- [Mat](/docs/GeoNodes/Mat.md) : [switch](/docs/GeoNodes/Mat.md#switch)
- [Object](/docs/GeoNodes/Object.md) : [switch](/docs/GeoNodes/Object.md#switch)
- [Rot](/docs/GeoNodes/Rot.md) : [switch](/docs/GeoNodes/Rot.md#switch)
- [Str](/docs/GeoNodes/Str.md) : [switch](/docs/GeoNodes/Str.md#switch)
- [Texture](/docs/GeoNodes/Texture.md) : [switch](/docs/GeoNodes/Texture.md#switch)
- [Vect](/docs/GeoNodes/Vect.md) : [switch](/docs/GeoNodes/Vect.md#switch)

## Init

``` python
def __init__(self, switch=None, false=None, true=None, input_type='GEOMETRY', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSwitch', node_label=node_label, node_color=node_color)

    self.input_type      = input_type
    self.switch          = switch
    self.false           = false
    self.true            = true
```
