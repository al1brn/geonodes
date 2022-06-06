
# Class DualMesh

> Geometry node name: _'Dual Mesh'_<br>Blender type:  **GeometryNodeDualMesh**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.DualMesh(mesh=None, keep_boundaries=None, label=None)
```


### Arguments


#### Input sockets



- **mesh** : _Mesh_
- **keep_boundaries** : _Boolean_



#### Node label



- **label** : Geometry node label



## Output sockets



- **dual_mesh** : _Geometry_



## Data sockets

> Data socket classes implementing this node


- [Mesh](../sockets/Mesh.md) [dual](../sockets/Mesh.md#dual) : Stacked method


