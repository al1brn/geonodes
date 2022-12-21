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

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dc3d0>>](Float.md#to_integer)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd990>>](Float.md#round)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3ddc30>>](Float.md#floor)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd840>>](Float.md#ceiling)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dcb20>>](Float.md#truncate)
