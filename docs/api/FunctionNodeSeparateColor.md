# Node Separate Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
- geonodes name: `WNode`
- bl_idname: `FunctionNodeSeparateColor`

```python
from geonodes import nodes

node = nodes.SeparateColor(color=None, mode='RGB')
```

#### Input socket arguments:

- color: Color

#### Node parameter arguments:

- mode (str): Node parameter, default = 'RGB' in ('RGB', 'HSV', 'HSL')

#### Output sockets:

- **red** : Float
- **green** : Float
- **blue** : Float
- **alpha** : Float

