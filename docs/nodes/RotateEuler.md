
# Class RotateEuler

> Geometry node name: _'Rotate Euler'_<br>Blender type:  **FunctionNodeRotateEuler**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None)
```


### Arguments


#### Input sockets



- **rotation** : _Vector_
- **rotate_by** : _Vector_
- **axis** : _Vector_
- **angle** : _Float_



#### Parameters



- **space** : _'OBJECT'_ in ('OBJECT', 'LOCAL')



#### Node label



- **label** : Geometry node label



## Output sockets



- **rotation** : _Vector_



## Data sockets

> Data socket classes implementing this node




- [Vector](../sockets/Vector.md) [rotate_euler](../sockets/Vector.md#rotate_euler) : Stacked method


