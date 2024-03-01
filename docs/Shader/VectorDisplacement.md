# Node VectorDisplacement

- Node name : 'Vector Displacement'
- bl_idname : [Vector Displacement](https://docs.blender.org/api/current/bpy.types.Vector Displacement.html)


``` python
VectorDisplacement(vector=None, midlevel=None, scale=None, space='TANGENT', node_label=None, node_color=None)
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
def __init__(self, vector=None, midlevel=None, scale=None, space='TANGENT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeVectorDisplacement', node_label=node_label, node_color=node_color)

    self.space           = space
    self.vector          = vector
    self.midlevel        = midlevel
    self.scale           = scale
```
