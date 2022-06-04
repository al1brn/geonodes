
# Class ExtrudeMesh

> Geometry node name: _'Extrude Mesh'_<br>Blender type:  **GeometryNodeExtrudeMesh**

## Initialization


```python
from geonodes import nodes
node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None)
```


### Arguments


#### Input sockets



- **mesh** : _Mesh_
- **selection** : _Boolean_
- **offset** : _Vector_
- **offset_scale** : _Float_
- **individual** : _Boolean_



#### Parameters



- **mode** : _'FACES'_ in ('VERTICES', 'EDGES', 'FACES')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_
- **top** : _Boolean_
- **side** : _Boolean_



## Data sockets

> Data socket classes implementing this node


- [Mesh](aaa). [extrude](bbb) : Method


