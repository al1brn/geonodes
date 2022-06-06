
# Class CaptureAttribute

> Geometry node name: _'Capture Attribute'_<br>Blender type:  **GeometryNodeCaptureAttribute**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.CaptureAttribute(geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_
- **value** : **data_type** dependant



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets : value
- Output sockets : attribute



## Output sockets



- **geometry** : _Geometry_
- **attribute** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node




- [Boolean](../sockets/Boolean.md) [capture_attribute](../sockets/Boolean.md#capture_attribute) : Method
- [Color](../sockets/Color.md) [capture_attribute](../sockets/Color.md#capture_attribute) : Method
- [Float](../sockets/Float.md) [capture_attribute](../sockets/Float.md#capture_attribute) : Method
- [Geometry](../sockets/Geometry.md) [capture_attribute](../sockets/Geometry.md#capture_attribute) : Method
- [Integer](../sockets/Integer.md) [capture_attribute](../sockets/Integer.md#capture_attribute) : Method
- [Vector](../sockets/Vector.md) [capture_attribute](../sockets/Vector.md#capture_attribute) : Method


