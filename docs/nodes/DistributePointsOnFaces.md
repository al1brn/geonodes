
# Class DistributePointsOnFaces

> Geometry node name: _'Distribute Points on Faces'_<br>Blender type:  **GeometryNodeDistributePointsOnFaces**

## Initialization


```python
from geonodes import nodes
node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None)
```


### Arguments


#### Input sockets



- **mesh** : _Mesh_
- **selection** : _Boolean_
- **distance_min** : _Float_
- **density_max** : _Float_
- **density** : _Float_
- **density_factor** : _Float_
- **seed** : _Integer_



#### Parameters



- **distribute_method** : _'RANDOM'_ in ('RANDOM', 'POISSON')



#### Node label



- **label** : Geometry node label



## Output sockets



- **points** : _Points_
- **normal** : _Vector_
- **rotation** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Mesh](aaa). [distribute_points_on_faces](bbb) : Method


