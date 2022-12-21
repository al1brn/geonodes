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

### Args:

#### Input socket arguments:

- **float**: [Float](Float.md)

#### Node parameter arguments:

- **rounding_mode** (str): default = 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

### Output sockets:

- **integer** : [Integer](Integer.md)

## Implementation

#### class [Float](Float.md)

 - [to_integer](Float.md#to_integer)
 - [round](Float.md#round)
 - [floor](Float.md#floor)
 - [ceiling](Float.md#ceiling)
 - [truncate](Float.md#truncate)