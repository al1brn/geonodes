
# Class Raycast

> Geometry node name: _'Raycast'_<br>Blender type:  **GeometryNodeRaycast**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None)
```


### Arguments


#### Input sockets



- **target_geometry** : _Geometry_
- **attribute** : **data_type** dependant
- **source_position** : _Vector_
- **ray_direction** : _Vector_
- **ray_length** : _Float_



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **mapping** : _'INTERPOLATED'_ in ('INTERPOLATED', 'NEAREST')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets : attribute
- Output sockets : attribute



## Output sockets



- **is_hit** : _Boolean_
- **hit_position** : _Vector_
- **hit_normal** : _Vector_
- **hit_distance** : _Float_
- **attribute** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node




- [Boolean](../sockets/Boolean.md) [raycast](../sockets/Boolean.md#raycast) : Method
- [Color](../sockets/Color.md) [raycast](../sockets/Color.md#raycast) : Method
- [Float](../sockets/Float.md) [raycast](../sockets/Float.md#raycast) : Method
- [Integer](../sockets/Integer.md) [raycast](../sockets/Integer.md#raycast) : Method
- [Vector](../sockets/Vector.md) [raycast](../sockets/Vector.md#raycast) : Method


