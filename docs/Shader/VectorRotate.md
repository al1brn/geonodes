# Node VectorRotate

- Node name : 'Vector Rotate'
- bl_idname : [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)


``` python
VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- center : None
- axis : None
- angle : None
- rotation : None
- invert : False
- rotation_type : 'AXIS_ANGLE'

## Implementation

- [VECTOR](/docs/Shader/socket_VECTOR.md) : [vector_rotate](/docs/Shader/socket_VECTOR.md#vector_rotate)

## Init

``` python
def __init__(self, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVectorRotate', node_label=node_label, node_color=node_color, **kwargs)

    self.invert          = invert
    self.rotation_type   = rotation_type
    self.vector          = vector
    self.center          = center
    self.axis            = axis
    self.angle           = angle
    self.rotation        = rotation
```
