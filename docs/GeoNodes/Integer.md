# Node Integer

- Node name : 'Integer'
- bl_idname : [FunctionNodeInputInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)


``` python
Integer(integer=0, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- integer : 0

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, integer=0, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeInputInt', node_label=node_label, node_color=node_color, **kwargs)

    self.integer         = integer
```
