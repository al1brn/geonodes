# Node Tangent

- Node name : 'Tangent'
- bl_idname : [ShaderNodeTangent](https://docs.blender.org/api/current/bpy.types.ShaderNodeTangent.html)


``` python
Tangent(axis='Z', direction_type='RADIAL', uv_map='', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- axis : 'Z'
- direction_type : 'RADIAL'
- uv_map : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, axis='Z', direction_type='RADIAL', uv_map='', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTangent', node_label=node_label, node_color=node_color, **kwargs)

    self.axis            = axis
    self.direction_type  = direction_type
    self.uv_map          = uv_map
```
