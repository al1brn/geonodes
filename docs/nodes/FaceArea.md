
# Node FaceArea

> Geometry node name: [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html)<br>
  Blender type: [Face Area](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.FaceArea(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- area : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[capture_face_area](/docs/sockets/Mesh.md#capture_face_area) : Capture attribute
- [Mesh](/docs/sockets/Mesh.md).[face_area](/docs/sockets/Mesh.md#face_area) : Attribute
  
