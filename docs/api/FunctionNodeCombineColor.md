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

#### Input socket arguments:

- `red`: [Float](Float.md)
- `green`: [Float](Float.md)
- `blue`: [Float](Float.md)
- `alpha`: [Float](Float.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'RGB' in ('RGB', 'HSV', 'HSL')

#### Output sockets:

- **color** : [Color](Color.md)

