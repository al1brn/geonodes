
# Class TransferAttribute

> Geometry node name: _'Transfer Attribute'_<br>Blender type:  **GeometryNodeAttributeTransfer**

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


- [Boolean](aaa). [transfer_attribute](bbb) : Method
- [Color](aaa). [transfer_attribute](bbb) : Method
- [Float](aaa). [transfer_attribute](bbb) : Method
- [Geometry](aaa). [transfer_boolean](bbb) : Method
- [Geometry](aaa). [transfer_color](bbb) : Method
- [Geometry](aaa). [transfer_float](bbb) : Method
- [Geometry](aaa). [transfer_integer](bbb) : Method
- [Geometry](aaa). [transfer_vector](bbb) : Method
- [Integer](aaa). [transfer_attribute](bbb) : Method
- [Vector](aaa). [transfer_attribute](bbb) : Method


