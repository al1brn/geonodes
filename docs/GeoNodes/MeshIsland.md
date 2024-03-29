# Node MeshIsland

- Node name : 'Mesh Island'
- bl_idname : [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)


``` python
MeshIsland(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [mesh_island](/docs/GeoNodes/socket_GEOMETRY.md#mesh_island)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshIsland', node_label=node_label, node_color=node_color, **kwargs)
```
