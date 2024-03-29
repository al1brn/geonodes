# Node MaterialIndex

- Node name : 'Material Index'
- bl_idname : [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)


``` python
MaterialIndex(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [material_index](/docs/GeoNodes/socket_GEOMETRY.md#material_index)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMaterialIndex', node_label=node_label, node_color=node_color, **kwargs)
```
