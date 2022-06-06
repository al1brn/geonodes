
# Class MapRange

> Geometry node name: _'Map Range'_<br>Blender type:  **ShaderNodeMapRange**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None)
```


### Arguments


#### Input sockets



- **value** : _Float_
- **from_min** : **data_type** dependant
- **from_max** : **data_type** dependant
- **to_min** : **data_type** dependant
- **to_max** : **data_type** dependant
- **steps** : **data_type** dependant
- **vector** : _Vector_



#### Parameters



- **clamp** : _True_ bool
- **data_type** : _'FLOAT'_ in ('FLOAT', 'FLOAT_VECTOR')
- **interpolation_type** : _'LINEAR'_ in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'FLOAT_VECTOR')
- Input sockets : from_min from_max to_min to_max steps



## Output sockets



- **result** : _Float_
- **vector** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Float](../sockets/Float.md) [map_range](../sockets/Float.md#map_range) : Method
- [Vector](../sockets/Vector.md) [map_range](../sockets/Vector.md#map_range) : Method


