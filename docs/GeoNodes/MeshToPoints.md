# Node MeshToPoints

- Node name : 'Mesh to Points'
- bl_idname : [GeometryNodeMeshToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)


``` python
MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None
- position : None
- radius : None
- mode : 'VERTICES'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [mesh_to_points](/docs/GeoNodes/socket_GEOMETRY.md#mesh_to_points)

## Init

``` python
def __init__(self, mesh=None, selection=None, position=None, radius=None, mode='VERTICES', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshToPoints', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.mesh            = mesh
    self.selection       = selection
    self.position        = position
    self.radius          = radius
```
