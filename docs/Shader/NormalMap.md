# Node NormalMap

- Node name : 'Normal Map'
- bl_idname : [Normal Map](https://docs.blender.org/api/current/bpy.types.Normal Map.html)


``` python
NormalMap(strength=None, color=None, space='TANGENT', uv_map='', node_label=None, node_color=None)
```
##### Arguments

- strength : None
- color : None
- space : 'TANGENT'
- uv_map : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, strength=None, color=None, space='TANGENT', uv_map='', node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeNormalMap', node_label=node_label, node_color=node_color)

    self.space           = space
    self.uv_map          = uv_map
    self.strength        = strength
    self.color           = color
```
