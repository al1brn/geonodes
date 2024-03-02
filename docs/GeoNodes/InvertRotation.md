# Node InvertRotation

- Node name : 'Invert Rotation'
- bl_idname : [FunctionNodeInvertRotation](https://docs.blender.org/api/current/bpy.types.FunctionNodeInvertRotation.html)


``` python
InvertRotation(rotation=None, node_label=None, node_color=None)
```
##### Arguments

- rotation : None

## Implementation

- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [invert_rotation](/docs/GeoNodes/socket_ROTATION.md#invert_rotation) [invert_rotation](/docs/GeoNodes/socket_ROTATION.md#invert_rotation)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [invert_rotation](/docs/GeoNodes/socket_VECTOR.md#invert_rotation) [invert_rotation](/docs/GeoNodes/socket_VECTOR.md#invert_rotation)

## Init

``` python
def __init__(self, rotation=None, node_label=None, node_color=None):

    Node.__init__(self, 'FunctionNodeInvertRotation', node_label=node_label, node_color=node_color)

    self.rotation        = rotation
```
