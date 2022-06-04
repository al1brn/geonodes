
# Class SeparateGeometry

> Geometry node name: _'Separate Geometry'_<br>Blender type:  **GeometryNodeSeparateGeometry**

## Initialization


```python
from geonodes import nodes
node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT', label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_
- **selection** : _Boolean_



#### Parameters



- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **selection** : _Geometry_
- **inverted** : _Geometry_



## Data sockets

> Data socket classes implementing this node


- [Geometry](../sockets/Geometry.md) [components](../sockets/Geometry.md#components) : Method


