# Node VectorDisplacement

- Node name : 'Vector Displacement'
- bl_idname : [ShaderNodeVectorDisplacement](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorDisplacement.html)


``` python
VectorDisplacement(vector=None, midlevel=None, scale=None, space='TANGENT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- midlevel : None
- scale : None
- space : 'TANGENT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, midlevel=None, scale=None, space='TANGENT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeVectorDisplacement', node_label=node_label, node_color=node_color, **kwargs)

    self.space           = space
    self.vector          = vector
    self.midlevel        = midlevel
    self.scale           = scale
```
