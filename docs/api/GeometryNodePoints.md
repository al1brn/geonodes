# Node Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
- geonodes name: `Points`
- bl_idname: `GeometryNodePoints`

```python
from geonodes import nodes

node = nodes.Points(count=None, position=None, radius=None)
```

#### Input socket arguments:

- count: [Integer](Integer.md)
- position: [Vector](Vector.md)
- radius: [Float](Float.md)

#### Output sockets:

- **geometry** : [Geometry](Geometry

