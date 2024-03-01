# Node FaceArea

- Node name : 'Face Area'
- bl_idname : [GeometryNodeInputMeshFaceArea](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)


``` python
FaceArea(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [face_area](/docs/GeoNodes/Geometry.md#face_area)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputMeshFaceArea', node_label=node_label, node_color=node_color)
```
