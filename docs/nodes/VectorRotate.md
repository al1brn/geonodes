
# Class VectorRotate

> Geometry node name: _'Vector Rotate'_<br>Blender type:  **ShaderNodeVectorRotate**

## Initialization


```python
from geonodes import nodes
node = nodes.VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **center** : _Vector_
- **axis** : _Vector_
- **angle** : _Float_
- **rotation** : _Vector_



#### Parameters



- **invert** : _False_ bool
- **rotation_type** : _'AXIS_ANGLE'_ in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')



#### Node label



- **label** : Geometry node label



## Output sockets



- **vector** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Vector](./sockets/Vector.md) [rotate](./sockets/Vector.md#rotate) : Method


