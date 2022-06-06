
# Class FieldAtIndex

> Geometry node name: _'Field at Index'_<br>Blender type:  **GeometryNodeFieldAtIndex**
[Index](/docs/index.md)

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


- [Boolean](../sockets/Boolean.md) [field_at_index](../sockets/Boolean.md#field_at_index) : Method
- [Color](../sockets/Color.md) [field_at_index](../sockets/Color.md#field_at_index) : Method
- [Float](../sockets/Float.md) [field_at_index](../sockets/Float.md#field_at_index) : Method
- [Integer](../sockets/Integer.md) [field_at_index](../sockets/Integer.md#field_at_index) : Method
- [Vector](../sockets/Vector.md) [field_at_index](../sockets/Vector.md#field_at_index) : Method


