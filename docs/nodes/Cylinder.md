
# Class Cylinder

> Geometry node name: _'Cylinder'_<br>Blender type:  **GeometryNodeMeshCylinder**

## Initialization


```python
from geonodes import nodes
node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None)
```


### Arguments


#### Input sockets



- **vertices** : _Integer_
- **side_segments** : _Integer_
- **fill_segments** : _Integer_
- **radius** : _Float_
- **depth** : _Float_



#### Parameters



- **fill_type** : _'NGON'_ in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_
- **top** : _Boolean_
- **side** : _Boolean_
- **bottom** : _Boolean_



## Data sockets

> Data socket classes implementing this node


- [Mesh](aaa). [Cylinder](bbb) : Constructor


