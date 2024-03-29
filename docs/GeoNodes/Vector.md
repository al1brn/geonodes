# Node Vector

- Node name : 'Vector'
- bl_idname : [FunctionNodeInputVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)


``` python
Vector(vector=(0.0, 0.0, 0.0), node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : (0.0, 0.0, 0.0)

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=(0.0, 0.0, 0.0), node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeInputVector', node_label=node_label, node_color=node_color, **kwargs)

    self.vector          = vector
```
