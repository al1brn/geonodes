
# Node EdgeAngle

> Geometry node name: [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/edge_angle.html)<br>
  Blender type: [Edge Angle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgeAngle(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

unsigned_angle : Float
- signed_angle : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Mesh) [capture_edge_angle](section:Data socket Mesh/capture_edge_angle) : Capture attribute
- [class_name](section:Data socket Mesh) [corner_ID](section:Data socket Mesh/corner_ID) : Attribute
- [class_name](section:Data socket Mesh) [corner_index](section:Data socket Mesh/corner_index) : Attribute
- [class_name](section:Data socket Mesh) [corner_porision](section:Data socket Mesh/corner_porision) : Attribute
- [class_name](section:Data socket Mesh) [edge_angle](section:Data socket Mesh/edge_angle) : Attribute
- [class_name](section:Data socket Mesh) [edge_unsigned_angle](section:Data socket Mesh/edge_unsigned_angle) : Attribute
- [class_name](section:Data socket Mesh) [egde_ID](section:Data socket Mesh/egde_ID) : Attribute
- [class_name](section:Data socket Mesh) [egde_index](section:Data socket Mesh/egde_index) : Attribute
- [class_name](section:Data socket Mesh) [egde_position](section:Data socket Mesh/egde_position) : Attribute
- [class_name](section:Data socket Mesh) [face_ID](section:Data socket Mesh/face_ID) : Attribute
- [class_name](section:Data socket Mesh) [face_index](section:Data socket Mesh/face_index) : Attribute
- [class_name](section:Data socket Mesh) [face_position](section:Data socket Mesh/face_position) : Attribute
  
