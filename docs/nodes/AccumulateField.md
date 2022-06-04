
# Class AccumulateField

> Geometry node name: _'Accumulate Field'_<br>Blender type:  **GeometryNodeAccumulateField**

## Initialization


```python
from geonodes import nodes
node = nodes.AccumulateField(value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None)
```


### Arguments


#### Input sockets



- **value** : **data_type** dependant
- **group_index** : _Integer_



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'FLOAT_VECTOR')
- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'FLOAT_VECTOR')
- Input sockets : value
- Output sockets : leading trailing total



## Output sockets



- **leading** : **data_type** dependant
- **trailing** : **data_type** dependant
- **total** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node


- [Float](./sockets/Float.md) [accumulate_field](./sockets/Float.md#accumulate_field) : Method
- [Integer](./sockets/Integer.md) [accumulate_field](./sockets/Integer.md#accumulate_field) : Method
- [Vector](./sockets/Vector.md) [accumulate_field](./sockets/Vector.md#accumulate_field) : Method


