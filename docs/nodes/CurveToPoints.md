
# Class CurveToPoints

> Geometry node name: _'Curve to Points'_<br>Blender type:  **GeometryNodeCurveToPoints**

## Initialization


```python
from geonodes import nodes
node = nodes.CurveToPoints(curve=None, count=None, length=None, mode='COUNT', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **count** : _Integer_
- **length** : _Float_



#### Parameters



- **mode** : _'COUNT'_ in ('EVALUATED', 'COUNT', 'LENGTH')



#### Node label



- **label** : Geometry node label



## Output sockets



- **points** : _Points_
- **tangent** : _Vector_
- **normal** : _Vector_
- **rotation** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Curve](./sockets/Curve.md) [to_points](./sockets/Curve.md#to_points) : Method


