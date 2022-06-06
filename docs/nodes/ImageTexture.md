
# Class ImageTexture

> Geometry node name: _'Image Texture'_<br>Blender type:  **GeometryNodeImageTexture**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None)
```


### Arguments


#### Input sockets



- **image** : _Image_
- **vector** : _Vector_
- **frame** : _Integer_



#### Parameters



- **extension** : _'REPEAT'_ in ('REPEAT', 'EXTEND', 'CLIP')
- **interpolation** : _'Linear'_ in ('Linear', 'Closest', 'Cubic')



#### Node label



- **label** : Geometry node label



## Output sockets



- **color** : _Color_
- **alpha** : _Float_



## Data sockets

> Data socket classes implementing this node




- [Texture](../sockets/Texture.md) [Image](../sockets/Texture.md#image) : Static method


