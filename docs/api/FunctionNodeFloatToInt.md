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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57400>>](Float.md#to_integer)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee573d0>>](Float.md#round)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee573a0>>](Float.md#floor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57370>>](Float.md#ceiling)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57340>>](Float.md#truncate)
