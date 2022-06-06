
# Class DomainSize

> Geometry node name: _'Domain Size'_<br>Blender type:  **GeometryNodeAttributeDomainSize**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.DomainSize(geometry=None, component='MESH', label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_



#### Parameters



- **component** : _'MESH'_ in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')



#### Node label



- **label** : Geometry node label



## Output sockets



- **point_count** : _Integer_
- **edge_count** : _Integer_
- **face_count** : _Integer_
- **face_corner_count** : _Integer_
- **spline_count** : _Integer_
- **instance_count** : _Integer_



## Data sockets

> Data socket classes implementing this node


- [Geometry](../sockets/Geometry.md) [attribute_domain_size](../sockets/Geometry.md#attribute_domain_size) : Method


