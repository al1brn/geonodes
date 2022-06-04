
# Class GradientTexture

> Geometry node name: _'Gradient Texture'_<br>Blender type:  **ShaderNodeTexGradient**

## Initialization


```python
from geonodes import nodes
node = nodes.GradientTexture(vector=None, gradient_type='LINEAR', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_



#### Parameters



- **gradient_type** : _'LINEAR'_ in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')



#### Node label



- **label** : Geometry node label



## Output sockets



- **color** : _Color_
- **fac** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Texture](../sockets/Texture.md) [Gradient](../sockets/Texture.md#gradient) : Static method


