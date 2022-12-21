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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44cb50>>](Float.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44e3e0>>](Float.md#less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44d2d0>>](Float.md#less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44ebc0>>](Float.md#greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44f8e0>>](Float.md#greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44caf0>>](Float.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44d840>>](Float.md#not_equal)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44cbe0>>](Integer.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44cbb0>>](Integer.md#less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44cb80>>](Integer.md#less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44cac0>>](Integer.md#greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44d390>>](Integer.md#greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44d240>>](Integer.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44d210>>](Integer.md#not_equal)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e44eb90>>](String.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57c40>>](String.md#not_equal)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57c70>>](Vector.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57ca0>>](Vector.md#elements_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57cd0>>](Vector.md#elements_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57d00>>](Vector.md#elements_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57d30>>](Vector.md#elements_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57d60>>](Vector.md#elements_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57d90>>](Vector.md#elements_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57dc0>>](Vector.md#length_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57df0>>](Vector.md#length_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57e20>>](Vector.md#length_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57e50>>](Vector.md#length_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57e80>>](Vector.md#length_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57eb0>>](Vector.md#length_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57ee0>>](Vector.md#average_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57f10>>](Vector.md#average_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57f40>>](Vector.md#average_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57f70>>](Vector.md#average_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57fa0>>](Vector.md#average_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57fd0>>](Vector.md#average_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57c10>>](Vector.md#dot_product_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee577c0>>](Vector.md#dot_product_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57790>>](Vector.md#dot_product_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57760>>](Vector.md#dot_product_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57730>>](Vector.md#dot_product_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57700>>](Vector.md#dot_product_not_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee576d0>>](Vector.md#direction_less_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee576a0>>](Vector.md#direction_less_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57670>>](Vector.md#direction_greater_than)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57640>>](Vector.md#direction_greater_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57610>>](Vector.md#direction_equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee575e0>>](Vector.md#direction_not_equal)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee575b0>>](Color.md#compare)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57580>>](Color.md#darker)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57550>>](Color.md#brighter)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee57520>>](Color.md#equal)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee574f0>>](Color.md#equal)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e44dff0>>](function.md#compare)
