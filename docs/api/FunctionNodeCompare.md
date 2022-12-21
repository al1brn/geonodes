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

 - [compare](Float.md#compare)
 - [less_than](Float.md#less_than)
 - [less_equal](Float.md#less_equal)
 - [greater_than](Float.md#greater_than)
 - [greater_equal](Float.md#greater_equal)
 - [equal](Float.md#equal)
 - [not_equal](Float.md#not_equal)
#### class [Integer](Integer.md)

 - [compare](Integer.md#compare)
 - [less_than](Integer.md#less_than)
 - [less_equal](Integer.md#less_equal)
 - [greater_than](Integer.md#greater_than)
 - [greater_equal](Integer.md#greater_equal)
 - [equal](Integer.md#equal)
 - [not_equal](Integer.md#not_equal)
#### class [String](String.md)

 - [equal](String.md#equal)
 - [not_equal](String.md#not_equal)
#### class [Vector](Vector.md)

 - [compare](Vector.md#compare)
 - [elements_less_than](Vector.md#elements_less_than)
 - [elements_less_equal](Vector.md#elements_less_equal)
 - [elements_greater_than](Vector.md#elements_greater_than)
 - [elements_greater_equal](Vector.md#elements_greater_equal)
 - [elements_equal](Vector.md#elements_equal)
 - [elements_not_equal](Vector.md#elements_not_equal)
 - [length_less_than](Vector.md#length_less_than)
 - [length_less_equal](Vector.md#length_less_equal)
 - [length_greater_than](Vector.md#length_greater_than)
 - [length_greater_equal](Vector.md#length_greater_equal)
 - [length_equal](Vector.md#length_equal)
 - [length_not_equal](Vector.md#length_not_equal)
 - [average_less_than](Vector.md#average_less_than)
 - [average_less_equal](Vector.md#average_less_equal)
 - [average_greater_than](Vector.md#average_greater_than)
 - [average_greater_equal](Vector.md#average_greater_equal)
 - [average_equal](Vector.md#average_equal)
 - [average_not_equal](Vector.md#average_not_equal)
 - [dot_product_less_than](Vector.md#dot_product_less_than)
 - [dot_product_less_equal](Vector.md#dot_product_less_equal)
 - [dot_product_greater_than](Vector.md#dot_product_greater_than)
 - [dot_product_greater_equal](Vector.md#dot_product_greater_equal)
 - [dot_product_equal](Vector.md#dot_product_equal)
 - [dot_product_not_equal](Vector.md#dot_product_not_equal)
 - [direction_less_than](Vector.md#direction_less_than)
 - [direction_less_equal](Vector.md#direction_less_equal)
 - [direction_greater_than](Vector.md#direction_greater_than)
 - [direction_greater_equal](Vector.md#direction_greater_equal)
 - [direction_equal](Vector.md#direction_equal)
 - [direction_not_equal](Vector.md#direction_not_equal)
#### class [Color](Color.md)

 - [compare](Color.md#compare)
 - [darker](Color.md#darker)
 - [brighter](Color.md#brighter)
 - [equal](Color.md#equal)
 - [equal](Color.md#equal)
#### Global functions

 - [compare](function.md#compare)
