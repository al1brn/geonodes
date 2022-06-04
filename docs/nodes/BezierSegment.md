
# Class BezierSegment

> Geometry node name: _'Bezier Segment'_<br>Blender type:  **GeometryNodeCurvePrimitiveBezierSegment**

## Initialization


```python
from geonodes import nodes
node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None)
```


### Arguments


#### Input sockets



- **resolution** : _Integer_
- **start** : _Vector_
- **start_handle** : _Vector_
- **end_handle** : _Vector_
- **end** : _Vector_



#### Parameters



- **mode** : _'POSITION'_ in ('POSITION', 'OFFSET')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](../sockets/Curve.md) [BezierSegment](../sockets/Curve.md#beziersegment) : Constructor


