
# Node Compare

> Geometry node name: [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html)<br>
  Blender type: [Compare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None)
```



## Arguments


### Input sockets

a : data_type dependant
- b : data_type dependant
- c : Float
- angle : Float
- epsilon : Float

### Parameters

data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- mode : str (default = 'ELEMENT') in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- operation : str (default = 'GREATER_THAN') in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- Input sockets  : ['a', 'b']
- Output sockets : []   
  
  

## Output sockets

result : Boolean

## Data sockets

> Data socket classes implementing this node.
  
[class_name](docs/sockets/Color.md) [brighter](docs/sockets/Color.md#brighter) : Method
- [class_name](docs/sockets/Color.md) [darker](docs/sockets/Color.md#darker) : Method
- [class_name](docs/sockets/Color.md) [equal](docs/sockets/Color.md#equal) : Method
- [class_name](docs/sockets/Color.md) [not_equal](docs/sockets/Color.md#not_equal) : Method
- [class_name](docs/sockets/Float.md) [equal](docs/sockets/Float.md#equal) : Method
- [class_name](docs/sockets/Float.md) [greater_equal](docs/sockets/Float.md#greater_equal) : Method
- [class_name](docs/sockets/Float.md) [greater_than](docs/sockets/Float.md#greater_than) : Method
- [class_name](docs/sockets/Float.md) [less_equal](docs/sockets/Float.md#less_equal) : Method
- [class_name](docs/sockets/Float.md) [less_than](docs/sockets/Float.md#less_than) : Method
- [class_name](docs/sockets/Float.md) [not_equal](docs/sockets/Float.md#not_equal) : Method
- [class_name](docs/sockets/Integer.md) [equal](docs/sockets/Integer.md#equal) : Method
- [class_name](docs/sockets/Integer.md) [greater_equal](docs/sockets/Integer.md#greater_equal) : Method
- [class_name](docs/sockets/Integer.md) [greater_than](docs/sockets/Integer.md#greater_than) : Method
- [class_name](docs/sockets/Integer.md) [less_equal](docs/sockets/Integer.md#less_equal) : Method
- [class_name](docs/sockets/Integer.md) [less_than](docs/sockets/Integer.md#less_than) : Method
- [class_name](docs/sockets/Integer.md) [not_equal](docs/sockets/Integer.md#not_equal) : Method
- [class_name](docs/sockets/String.md) [average](docs/sockets/String.md#average) : Method
- [class_name](docs/sockets/String.md) [direction](docs/sockets/String.md#direction) : Method
- [class_name](docs/sockets/String.md) [dot_product](docs/sockets/String.md#dot_product) : Method
- [class_name](docs/sockets/String.md) [element](docs/sockets/String.md#element) : Method
- [class_name](docs/sockets/String.md) [length](docs/sockets/String.md#length) : Method
- [class_name](docs/sockets/Vector.md) [equal](docs/sockets/Vector.md#equal) : Method
- [class_name](docs/sockets/Vector.md) [greater_equal](docs/sockets/Vector.md#greater_equal) : Method
- [class_name](docs/sockets/Vector.md) [greater_than](docs/sockets/Vector.md#greater_than) : Method
- [class_name](docs/sockets/Vector.md) [less_equal](docs/sockets/Vector.md#less_equal) : Method
- [class_name](docs/sockets/Vector.md) [less_than](docs/sockets/Vector.md#less_than) : Method
- [class_name](docs/sockets/Vector.md) [not_equal](docs/sockets/Vector.md#not_equal) : Method
- [class_name](docs/sockets/functions.md) [compare](docs/sockets/functions.md#compare) : Function
  
