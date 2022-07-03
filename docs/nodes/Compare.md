
# Node Compare

> Geometry node name: [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)<br>
  Blender type: [Compare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None, node_color=None)
```



## Arguments


### Input sockets

- a : data_type dependant
- b : data_type dependant
- c : Float
- angle : Float
- epsilon : Float

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- mode : str (default = 'ELEMENT') in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- operation : str (default = 'GREATER_THAN') in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- Input sockets  : ['a', 'b']
- Output sockets : []   
  
  

## Output sockets

- result : Boolean

## Data sockets

> Data socket classes implementing this node.
  
  
- [Color](/docs/sockets/Color.md).[brighter](/docs/sockets/Color.md#brighter) : Method
- [Color](/docs/sockets/Color.md).[darker](/docs/sockets/Color.md#darker) : Method
- [Color](/docs/sockets/Color.md).[equal](/docs/sockets/Color.md#equal) : Method
- [Color](/docs/sockets/Color.md).[not_equal](/docs/sockets/Color.md#not_equal) : Method
- [Float](/docs/sockets/Float.md).[equal](/docs/sockets/Float.md#equal) : Method
- [Float](/docs/sockets/Float.md).[greater_equal](/docs/sockets/Float.md#greater_equal) : Method
- [Float](/docs/sockets/Float.md).[greater_than](/docs/sockets/Float.md#greater_than) : Method
- [Float](/docs/sockets/Float.md).[less_equal](/docs/sockets/Float.md#less_equal) : Method
- [Float](/docs/sockets/Float.md).[less_than](/docs/sockets/Float.md#less_than) : Method
- [Float](/docs/sockets/Float.md).[not_equal](/docs/sockets/Float.md#not_equal) : Method
- [Integer](/docs/sockets/Integer.md).[equal](/docs/sockets/Integer.md#equal) : Method
- [Integer](/docs/sockets/Integer.md).[greater_equal](/docs/sockets/Integer.md#greater_equal) : Method
- [Integer](/docs/sockets/Integer.md).[greater_than](/docs/sockets/Integer.md#greater_than) : Method
- [Integer](/docs/sockets/Integer.md).[less_equal](/docs/sockets/Integer.md#less_equal) : Method
- [Integer](/docs/sockets/Integer.md).[less_than](/docs/sockets/Integer.md#less_than) : Method
- [Integer](/docs/sockets/Integer.md).[not_equal](/docs/sockets/Integer.md#not_equal) : Method
- [String](/docs/sockets/String.md).[equal](/docs/sockets/String.md#equal) : Method
- [String](/docs/sockets/String.md).[not_equal](/docs/sockets/String.md#not_equal) : Method
- [Vector](/docs/sockets/Vector.md).[average_equal](/docs/sockets/Vector.md#average_equal) : Method
- [Vector](/docs/sockets/Vector.md).[average_greater_equal](/docs/sockets/Vector.md#average_greater_equal) : Method
- [Vector](/docs/sockets/Vector.md).[average_greater_than](/docs/sockets/Vector.md#average_greater_than) : Method
- [Vector](/docs/sockets/Vector.md).[average_less_equal](/docs/sockets/Vector.md#average_less_equal) : Method
- [Vector](/docs/sockets/Vector.md).[average_less_than](/docs/sockets/Vector.md#average_less_than) : Method
- [Vector](/docs/sockets/Vector.md).[average_not_equal](/docs/sockets/Vector.md#average_not_equal) : Method
- [Vector](/docs/sockets/Vector.md).[direction_equal](/docs/sockets/Vector.md#direction_equal) : Method
- [Vector](/docs/sockets/Vector.md).[direction_greater_equal](/docs/sockets/Vector.md#direction_greater_equal) : Method
- [Vector](/docs/sockets/Vector.md).[direction_greater_than](/docs/sockets/Vector.md#direction_greater_than) : Method
- [Vector](/docs/sockets/Vector.md).[direction_less_equal](/docs/sockets/Vector.md#direction_less_equal) : Method
- [Vector](/docs/sockets/Vector.md).[direction_less_than](/docs/sockets/Vector.md#direction_less_than) : Method
- [Vector](/docs/sockets/Vector.md).[direction_not_equal](/docs/sockets/Vector.md#direction_not_equal) : Method
- [Vector](/docs/sockets/Vector.md).[dot_product_equal](/docs/sockets/Vector.md#dot_product_equal) : Method
- [Vector](/docs/sockets/Vector.md).[dot_product_greater_equal](/docs/sockets/Vector.md#dot_product_greater_equal) : Method
- [Vector](/docs/sockets/Vector.md).[dot_product_greater_than](/docs/sockets/Vector.md#dot_product_greater_than) : Method
- [Vector](/docs/sockets/Vector.md).[dot_product_less_equal](/docs/sockets/Vector.md#dot_product_less_equal) : Method
- [Vector](/docs/sockets/Vector.md).[dot_product_less_than](/docs/sockets/Vector.md#dot_product_less_than) : Method
- [Vector](/docs/sockets/Vector.md).[dot_product_not_equal](/docs/sockets/Vector.md#dot_product_not_equal) : Method
- [Vector](/docs/sockets/Vector.md).[element_equal](/docs/sockets/Vector.md#element_equal) : Method
- [Vector](/docs/sockets/Vector.md).[element_greater_equal](/docs/sockets/Vector.md#element_greater_equal) : Method
- [Vector](/docs/sockets/Vector.md).[element_greater_than](/docs/sockets/Vector.md#element_greater_than) : Method
- [Vector](/docs/sockets/Vector.md).[element_less_equal](/docs/sockets/Vector.md#element_less_equal) : Method
- [Vector](/docs/sockets/Vector.md).[element_less_than](/docs/sockets/Vector.md#element_less_than) : Method
- [Vector](/docs/sockets/Vector.md).[element_not_equal](/docs/sockets/Vector.md#element_not_equal) : Method
- [Vector](/docs/sockets/Vector.md).[equal](/docs/sockets/Vector.md#equal) : Method
- [Vector](/docs/sockets/Vector.md).[greater_equal](/docs/sockets/Vector.md#greater_equal) : Method
- [Vector](/docs/sockets/Vector.md).[greater_than](/docs/sockets/Vector.md#greater_than) : Method
- [Vector](/docs/sockets/Vector.md).[length_equal](/docs/sockets/Vector.md#length_equal) : Method
- [Vector](/docs/sockets/Vector.md).[length_greater_equal](/docs/sockets/Vector.md#length_greater_equal) : Method
- [Vector](/docs/sockets/Vector.md).[length_greater_than](/docs/sockets/Vector.md#length_greater_than) : Method
- [Vector](/docs/sockets/Vector.md).[length_less_equal](/docs/sockets/Vector.md#length_less_equal) : Method
- [Vector](/docs/sockets/Vector.md).[length_less_than](/docs/sockets/Vector.md#length_less_than) : Method
- [Vector](/docs/sockets/Vector.md).[length_not_equal](/docs/sockets/Vector.md#length_not_equal) : Method
- [Vector](/docs/sockets/Vector.md).[less_equal](/docs/sockets/Vector.md#less_equal) : Method
- [Vector](/docs/sockets/Vector.md).[less_than](/docs/sockets/Vector.md#less_than) : Method
- [Vector](/docs/sockets/Vector.md).[not_equal](/docs/sockets/Vector.md#not_equal) : Method
- [functions](/docs/sockets/functions.md).[compare](/docs/sockets/functions.md#compare) : Function
  
