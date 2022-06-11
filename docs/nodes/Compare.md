
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
  
[class_name](section:Data socket Color) [brighter](section:Data socket Color/brighter) : Method
- [class_name](section:Data socket Color) [darker](section:Data socket Color/darker) : Method
- [class_name](section:Data socket Color) [equal](section:Data socket Color/equal) : Method
- [class_name](section:Data socket Color) [not_equal](section:Data socket Color/not_equal) : Method
- [class_name](section:Data socket Float) [equal](section:Data socket Float/equal) : Method
- [class_name](section:Data socket Float) [greater_equal](section:Data socket Float/greater_equal) : Method
- [class_name](section:Data socket Float) [greater_than](section:Data socket Float/greater_than) : Method
- [class_name](section:Data socket Float) [less_equal](section:Data socket Float/less_equal) : Method
- [class_name](section:Data socket Float) [less_than](section:Data socket Float/less_than) : Method
- [class_name](section:Data socket Float) [not_equal](section:Data socket Float/not_equal) : Method
- [class_name](section:Data socket Integer) [equal](section:Data socket Integer/equal) : Method
- [class_name](section:Data socket Integer) [greater_equal](section:Data socket Integer/greater_equal) : Method
- [class_name](section:Data socket Integer) [greater_than](section:Data socket Integer/greater_than) : Method
- [class_name](section:Data socket Integer) [less_equal](section:Data socket Integer/less_equal) : Method
- [class_name](section:Data socket Integer) [less_than](section:Data socket Integer/less_than) : Method
- [class_name](section:Data socket Integer) [not_equal](section:Data socket Integer/not_equal) : Method
- [class_name](section:Data socket String) [average](section:Data socket String/average) : Method
- [class_name](section:Data socket String) [direction](section:Data socket String/direction) : Method
- [class_name](section:Data socket String) [dot_product](section:Data socket String/dot_product) : Method
- [class_name](section:Data socket String) [element](section:Data socket String/element) : Method
- [class_name](section:Data socket String) [length](section:Data socket String/length) : Method
- [class_name](section:Data socket Vector) [equal](section:Data socket Vector/equal) : Method
- [class_name](section:Data socket Vector) [greater_equal](section:Data socket Vector/greater_equal) : Method
- [class_name](section:Data socket Vector) [greater_than](section:Data socket Vector/greater_than) : Method
- [class_name](section:Data socket Vector) [less_equal](section:Data socket Vector/less_equal) : Method
- [class_name](section:Data socket Vector) [less_than](section:Data socket Vector/less_than) : Method
- [class_name](section:Data socket Vector) [not_equal](section:Data socket Vector/not_equal) : Method
- [class_name](section:Data socket functions) [compare](section:Data socket functions/compare) : Function
  
