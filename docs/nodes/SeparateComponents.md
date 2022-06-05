
# Class SeparateComponents

> Geometry node name: _'Separate Components'_<br>Blender type:  **GeometryNodeSeparateComponents**

## Initialization


```python
from geonodes import nodes
node = nodes.SeparateComponents(geometry=None, label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_
- **point_cloud** : _Geometry_
- **curve** : _Curve_
- **volume** : _Volume_
- **instances** : _Instances_



## Data sockets

> Data socket classes implementing this node


- [Geometry](../sockets/Geometry.md) [components](../sockets/Geometry.md#components) : Property
- [Geometry](../sockets/Geometry.md) [curve_component](../sockets/Geometry.md#curve_component) : Property
- [Geometry](../sockets/Geometry.md) [instances_component](../sockets/Geometry.md#instances_component) : Property
- [Geometry](../sockets/Geometry.md) [mesh_component](../sockets/Geometry.md#mesh_component) : Property
- [Geometry](../sockets/Geometry.md) [points_component](../sockets/Geometry.md#points_component) : Property
- [Geometry](../sockets/Geometry.md) [volume_component](../sockets/Geometry.md#volume_component) : Property


