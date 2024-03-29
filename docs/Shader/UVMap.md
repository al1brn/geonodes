# Node UVMap

- Node name : 'UV Map'
- bl_idname : [ShaderNodeUVMap](https://docs.blender.org/api/current/bpy.types.ShaderNodeUVMap.html)


``` python
UVMap(from_instancer=False, uv_map='', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- from_instancer : False
- uv_map : ''

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, from_instancer=False, uv_map='', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeUVMap', node_label=node_label, node_color=node_color, **kwargs)

    self.from_instancer  = from_instancer
    self.uv_map          = uv_map
```
