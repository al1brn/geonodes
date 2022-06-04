
# Class RandomValue

> Geometry node name: _'Random Value'_<br>Blender type:  **FunctionNodeRandomValue**

## Initialization


```python
from geonodes import nodes
node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None)
```


### Arguments


#### Input sockets



- **min** : **data_type** dependant
- **max** : **data_type** dependant
- **probability** : _Float_
- **ID** : _Integer_
- **seed** : _Integer_



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
- Input sockets : min max
- Output sockets : value



## Output sockets



- **value** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node


- [Boolean](aaa). [Random](bbb) : Constructor
- [Float](aaa). [Random](bbb) : Constructor
- [Integer](aaa). [Random](bbb) : Constructor
- [Vector](aaa). [Random](bbb) : Constructor


