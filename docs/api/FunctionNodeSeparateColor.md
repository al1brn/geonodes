# Node Separate Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
- geonodes name: `SeparateColor`
- bl_idname: `FunctionNodeSeparateColor`

```python
from geonodes import nodes

node = nodes.SeparateColor(color=None, mode='RGB')
```

### Args:

#### Input socket arguments:

- **color**: [Color](Color.md)

#### Node parameter arguments:

- **mode** (str): default = 'RGB' in ('RGB', 'HSV', 'HSL')

### Output sockets:

- **red** : [Float](Float.md)
- **green** : [Float](Float.md)
- **blue** : [Float](Float.md)
- **alpha** : [Float](Float.md)

## Implementation

#### class [Color](Color.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fafe0>>](Color.md#rgb-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fafb0>>](Color.md#hsv-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4faf80>>](Color.md#hsl-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4faf50>>](Color.md#alpha-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4faf20>>](Color.md#red-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4faef0>>](Color.md#green-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4faec0>>](Color.md#blue-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fae90>>](Color.md#hue-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fae60>>](Color.md#saturation-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fae30>>](Color.md#value-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fae00>>](Color.md#lightness-property)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb070>>](function.md#separate_rgb)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb040>>](function.md#separate_hsv)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb010>>](function.md#separate_hsl)
