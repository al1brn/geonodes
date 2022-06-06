
# Class Arc

> Geometry node name: _'Arc'_<br>Blender type:  **GeometryNodeCurveArc**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Arc(resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None)
```


### Arguments


#### Input sockets



- **resolution** : _Integer_
- **start** : _Vector_
- **middle** : _Vector_
- **end** : _Vector_
- **radius** : _Float_
- **start_angle** : _Float_
- **sweep_angle** : _Float_
- **offset_angle** : _Float_
- **connect_center** : _Boolean_
- **invert_arc** : _Boolean_



#### Parameters



- **mode** : _'RADIUS'_ in ('POINTS', 'RADIUS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_
- **center** : _Vector_
- **normal** : _Vector_
- **radius** : _Float_



## Data sockets

> Data socket classes implementing this node




- [Curve](../sockets/Curve.md) [ArcFromPoints](../sockets/Curve.md#arcfrompoints) : Static method
- [Curve](../sockets/Curve.md) [ArcFromRadius](../sockets/Curve.md#arcfromradius) : Constructor


