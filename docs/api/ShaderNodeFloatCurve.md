# Node *Float Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
- geonodes name: `FloatCurve`
- bl_idname: `ShaderNodeFloatCurve`

```python
from geonodes import nodes

node = nodes.FloatCurve(factor=None, value=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeFloatCurve.webp)

### Args:

#### Input socket arguments:

- **factor**: [Float](Float.md)
- **value**: [Float](Float.md)

### Output sockets:

- **value** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [float_curve](Float.md#float_curve) | `def float_curve(self, factor=None):` |

<sub>Go to [top](#node-Float-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

