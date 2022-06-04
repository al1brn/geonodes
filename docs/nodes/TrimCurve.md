
# Class TrimCurve

> Geometry node name: _'Trim Curve'_<br>Blender type:  **GeometryNodeTrimCurve**

## Initialization


```python
from geonodes import nodes
node = nodes.TrimCurve(curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **start0** : _Float_
- **start1** : _Float_
- **end0** : _Float_
- **end1** : _Float_



#### Parameters



- **mode** : _'FACTOR'_ in ('FACTOR', 'LENGTH')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](./sockets/Curve.md) [trim](./sockets/Curve.md#trim) : Stacked method


