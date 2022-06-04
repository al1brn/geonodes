
# Class CurveLine

> Geometry node name: _'Curve Line'_<br>Blender type:  **GeometryNodeCurvePrimitiveLine**

## Initialization


```python
from geonodes import nodes
node = nodes.CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS', label=None)
```


### Arguments


#### Input sockets



- **start** : _Vector_
- **end** : _Vector_
- **direction** : _Vector_
- **length** : _Float_



#### Parameters



- **mode** : _'POINTS'_ in ('POINTS', 'DIRECTION')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](./sockets/Curve.md) [Line](./sockets/Curve.md#line) : Constructor


