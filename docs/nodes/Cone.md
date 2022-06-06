
# Class Cone

> Geometry node name: _'Cone'_<br>Blender type:  **GeometryNodeMeshCone**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None)
```


### Arguments


#### Input sockets



- **vertices** : _Integer_
- **side_segments** : _Integer_
- **fill_segments** : _Integer_
- **radius_top** : _Float_
- **radius_bottom** : _Float_
- **depth** : _Float_



#### Parameters



- **fill_type** : _'NGON'_ in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_
- **top** : _Boolean_
- **bottom** : _Boolean_
- **side** : _Boolean_



## Data sockets

> Data socket classes implementing this node




- [Mesh](../sockets/Mesh.md) [Cone](../sockets/Mesh.md#cone) : Constructor


