
# Node PointsToVertices

> Geometry node name: [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/points_to_vertices.html)<br>
  Blender type: [Points to Vertices](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.PointsToVertices(points=None, selection=None, label=None)
```



## Arguments


### Input sockets

points : Points
- selection : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Points.md) [to_vertices](/docs/sockets/Points.md#to_vertices) : Method

