
# Class AlignEulerToVector

> Geometry node name: _'Align Euler to Vector'_<br>Blender type:  **FunctionNodeAlignEulerToVector**

## Initialization


```python
from geonodes import nodes
node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None)
```


### Arguments


#### Input sockets



- **rotation** : _Vector_
- **factor** : _Float_
- **vector** : _Vector_



#### Parameters



- **axis** : _'X'_ in ('X', 'Y', 'Z')
- **pivot_axis** : _'AUTO'_ in ('AUTO', 'X', 'Y', 'Z')



#### Node label



- **label** : Geometry node label



## Output sockets



- **rotation** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Vector](./sockets/Vector.md) [AlignToVector](./sockets/Vector.md#aligntovector) : Constructor
- [Vector](./sockets/Vector.md) [align_to_vector](./sockets/Vector.md#align_to_vector) : Stacked method


