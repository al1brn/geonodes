# Node ColorRamp

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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dc430>>](Float.md#color_ramp-property)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc3a0>>](function.md#color_ramp)
