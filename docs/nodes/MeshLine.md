
# Class MeshLine

> Geometry node name: _'Mesh Line'_<br>Blender type:  **GeometryNodeMeshLine**

## Initialization


```python
from geonodes import nodes
node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None)
```


### Arguments


#### Input sockets



- **count** : _Integer_
- **resolution** : _Float_
- **start_location** : _Vector_
- **offset** : _Vector_



#### Parameters



- **count_mode** : _'TOTAL'_ in ('TOTAL', 'RESOLUTION')
- **mode** : _'OFFSET'_ in ('OFFSET', 'END_POINTS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node


- [Mesh](../sockets/Mesh.md) [Line](../sockets/Mesh.md#line) : Constructor


