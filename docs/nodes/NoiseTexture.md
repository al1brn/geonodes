
# Class NoiseTexture

> Geometry node name: _'Noise Texture'_<br>Blender type:  **ShaderNodeTexNoise**

## Initialization


```python
from geonodes import nodes
node = nodes.NoiseTexture(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **w** : _Float_
- **scale** : _Float_
- **detail** : _Float_
- **roughness** : _Float_
- **distortion** : _Float_



#### Parameters



- **noise_dimensions** : _'3D'_ in ('1D', '2D', '3D', '4D')



#### Node label



- **label** : Geometry node label



## Output sockets



- **fac** : _Float_
- **color** : _Color_



## Data sockets

> Data socket classes implementing this node


- [Texture](./sockets/Texture.md) [Noise](./sockets/Texture.md#noise) : Static method


