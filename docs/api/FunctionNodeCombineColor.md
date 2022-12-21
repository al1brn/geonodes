# Node Combine Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)
- geonodes name: `CombineColor`
- bl_idname: `FunctionNodeCombineColor`

```python
from geonodes import nodes

node = nodes.CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB')
```

### Args:

#### Input socket arguments:

- **red**: [Float](Float.md)
- **green**: [Float](Float.md)
- **blue**: [Float](Float.md)
- **alpha**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'RGB' in ('RGB', 'HSV', 'HSL')

### Output sockets:

- **color** : [Color](Color.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1639dc2b0>>](Color.md#RGB-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1639dc280>>](Color.md#HSV-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1639dc250>>](Color.md#HSL-classmethod)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc460>>](function.md#combine_rgb)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc820>>](function.md#combine_hsv)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1639dc7c0>>](function.md#combine_hsl)
