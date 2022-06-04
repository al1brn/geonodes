
# Class ResampleCurve

> Geometry node name: _'Resample Curve'_<br>Blender type:  **GeometryNodeResampleCurve**

## Initialization


```python
from geonodes import nodes
node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **selection** : _Boolean_
- **count** : _Integer_
- **length** : _Float_



#### Parameters



- **mode** : _'COUNT'_ in ('EVALUATED', 'COUNT', 'LENGTH')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](./sockets/Curve.md) [resample](./sockets/Curve.md#resample) : Stacked method


