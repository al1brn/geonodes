
# Class GeometryProximity

> Geometry node name: _'Geometry Proximity'_<br>Blender type:  **GeometryNodeProximity**

## Initialization


```python
from geonodes import nodes
node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES', label=None)
```


### Arguments


#### Input sockets



- **target** : _Geometry_
- **source_position** : _Vector_



#### Parameters



- **target_element** : _'FACES'_ in ('POINTS', 'EDGES', 'FACES')



#### Node label



- **label** : Geometry node label



## Output sockets



- **position** : _Vector_
- **distance** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Geometry](./sockets/Geometry.md) [proximity](./sockets/Geometry.md#proximity) : Method


