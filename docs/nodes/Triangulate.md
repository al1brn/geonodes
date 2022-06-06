
# Class Triangulate

> Geometry node name: _'Triangulate'_<br>Blender type:  **GeometryNodeTriangulate**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None)
```


### Arguments


#### Input sockets



- **mesh** : _Mesh_
- **selection** : _Boolean_
- **minimum_vertices** : _Integer_



#### Parameters



- **ngon_method** : _'BEAUTY'_ in ('BEAUTY', 'CLIP')
- **quad_method** : _'SHORTEST_DIAGONAL'_ in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node




- [Mesh](../sockets/Mesh.md) [triangulate](../sockets/Mesh.md#triangulate) : Stacked method


