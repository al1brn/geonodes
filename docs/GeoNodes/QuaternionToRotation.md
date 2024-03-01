# Node QuaternionToRotation

- Node name : 'Quaternion to Rotation'
- bl_idname : [FunctionNodeQuaternionToRotation](https://docs.blender.org/api/current/bpy.types.FunctionNodeQuaternionToRotation.html)


``` python
QuaternionToRotation(w=None, x=None, y=None, z=None, node_label=None, node_color=None)
```
##### Arguments

- w : None
- x : None
- y : None
- z : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, w=None, x=None, y=None, z=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'FunctionNodeQuaternionToRotation', node_label=node_label, node_color=node_color)

    self.w               = w
    self.x               = x
    self.y               = y
    self.z               = z
```
