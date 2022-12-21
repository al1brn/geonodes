# Node Curve Length

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
- geonodes name: `CurveLength`
- bl_idname: `GeometryNodeCurveLength`

```python
from geonodes import nodes

node = nodes.CurveLength(curve=None)
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)

### Output sockets:

- **length** : [Float](Float.md)

## Implementation

#### class [Curve](Curve.md)

 - [length](Curve.md#length-property)