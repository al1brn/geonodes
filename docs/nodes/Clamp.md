
# Class Clamp

> Geometry node name: _'Clamp'_<br>Blender type:  **ShaderNodeClamp**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX', label=None)
```


### Arguments


#### Input sockets



- **value** : _Float_
- **min** : _Float_
- **max** : _Float_



#### Parameters



- **clamp_type** : _'MINMAX'_ in ('MINMAX', 'RANGE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **result** : _Float_



## Data sockets

> Data socket classes implementing this node




- [Float](../sockets/Float.md) [clamp](../sockets/Float.md#clamp) : Method


