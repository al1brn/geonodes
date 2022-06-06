
# Class Compare

> Geometry node name: _'Compare'_<br>Blender type:  **FunctionNodeCompare**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None)
```


### Arguments


#### Input sockets



- **a** : **data_type** dependant
- **b** : **data_type** dependant
- **c** : _Float_
- **angle** : _Float_
- **epsilon** : _Float_



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- **mode** : _'ELEMENT'_ in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- **operation** : _'GREATER_THAN'_ in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- Input sockets : a b



## Output sockets



- **result** : _Boolean_



## Data sockets

> Data socket classes implementing this node


- [Color](../sockets/Color.md) [brighter](../sockets/Color.md#brighter) : Method
- [Color](../sockets/Color.md) [darker](../sockets/Color.md#darker) : Method
- [Color](../sockets/Color.md) [equal](../sockets/Color.md#equal) : Method
- [Color](../sockets/Color.md) [not_equal](../sockets/Color.md#not_equal) : Method
- [Float](../sockets/Float.md) [equal](../sockets/Float.md#equal) : Method
- [Float](../sockets/Float.md) [greater_equal](../sockets/Float.md#greater_equal) : Method
- [Float](../sockets/Float.md) [greater_than](../sockets/Float.md#greater_than) : Method
- [Float](../sockets/Float.md) [less_equal](../sockets/Float.md#less_equal) : Method
- [Float](../sockets/Float.md) [less_than](../sockets/Float.md#less_than) : Method
- [Float](../sockets/Float.md) [not_equal](../sockets/Float.md#not_equal) : Method
- [Integer](../sockets/Integer.md) [equal](../sockets/Integer.md#equal) : Method
- [Integer](../sockets/Integer.md) [greater_equal](../sockets/Integer.md#greater_equal) : Method
- [Integer](../sockets/Integer.md) [greater_than](../sockets/Integer.md#greater_than) : Method
- [Integer](../sockets/Integer.md) [less_equal](../sockets/Integer.md#less_equal) : Method
- [Integer](../sockets/Integer.md) [less_than](../sockets/Integer.md#less_than) : Method
- [Integer](../sockets/Integer.md) [not_equal](../sockets/Integer.md#not_equal) : Method
- [String](../sockets/String.md) [average](../sockets/String.md#average) : Method
- [String](../sockets/String.md) [direction](../sockets/String.md#direction) : Method
- [String](../sockets/String.md) [dot_product](../sockets/String.md#dot_product) : Method
- [String](../sockets/String.md) [element](../sockets/String.md#element) : Method
- [String](../sockets/String.md) [length](../sockets/String.md#length) : Method
- [Vector](../sockets/Vector.md) [equal](../sockets/Vector.md#equal) : Method
- [Vector](../sockets/Vector.md) [greater_equal](../sockets/Vector.md#greater_equal) : Method
- [Vector](../sockets/Vector.md) [greater_than](../sockets/Vector.md#greater_than) : Method
- [Vector](../sockets/Vector.md) [less_equal](../sockets/Vector.md#less_equal) : Method
- [Vector](../sockets/Vector.md) [less_than](../sockets/Vector.md#less_than) : Method
- [Vector](../sockets/Vector.md) [not_equal](../sockets/Vector.md#not_equal) : Method
- [functions](../sockets/functions.md) [compare](../sockets/functions.md#compare) : Function


