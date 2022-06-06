
# Class DeleteGeometry

> Geometry node name: _'Delete Geometry'_<br>Blender type:  **GeometryNodeDeleteGeometry**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL', label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_
- **selection** : _Boolean_



#### Parameters



- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- **mode** : _'ALL'_ in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **geometry** : _Geometry_



## Data sockets

> Data socket classes implementing this node




- [Geometry](../sockets/Geometry.md) [delete_geometry](../sockets/Geometry.md#delete_geometry) : Stacked method


