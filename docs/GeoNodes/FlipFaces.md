# Node FlipFaces

- Node name : 'Flip Faces'
- bl_idname : [GeometryNodeFlipFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)


``` python
FlipFaces(mesh=None, selection=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- selection : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [flip_faces](/docs/GeoNodes/socket_GEOMETRY.md#flip_faces)

## Init

``` python
def __init__(self, mesh=None, selection=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeFlipFaces', node_label=node_label, node_color=node_color, **kwargs)

    self.mesh            = mesh
    self.selection       = selection
```
