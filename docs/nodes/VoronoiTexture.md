
# Class VoronoiTexture

> Geometry node name: _'Voronoi Texture'_<br>Blender type:  **ShaderNodeTexVoronoi**

## Initialization


```python
from geonodes import nodes
node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **w** : _Float_
- **scale** : _Float_
- **smoothness** : _Float_
- **exponent** : _Float_
- **randomness** : _Float_



#### Parameters



- **distance** : _'EUCLIDEAN'_ in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- **feature** : _'F1'_ in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **voronoi_dimensions** : _'3D'_ in ('1D', '2D', '3D', '4D')



#### Node label



- **label** : Geometry node label



## Output sockets



- **distance** : _Float_
- **color** : _Color_
- **position** : _Vector_
- **w** : _Float_
- **radius** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Texture](aaa). [Voronoi](bbb) : Static method


