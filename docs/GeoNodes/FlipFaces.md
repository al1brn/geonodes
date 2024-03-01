# Node FlipFaces

- Node name : 'Flip Faces'
- bl_idname : [GeometryNodeFlipFaces](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
FlipFaces(mesh=None, selection=None, node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- selection : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [flip_faces](/docs/GeoNodes/Geometry.md#flip_faces)

## Init

``` python
def __init__(self, mesh=None, selection=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeFlipFaces', node_label=node_label, node_color=node_color)

    self.mesh            = mesh
    self.selection       = selection
```
