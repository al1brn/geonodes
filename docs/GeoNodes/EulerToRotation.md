# Node EulerToRotation

- Node name : 'Euler to Rotation'
- bl_idname : [Euler to Rotation](https://docs.blender.org/api/current/bpy.types.Euler to Rotation.html)


``` python
EulerToRotation(euler=None, node_label=None, node_color=None)
```
##### Arguments

- euler : None

## Implementation

- [Vect](/docs/GeoNodes/Vect.md) : [euler_to_rotation](/docs/GeoNodes/Vect.md#euler_to_rotation)

## Init

``` python
def __init__(self, euler=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeEulerToRotation', node_label=node_label, node_color=node_color)

    self.euler           = euler
```
