
# Class WhiteNoiseTexture

> Geometry node name: _'White Noise Texture'_<br>Blender type:  **ShaderNodeTexWhiteNoise**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **w** : _Float_



#### Parameters



- **noise_dimensions** : _'3D'_ in ('1D', '2D', '3D', '4D')



#### Node label



- **label** : Geometry node label



## Output sockets



- **value** : _Float_
- **color** : _Color_



## Data sockets

> Data socket classes implementing this node




- [Texture](../sockets/Texture.md) [WhiteNoise](../sockets/Texture.md#whitenoise) : Static method


