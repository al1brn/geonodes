
# Node FaceSetBoundaries

> Geometry node name: [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html)<br>
  Blender type: [Face Set Boundaries](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FaceSetBoundaries(face_set=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- face_set : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- boundary_edges : Boolean
