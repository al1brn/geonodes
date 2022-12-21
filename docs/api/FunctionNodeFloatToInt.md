# Node Float to Integer

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
- geonodes name: `FloatToInteger`
- bl_idname: `FunctionNodeFloatToInt`

```python
from geonodes import nodes

node = nodes.FloatToInteger(float=None, rounding_mode='ROUND')
```

#### Input socket arguments:

- float: [Float[Float.md]

#### Node parameter arguments:

- rounding_mode (str): Node parameter, default = 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

#### Output sockets:

- **integer** : Integer

