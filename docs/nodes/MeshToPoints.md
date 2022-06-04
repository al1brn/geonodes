
# Class MeshToPoints

> Geometry node name: _'Mesh to Points'_<br>Blender type:  **GeometryNodeMeshToPoints**

## Initialization


```python
from geonodes import nodes
node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None)
```


### Arguments


#### Input sockets



- **mesh** : _Mesh_
- **selection** : _Boolean_
- **position** : _Vector_
- **radius** : _Float_



#### Parameters



- **mode** : _'VERTICES'_ in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **points** : _Points_



## Data sockets

> Data socket classes implementing this node


- [Mesh](../sockets/Mesh.md) [to_points](../sockets/Mesh.md#to_points) : Method


