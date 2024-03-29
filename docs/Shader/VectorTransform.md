# Node VectorTransform

- Node name : 'Vector Transform'
- bl_idname : [ShaderNodeVectorTransform](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorTransform.html)


``` python
VectorTransform(vector=None, convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- convert_from : 'WORLD'
- convert_to : 'OBJECT'
- vector_type : 'VECTOR'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVectorTransform', node_label=node_label, node_color=node_color, **kwargs)

    self.convert_from    = convert_from
    self.convert_to      = convert_to
    self.vector_type     = vector_type
    self.vector          = vector
```
