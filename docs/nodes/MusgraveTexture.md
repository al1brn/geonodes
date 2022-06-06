
# Class MusgraveTexture

> Geometry node name: _'Musgrave Texture'_<br>Blender type:  **ShaderNodeTexMusgrave**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **w** : _Float_
- **scale** : _Float_
- **detail** : _Float_
- **dimension** : _Float_
- **lacunarity** : _Float_
- **offset** : _Float_
- **gain** : _Float_



#### Parameters



- **musgrave_dimensions** : _'3D'_ in ('1D', '2D', '3D', '4D')
- **musgrave_type** : _'FBM'_ in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')



#### Node label



- **label** : Geometry node label



## Output sockets



- **fac** : _Float_



## Data sockets

> Data socket classes implementing this node


- [Texture](../sockets/Texture.md) [Musgrave](../sockets/Texture.md#musgrave) : Static method


