# Node Compare

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
- geonodes name: `Compare`
- bl_idname: `FunctionNodeCompare`

```python
from geonodes import nodes

node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
```

### Args:

#### Input socket arguments:

- **a**: **data_type** dependant
- **b**: **data_type** dependant
- **c**: [Float](Float.md)
- **angle**: [Float](Float.md)
- **epsilon**: [Float](Float.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- **mode** (str): default = 'ELEMENT' in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- **operation** (str): default = 'GREATER_THAN' in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')

### Output sockets:

- **result** : [Boolean](Boolean.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- Input sockets  : ['a', 'b']
- Output sockets : []
## Implementation

#### class [Float](Float.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3799c0>>](Float.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378940>>](Float.md#less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a5c0>>](Float.md#less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e379c90>>](Float.md#greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3786d0>>](Float.md#greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e379fc0>>](Float.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3784c0>>](Float.md#not_equal)
#### class [Integer](Integer.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3789a0>>](Integer.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37b4f0>>](Integer.md#less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a920>>](Integer.md#less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a710>>](Integer.md#greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a890>>](Integer.md#greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378850>>](Integer.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378910>>](Integer.md#not_equal)
#### class [String](String.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378580>>](String.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a7a0>>](String.md#not_equal)
#### class [Vector](Vector.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a6e0>>](Vector.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37b460>>](Vector.md#elements_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37b160>>](Vector.md#elements_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378220>>](Vector.md#elements_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3781c0>>](Vector.md#elements_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378070>>](Vector.md#elements_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378040>>](Vector.md#elements_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3780d0>>](Vector.md#length_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e379120>>](Vector.md#length_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e379150>>](Vector.md#length_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e379690>>](Vector.md#length_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e378be0>>](Vector.md#length_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37a2c0>>](Vector.md#length_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37ace0>>](Vector.md#average_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e37ad40>>](Vector.md#average_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de8f0>>](Vector.md#average_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de380>>](Vector.md#average_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de620>>](Vector.md#average_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de170>>](Vector.md#average_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dead0>>](Vector.md#dot_product_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfd60>>](Vector.md#dot_product_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfdc0>>](Vector.md#dot_product_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dfcd0>>](Vector.md#dot_product_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3ddff0>>](Vector.md#dot_product_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dc250>>](Vector.md#dot_product_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dc610>>](Vector.md#direction_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd0f0>>](Vector.md#direction_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd090>>](Vector.md#direction_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dcfd0>>](Vector.md#direction_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd000>>](Vector.md#direction_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df400>>](Vector.md#direction_not_equal)
#### class [Color](Color.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df640>>](Color.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dcc70>>](Color.md#darker)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3defb0>>](Color.md#brighter)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3def20>>](Color.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3ddcf0>>](Color.md#equal)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e37a4d0>>](function.md#compare)
