# Node *Compare*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
- geonodes name: `Compare`
- bl_idname: `FunctionNodeCompare`

```python
from geonodes import nodes

node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCompare.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Color](Color.md)** |
| [darker](Color.md#darker) | `def darker(self, b=None):` |
| [brighter](Color.md#brighter) | `def brighter(self, b=None):` |
| [equal](Color.md#equal) | `def equal(self, b=None, epsilon=None):` |
| [equal](Color.md#equal) | `def equal(self, b=None, epsilon=None):` |
| **[Float](Float.md)** |
| [compare](Float.md#compare) | `def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):` |
| [less_than](Float.md#less_than) | `def less_than(self, b=None):` |
| [less_equal](Float.md#less_equal) | `def less_equal(self, b=None):` |
| [greater_than](Float.md#greater_than) | `def greater_than(self, b=None):` |
| [greater_equal](Float.md#greater_equal) | `def greater_equal(self, b=None):` |
| [equal](Float.md#equal) | `def equal(self, b=None, epsilon=None):` |
| [not_equal](Float.md#not_equal) | `def not_equal(self, b=None, epsilon=None):` |
| **[Integer](Integer.md)** |
| [compare](Integer.md#compare) | `def compare(self, b=None, operation='GREATER_THAN'):` |
| [less_than](Integer.md#less_than) | `def less_than(self, b=None):` |
| [less_equal](Integer.md#less_equal) | `def less_equal(self, b=None):` |
| [greater_than](Integer.md#greater_than) | `def greater_than(self, b=None):` |
| [greater_equal](Integer.md#greater_equal) | `def greater_equal(self, b=None):` |
| [equal](Integer.md#equal) | `def equal(self, b=None):` |
| [not_equal](Integer.md#not_equal) | `def not_equal(self, b=None):` |
| **[String](String.md)** |
| [equal](String.md#equal) | `def equal(self, b=None):` |
| [not_equal](String.md#not_equal) | `def not_equal(self, b=None):` |
| **[Vector](Vector.md)** |
| [compare](Vector.md#compare) | `def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):` |
| [elements_less_than](Vector.md#elements_less_than) | `def elements_less_than(self, b=None):` |
| [elements_less_equal](Vector.md#elements_less_equal) | `def elements_less_equal(self, b=None):` |
| [elements_greater_than](Vector.md#elements_greater_than) | `def elements_greater_than(self, b=None):` |
| [elements_greater_equal](Vector.md#elements_greater_equal) | `def elements_greater_equal(self, b=None):` |
| [elements_equal](Vector.md#elements_equal) | `def elements_equal(self, b=None, epsilon=None):` |
| [elements_not_equal](Vector.md#elements_not_equal) | `def elements_not_equal(self, b=None, epsilon=None):` |
| [length_less_than](Vector.md#length_less_than) | `def length_less_than(self, b=None):` |
| [length_less_equal](Vector.md#length_less_equal) | `def length_less_equal(self, b=None):` |
| [length_greater_than](Vector.md#length_greater_than) | `def length_greater_than(self, b=None):` |
| [length_greater_equal](Vector.md#length_greater_equal) | `def length_greater_equal(self, b=None):` |
| [length_equal](Vector.md#length_equal) | `def length_equal(self, b=None, epsilon=None):` |
| [length_not_equal](Vector.md#length_not_equal) | `def length_not_equal(self, b=None, epsilon=None):` |
| [average_less_than](Vector.md#average_less_than) | `def average_less_than(self, b=None):` |
| [average_less_equal](Vector.md#average_less_equal) | `def average_less_equal(self, b=None):` |
| [average_greater_than](Vector.md#average_greater_than) | `def average_greater_than(self, b=None):` |
| [average_greater_equal](Vector.md#average_greater_equal) | `def average_greater_equal(self, b=None):` |
| [average_equal](Vector.md#average_equal) | `def average_equal(self, b=None, epsilon=None):` |
| [average_not_equal](Vector.md#average_not_equal) | `def average_not_equal(self, b=None, epsilon=None):` |
| [dot_product_less_than](Vector.md#dot_product_less_than) | `def dot_product_less_than(self, b=None, c=None):` |
| [dot_product_less_equal](Vector.md#dot_product_less_equal) | `def dot_product_less_equal(self, b=None, c=None):` |
| [dot_product_greater_than](Vector.md#dot_product_greater_than) | `def dot_product_greater_than(self, b=None, c=None):` |
| [dot_product_greater_equal](Vector.md#dot_product_greater_equal) | `def dot_product_greater_equal(self, b=None, c=None):` |
| [dot_product_equal](Vector.md#dot_product_equal) | `def dot_product_equal(self, b=None, c=None, epsilon=None):` |
| [dot_product_not_equal](Vector.md#dot_product_not_equal) | `def dot_product_not_equal(self, b=None, c=None, epsilon=None):` |
| [direction_less_than](Vector.md#direction_less_than) | `def direction_less_than(self, b=None, angle=None):` |
| [direction_less_equal](Vector.md#direction_less_equal) | `def direction_less_equal(self, b=None, angle=None):` |
| [direction_greater_than](Vector.md#direction_greater_than) | `def direction_greater_than(self, b=None, angle=None):` |
| [direction_greater_equal](Vector.md#direction_greater_equal) | `def direction_greater_equal(self, b=None, angle=None):` |
| [direction_equal](Vector.md#direction_equal) | `def direction_equal(self, b=None, angle=None, epsilon=None):` |
| [direction_not_equal](Vector.md#direction_not_equal) | `def direction_not_equal(self, b=None, angle=None, epsilon=None):` |
| Global functions |
| [compare](functions.md#compare) | `def compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):` |

<sub>Go to [top](#node-Compare) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

