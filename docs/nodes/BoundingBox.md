
# Class BoundingBox

> Geometry node name: _'Bounding Box'_<br>Blender type:  **GeometryNodeBoundBox**

## Initialization


```python
from geonodes import nodes
node = nodes.BoundingBox(geometry=None, label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_



#### Node label



- **label** : Geometry node label



## Output sockets



- **bounding_box** : _Geometry_
- **min** : _Vector_
- **max** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Geometry](../sockets/Geometry.md) [bound_box](../sockets/Geometry.md#bound_box) : Property
- [Geometry](../sockets/Geometry.md) [box](../sockets/Geometry.md#box) : Property
- [Geometry](../sockets/Geometry.md) [box_max](../sockets/Geometry.md#box_max) : Property
- [Geometry](../sockets/Geometry.md) [box_min](../sockets/Geometry.md#box_min) : Property


