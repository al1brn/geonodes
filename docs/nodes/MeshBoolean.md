
# Class MeshBoolean

> Geometry node name: _'Mesh Boolean'_<br>Blender type:  **GeometryNodeMeshBoolean**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None)
```


### Arguments


#### Input sockets



- **mesh_1** : _Geometry_
- **mesh_2** : * _Geometry_
- **self_intersection** : _Boolean_
- **hole_tolerant** : _Boolean_



#### Parameters



- **operation** : _'DIFFERENCE'_ in ('INTERSECT', 'UNION', 'DIFFERENCE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node


- [Mesh](../sockets/Mesh.md) [difference](../sockets/Mesh.md#difference) : Method
- [Mesh](../sockets/Mesh.md) [intersect](../sockets/Mesh.md#intersect) : Method
- [Mesh](../sockets/Mesh.md) [union](../sockets/Mesh.md#union) : Method


