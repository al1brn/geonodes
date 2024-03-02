# Node Boolean

- Node name : 'Boolean'
- bl_idname : [FunctionNodeInputBool](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)


``` python
Boolean(boolean=False, node_label=None, node_color=None)
```
##### Arguments

- boolean : False

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, boolean=False, node_label=None, node_color=None):

    Node.__init__(self, 'FunctionNodeInputBool', node_label=node_label, node_color=node_color)

    self.boolean         = boolean
```