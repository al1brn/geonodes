
# Class FilletCurve

> Geometry node name: _'Fillet Curve'_<br>Blender type:  **GeometryNodeFilletCurve**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **count** : _Integer_
- **radius** : _Float_
- **limit_radius** : _Boolean_



#### Parameters



- **mode** : _'BEZIER'_ in ('BEZIER', 'POLY')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node




- [Curve](../sockets/Curve.md) [fillet](../sockets/Curve.md#fillet) : Stacked method


