
# Class Star

> Geometry node name: _'Star'_<br>Blender type:  **GeometryNodeCurveStar**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None, label=None)
```


### Arguments


#### Input sockets



- **points** : _Integer_
- **inner_radius** : _Float_
- **outer_radius** : _Float_
- **twist** : _Float_



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_
- **outer_points** : _Boolean_



## Data sockets

> Data socket classes implementing this node


- [Curve](../sockets/Curve.md) [Star](../sockets/Curve.md#star) : Constructor


