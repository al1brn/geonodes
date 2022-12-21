# Node Points to Vertices

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
- geonodes name: `PointsToVertices`
- bl_idname: `GeometryNodePointsToVertices`

```python
from geonodes import nodes

node = nodes.PointsToVertices(points=None, selection=None)
```

#### Input socket arguments:

- points: [Points[Points.md]
- selection: [Boolean[Boolean.md]

#### Output sockets:

- **mesh** : Mesh

