
# Class FieldAtIndex

> Geometry node name: _'Field at Index'_<br>Blender type:  **GeometryNodeFieldAtIndex**

## Initialization


```python
from geonodes import nodes
node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT', label=None)
```


### Arguments


#### Input sockets



- **index** : _Integer_
- **value** : **data_type** dependant



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets : value
- Output sockets : value



## Output sockets



- **value** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node


- [Boolean](aaa). [field_at_index](bbb) : Method
- [Color](aaa). [field_at_index](bbb) : Method
- [Float](aaa). [field_at_index](bbb) : Method
- [Integer](aaa). [field_at_index](bbb) : Method
- [Vector](aaa). [field_at_index](bbb) : Method


