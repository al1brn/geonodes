# Node Normal

- Node name : 'Normal'
- bl_idname : [ShaderNodeNormal](https://docs.blender.org/api/current/bpy.types.ShaderNodeNormal.html)


``` python
Normal(normal=None, node_label=None, node_color=None)
```
##### Arguments

- normal : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, normal=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeNormal', node_label=node_label, node_color=node_color)

    self.normal          = normal
```
