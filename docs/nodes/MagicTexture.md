
# Class MagicTexture

> Geometry node name: _'Magic Texture'_<br>Blender type:  **ShaderNodeTexMagic**

## Initialization


```python
from geonodes import nodes
node = nodes.MagicTexture(vector=None, scale=None, distortion=None, turbulence_depth=2, label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **scale** : _Float_
- **distortion** : _Float_



#### Parameters



- **turbulence_depth** : _2_ int



#### Node label



- **label** : Geometry node label



## Output sockets



- **color** : _Color_
- **fac** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Texture](../sockets/Texture.md) [Magic](../sockets/Texture.md#magic) : Static method


