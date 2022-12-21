# Node 'ColorRamp'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
- geonodes name: `ColorRamp`
- bl_idname: `ShaderNodeValToRGB`

```python
from geonodes import nodes

node = nodes.ColorRamp(fac=None)
```

### Args:

#### Input socket arguments:

- **fac**: [Float](Float.md)

### Output sockets:

- **color** : [Color](Color.md)
- **alpha** : [Float](Float.md)

## Implementation

### Global functions

| Name | Definition |
|------|------------|
 | [color_ramp](A.md#color_ramp) | `def color_ramp(fac=None):` |

### [Float](Float.md)

| Name | Definition |
|------|------------|
 | [color_ramp](Float.md#color_ramp-property) | `def color_ramp(self):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

