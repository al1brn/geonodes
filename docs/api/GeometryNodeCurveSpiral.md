# Node Spiral

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
- geonodes name: `Spiral`
- bl_idname: `GeometryNodeCurveSpiral`

```python
from geonodes import nodes

node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```

#### Input socket arguments:

- resolution: [Integer](Integer.md)
- rotations: [Float](Float.md)
- start_radius: [Float](Float.md)
- end_radius: [Float](Float.md)
- height: [Float](Float.md)
- reverse: [Boolean](Boolean.md)

#### Output sockets:

- **curve** : [Curve](Curve

