
# Class TransferAttribute

> Geometry node name: _'Transfer Attribute'_<br>Blender type:  **GeometryNodeAttributeTransfer**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.TransferAttribute(source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None)
```


### Arguments


#### Input sockets



- **source** : _Geometry_
- **attribute** : **data_type** dependant
- **source_position** : _Vector_
- **index** : _Integer_



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- **mapping** : _'NEAREST_FACE_INTERPOLATED'_ in ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets : attribute
- Output sockets : attribute



## Output sockets



- **attribute** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node




- [Boolean](../sockets/Boolean.md) [transfer_attribute](../sockets/Boolean.md#transfer_attribute) : Method
- [Color](../sockets/Color.md) [transfer_attribute](../sockets/Color.md#transfer_attribute) : Method
- [Float](../sockets/Float.md) [transfer_attribute](../sockets/Float.md#transfer_attribute) : Method
- [Geometry](../sockets/Geometry.md) [transfer_boolean](../sockets/Geometry.md#transfer_boolean) : Method
- [Geometry](../sockets/Geometry.md) [transfer_color](../sockets/Geometry.md#transfer_color) : Method
- [Geometry](../sockets/Geometry.md) [transfer_float](../sockets/Geometry.md#transfer_float) : Method
- [Geometry](../sockets/Geometry.md) [transfer_integer](../sockets/Geometry.md#transfer_integer) : Method
- [Geometry](../sockets/Geometry.md) [transfer_vector](../sockets/Geometry.md#transfer_vector) : Method
- [Integer](../sockets/Integer.md) [transfer_attribute](../sockets/Integer.md#transfer_attribute) : Method
- [Vector](../sockets/Vector.md) [transfer_attribute](../sockets/Vector.md#transfer_attribute) : Method


