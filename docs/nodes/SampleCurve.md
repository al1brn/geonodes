
# Class SampleCurve

> Geometry node name: _'Sample Curve'_<br>Blender type:  **GeometryNodeSampleCurve**

## Initialization


```python
from geonodes import nodes
node = nodes.SampleCurve(curve=None, factor=None, length=None, mode='LENGTH', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **factor** : _Float_
- **length** : _Float_



#### Parameters



- **mode** : _'LENGTH'_ in ('FACTOR', 'LENGTH')



#### Node label



- **label** : Geometry node label



## Output sockets



- **position** : _Vector_
- **tangent** : _Vector_
- **normal** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Curve](./sockets/Curve.md) [sample](./sockets/Curve.md#sample) : Method


