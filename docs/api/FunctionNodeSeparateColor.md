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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1640971f0>>](Color.md#rgb-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1640974f0>>](Color.md#hsv-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164097550>>](Color.md#hsl-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1640961d0>>](Color.md#alpha-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164096320>>](Color.md#red-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164096350>>](Color.md#green-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164097370>>](Color.md#blue-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164097400>>](Color.md#hue-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164097490>>](Color.md#saturation-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164097520>>](Color.md#value-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x164097670>>](Color.md#lightness-property)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164096110>>](function.md#separate_rgb)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1640974c0>>](function.md#separate_hsv)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x164097190>>](function.md#separate_hsl)
