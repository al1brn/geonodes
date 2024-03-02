# Node MapRange

- Node name : 'Map Range'
- bl_idname : [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)


``` python
MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, vector=None, steps=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', node_label=None, node_color=None)
```
##### Arguments

- value : None
- from_min : None
- from_max : None
- to_min : None
- to_max : None
- vector : None
- steps : None
- clamp : True
- data_type : 'FLOAT'
- interpolation_type : 'LINEAR'

## Implementation

- [INT](/docs/GeoNodes/socket_INT.md) : [map_range](/docs/GeoNodes/socket_INT.md#map_range) [map_range](/docs/GeoNodes/socket_INT.md#map_range)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [map_range](/docs/GeoNodes/socket_VALUE.md#map_range) [map_range](/docs/GeoNodes/socket_VALUE.md#map_range)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [map_range](/docs/GeoNodes/socket_VECTOR.md#map_range) [map_range](/docs/GeoNodes/socket_VECTOR.md#map_range)

## Init

``` python
def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, vector=None, steps=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeMapRange', node_label=node_label, node_color=node_color)

    self.clamp           = clamp
    self.data_type       = data_type
    self.interpolation_type = interpolation_type
    self.value           = value
    self.from_min        = from_min
    self.from_max        = from_max
    self.to_min          = to_min
    self.to_max          = to_max
    self.vector          = vector
    self.steps           = steps
```