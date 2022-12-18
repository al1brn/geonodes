
# Node CornersOfFace

> Geometry node name: [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html)<br>
  Blender type: [Corners of Face](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CornersOfFace(face_index=None, weights=None, sort_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- face_index : Integer
- weights : Float
- sort_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- corner_index : Integer
- total : Integer
