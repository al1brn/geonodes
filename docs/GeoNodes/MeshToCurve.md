# Node MeshToCurve

- Node name : 'Mesh to Curve'
- bl_idname : [GeometryNodeMeshToCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)


``` python
MeshToCurve(mesh=None, selection=None, node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- selection : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [mesh_to_curve](/docs/GeoNodes/Geometry.md#mesh_to_curve)

## Init

``` python
def __init__(self, mesh=None, selection=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshToCurve', node_label=node_label, node_color=node_color)

    self.mesh            = mesh
    self.selection       = selection
```
