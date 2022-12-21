# Node Spiral

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurveSpiral`

```python
from geonodes import nodes

node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```

#### Input socket arguments:

- resolution: Integer
- rotations: Float
- start_radius: Float
- end_radius: Float
- height: Float
- reverse: Boolean

#### Output sockets:

- **curve** : Curve

