
# Class Compare

> Geometry node name: _'Compare'_<br>Blender type:  **FunctionNodeCompare**

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


- [Color](aaa). [brighter](bbb) : Method
- [Color](aaa). [darker](bbb) : Method
- [Color](aaa). [equal](bbb) : Method
- [Color](aaa). [not_equal](bbb) : Method
- [Float](aaa). [equal](bbb) : Method
- [Float](aaa). [greater_equal](bbb) : Method
- [Float](aaa). [greater_than](bbb) : Method
- [Float](aaa). [less_equal](bbb) : Method
- [Float](aaa). [less_than](bbb) : Method
- [Float](aaa). [not_equal](bbb) : Method
- [Integer](aaa). [equal](bbb) : Method
- [Integer](aaa). [greater_equal](bbb) : Method
- [Integer](aaa). [greater_than](bbb) : Method
- [Integer](aaa). [less_equal](bbb) : Method
- [Integer](aaa). [less_than](bbb) : Method
- [Integer](aaa). [not_equal](bbb) : Method
- [String](aaa). [average](bbb) : Method
- [String](aaa). [direction](bbb) : Method
- [String](aaa). [dot_product](bbb) : Method
- [String](aaa). [element](bbb) : Method
- [String](aaa). [length](bbb) : Method
- [Vector](aaa). [equal](bbb) : Method
- [Vector](aaa). [greater_equal](bbb) : Method
- [Vector](aaa). [greater_than](bbb) : Method
- [Vector](aaa). [less_equal](bbb) : Method
- [Vector](aaa). [less_than](bbb) : Method
- [Vector](aaa). [not_equal](bbb) : Method
- [functions](aaa). [compare](bbb) : Function


