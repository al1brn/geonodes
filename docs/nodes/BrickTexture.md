
# Class BrickTexture

> Geometry node name: _'Brick Texture'_<br>Blender type:  **ShaderNodeTexBrick**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.BrickTexture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None)
```


### Arguments


#### Input sockets



- **vector** : _Vector_
- **color1** : _Color_
- **color2** : _Color_
- **mortar** : _Color_
- **scale** : _Float_
- **mortar_size** : _Float_
- **mortar_smooth** : _Float_
- **bias** : _Float_
- **brick_width** : _Float_
- **row_height** : _Float_



#### Parameters



- **offset** : _0.5_ float
- **offset_frequency** : _2_ int
- **squash** : _1.0_ float
- **squash_frequency** : _2_ int



#### Node label



- **label** : Geometry node label



## Output sockets



- **color** : _Color_
- **fac** : _Float_



## Data sockets

> Data socket classes implementing this node




- [Texture](../sockets/Texture.md) [Brick](../sockets/Texture.md#brick) : Static method


