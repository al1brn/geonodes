
# Node EdgeAngle

> Geometry node name: [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)<br>
  Blender type: [Edge Angle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------```python
from geonodes import nodes
node = nodes.EdgeAngle(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- unsigned_angle : Float
- signed_angle : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[capture_edge_angle](/docs/sockets/Mesh.md#capture_edge_angle) : Capture attribute
- [Mesh](/docs/sockets/Mesh.md).[corner_ID](/docs/sockets/Mesh.md#corner_id) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[corner_index](/docs/sockets/Mesh.md#corner_index) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[corner_porision](/docs/sockets/Mesh.md#corner_porision) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[edge_angle](/docs/sockets/Mesh.md#edge_angle) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[edge_unsigned_angle](/docs/sockets/Mesh.md#edge_unsigned_angle) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[egde_ID](/docs/sockets/Mesh.md#egde_id) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[egde_index](/docs/sockets/Mesh.md#egde_index) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[egde_position](/docs/sockets/Mesh.md#egde_position) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[face_ID](/docs/sockets/Mesh.md#face_id) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[face_index](/docs/sockets/Mesh.md#face_index) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[face_position](/docs/sockets/Mesh.md#face_position) : Attribute
  
