# Node FaceArea

- Node name : 'Face Area'
- bl_idname : [GeometryNodeInputMeshFaceArea](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)


``` python
FaceArea(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [face_area](/docs/GeoNodes/socket_GEOMETRY.md#face_area)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshFaceArea', node_label=node_label, node_color=node_color, **kwargs)
```
