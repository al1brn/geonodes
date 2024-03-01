# Node CombineXYZ

- Node name : 'Combine XYZ'
- bl_idname : [ShaderNodeCombineXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)


``` python
CombineXYZ(x=None, y=None, z=None, node_label=None, node_color=None)
```
##### Arguments

- x : None
- y : None
- z : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, x=None, y=None, z=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeCombineXYZ', node_label=node_label, node_color=node_color)

    self.x               = x
    self.y               = y
    self.z               = z
```
