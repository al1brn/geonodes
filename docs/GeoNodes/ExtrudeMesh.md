# Node ExtrudeMesh

- Node name : 'Extrude Mesh'
- bl_idname : [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)


``` python
ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None
- offset : None
- offset_scale : None
- individual : None
- mode : 'FACES'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [extrude_mesh](/docs/GeoNodes/socket_GEOMETRY.md#extrude_mesh)

## Init

``` python
def __init__(self, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeExtrudeMesh', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.mesh            = mesh
    self.selection       = selection
    self.offset          = offset
    self.offset_scale    = offset_scale
    self.individual      = individual
```
