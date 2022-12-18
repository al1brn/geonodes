
# Node FaceOfCorner

> Geometry node name: [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html)<br>
  Blender type: [Face of Corner](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FaceOfCorner(corner_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- corner_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- face_index : Integer
- index_in_face : Integer
