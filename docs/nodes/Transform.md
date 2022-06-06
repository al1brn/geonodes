
# Class Transform

> Geometry node name: _'Transform'_<br>Blender type:  **GeometryNodeTransform**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None, label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_
- **translation** : _Vector_
- **rotation** : _Vector_
- **scale** : _Vector_



#### Node label



- **label** : Geometry node label



## Output sockets



- **geometry** : _Geometry_



## Data sockets

> Data socket classes implementing this node




- [Geometry](../sockets/Geometry.md) [transform](../sockets/Geometry.md#transform) : Stacked method


