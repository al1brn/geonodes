# Node Star

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurveStar`

```python
from geonodes import nodes

node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None)
```

#### Input socket arguments:

- points: Integer
- inner_radius: Float
- outer_radius: Float
- twist: Float

#### Output sockets:

- **curve** : Curve
- **outer_points** : Boolean

