
# Class SetSplineType

> Geometry node name: _'Set Spline Type'_<br>Blender type:  **GeometryNodeCurveSplineType**

## Initialization


```python
from geonodes import nodes
node = nodes.SetSplineType(curve=None, selection=None, spline_type='POLY', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **selection** : _Boolean_



#### Parameters



- **spline_type** : _'POLY'_ in ('BEZIER', 'NURBS', 'POLY')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](aaa). [set_spline_type](bbb) : Stacked method


