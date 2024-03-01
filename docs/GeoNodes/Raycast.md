# Node Raycast

- Node name : 'Raycast'
- bl_idname : [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', node_label=None, node_color=None)
```
##### Arguments

- target_geometry : None
- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- data_type : 'FLOAT'
- mapping : 'INTERPOLATED'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [raycast](/docs/GeoNodes/Geometry.md#raycast) [raycast_boolean](/docs/GeoNodes/Geometry.md#raycast_boolean) [raycast_color](/docs/GeoNodes/Geometry.md#raycast_color) [raycast_float](/docs/GeoNodes/Geometry.md#raycast_float) [raycast_int](/docs/GeoNodes/Geometry.md#raycast_int) [raycast_quaternion](/docs/GeoNodes/Geometry.md#raycast_quaternion) [raycast_vector](/docs/GeoNodes/Geometry.md#raycast_vector)

## Init

``` python
def __init__(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeRaycast', node_label=node_label, node_color=node_color)

    self.data_type       = data_type
    self.mapping         = mapping
    self.target_geometry = target_geometry
    self.attribute       = attribute
    self.source_position = source_position
    self.ray_direction   = ray_direction
    self.ray_length      = ray_length
```
