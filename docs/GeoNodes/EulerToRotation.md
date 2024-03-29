# Node EulerToRotation

- Node name : 'Euler to Rotation'
- bl_idname : [FunctionNodeEulerToRotation](https://docs.blender.org/api/current/bpy.types.FunctionNodeEulerToRotation.html)


``` python
EulerToRotation(euler=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- euler : None

## Implementation

- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [euler_to_rotation](/docs/GeoNodes/socket_VECTOR.md#euler_to_rotation)

## Init

``` python
def __init__(self, euler=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeEulerToRotation', node_label=node_label, node_color=node_color, **kwargs)

    self.euler           = euler
```
