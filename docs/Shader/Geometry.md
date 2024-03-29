# Node Geometry

- Node name : 'Geometry'
- bl_idname : [ShaderNodeNewGeometry](https://docs.blender.org/api/current/bpy.types.ShaderNodeNewGeometry.html)


``` python
Geometry(node_label=None, node_color=None, **kwargs)
```
## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeNewGeometry', node_label=node_label, node_color=node_color, **kwargs)
```
