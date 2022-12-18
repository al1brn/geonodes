
# Node PointsToVertices

> Geometry node name: [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)<br>
  Blender type: [Points to Vertices](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.PointsToVertices(points=None, selection=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- points : Points
- selection : Boolean

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
