# Node Mapping

- Node name : 'Mapping'
- bl_idname : [ShaderNodeMapping](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapping.html)


``` python
Mapping(vector=None, location=None, rotation=None, scale=None, vector_type='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- location : None
- rotation : None
- scale : None
- vector_type : 'POINT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, location=None, rotation=None, scale=None, vector_type='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeMapping', node_label=node_label, node_color=node_color, **kwargs)

    self.vector_type     = vector_type
    self.vector          = vector
    self.location        = location
    self.rotation        = rotation
    self.scale           = scale
```
