# Node Transform

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
- geonodes name: `Transform`
- bl_idname: `GeometryNodeTransform`

```python
from geonodes import nodes

node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None)
```

#### Input socket arguments:

- geometry: Geometry
- translation: Vector
- rotation: Vector
- scale: Vector

#### Output sockets:

- **geometry** : Geometry

