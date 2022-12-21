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

#### Global functions

 - [compare](A.md#compare)
  ```python
  nodes.Compare(a=a, b=b, c=c, angle=angle, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation  ```

#### [Color](Color.md)

 - [compare](Color.md#compare)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='COLOR', mode='ELEMENT', operation=operation  ```

 - [darker](Color.md#darker)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='COLOR', mode='ELEMENT', operation='DARKER'  ```

 - [brighter](Color.md#brighter)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='COLOR', mode='ELEMENT', operation='BRIGHTER'  ```

 - [equal](Color.md#equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='COLOR', mode='ELEMENT', operation='EQUAL'  ```

 - [equal](Color.md#equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='COLOR', mode='ELEMENT', operation='EQUAL'  ```

#### [Float](Float.md)

 - [compare](Float.md#compare)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation=operation  ```

 - [less_than](Float.md#less_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN'  ```

 - [less_equal](Float.md#less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL'  ```

 - [greater_than](Float.md#greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'  ```

 - [greater_equal](Float.md#greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL'  ```

 - [equal](Float.md#equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL'  ```

 - [not_equal](Float.md#not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL'  ```

#### [Integer](Integer.md)

 - [compare](Integer.md#compare)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation=operation  ```

 - [less_than](Integer.md#less_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='LESS_THAN'  ```

 - [less_equal](Integer.md#less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL'  ```

 - [greater_than](Integer.md#greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='GREATER_THAN'  ```

 - [greater_equal](Integer.md#greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL'  ```

 - [equal](Integer.md#equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='EQUAL'  ```

 - [not_equal](Integer.md#not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL'  ```

#### [String](String.md)

 - [equal](String.md#equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='STRING', mode='ELEMENT', operation='EQUAL'  ```

 - [not_equal](String.md#not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL'  ```

#### [Vector](Vector.md)

 - [compare](Vector.md#compare)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation=operation  ```

 - [elements_less_than](Vector.md#elements_less_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN'  ```

 - [elements_less_equal](Vector.md#elements_less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL'  ```

 - [elements_greater_than](Vector.md#elements_greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN'  ```

 - [elements_greater_equal](Vector.md#elements_greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL'  ```

 - [elements_equal](Vector.md#elements_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='EQUAL'  ```

 - [elements_not_equal](Vector.md#elements_not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL'  ```

 - [length_less_than](Vector.md#length_less_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='LESS_THAN'  ```

 - [length_less_equal](Vector.md#length_less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='LESS_EQUAL'  ```

 - [length_greater_than](Vector.md#length_greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='GREATER_THAN'  ```

 - [length_greater_equal](Vector.md#length_greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='GREATER_EQUAL'  ```

 - [length_equal](Vector.md#length_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='EQUAL'  ```

 - [length_not_equal](Vector.md#length_not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='NOT_EQUAL'  ```

 - [average_less_than](Vector.md#average_less_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='LESS_THAN'  ```

 - [average_less_equal](Vector.md#average_less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='LESS_EQUAL'  ```

 - [average_greater_than](Vector.md#average_greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='GREATER_THAN'  ```

 - [average_greater_equal](Vector.md#average_greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='GREATER_EQUAL'  ```

 - [average_equal](Vector.md#average_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='EQUAL'  ```

 - [average_not_equal](Vector.md#average_not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='NOT_EQUAL'  ```

 - [dot_product_less_than](Vector.md#dot_product_less_than)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_THAN'  ```

 - [dot_product_less_equal](Vector.md#dot_product_less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_EQUAL'  ```

 - [dot_product_greater_than](Vector.md#dot_product_greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_THAN'  ```

 - [dot_product_greater_equal](Vector.md#dot_product_greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_EQUAL'  ```

 - [dot_product_equal](Vector.md#dot_product_equal)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='EQUAL'  ```

 - [dot_product_not_equal](Vector.md#dot_product_not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='NOT_EQUAL'  ```

 - [direction_less_than](Vector.md#direction_less_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='LESS_THAN'  ```

 - [direction_less_equal](Vector.md#direction_less_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='LESS_EQUAL'  ```

 - [direction_greater_than](Vector.md#direction_greater_than)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='GREATER_THAN'  ```

 - [direction_greater_equal](Vector.md#direction_greater_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='GREATER_EQUAL'  ```

 - [direction_equal](Vector.md#direction_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='EQUAL'  ```

 - [direction_not_equal](Vector.md#direction_not_equal)
  ```python
  nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='NOT_EQUAL'  ```

