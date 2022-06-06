
# Class MeshCircle

> Geometry node name: _'Mesh Circle'_<br>Blender type:  **GeometryNodeMeshCircle**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE', label=None)
```


### Arguments


#### Input sockets



- **vertices** : _Integer_
- **radius** : _Float_



#### Parameters



- **fill_type** : _'NONE'_ in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node


- [Mesh](../sockets/Mesh.md) [Circle](../sockets/Mesh.md#circle) : Constructor


