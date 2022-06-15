
# Node EdgeAngle

> Geometry node name: [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)<br>
  Blender type: [Edge Angle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgeAngle(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- unsigned_angle : Float
- signed_angle : Float
