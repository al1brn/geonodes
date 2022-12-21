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

#### class [Color](Color.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16d4fb940>>](Color.md#RGB-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16d4fb910>>](Color.md#HSV-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16d4fb8e0>>](Color.md#HSL-classmethod)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb9d0>>](function.md#combine_rgb)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb9a0>>](function.md#combine_hsv)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb970>>](function.md#combine_hsl)
