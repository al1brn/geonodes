
# Class CurveCircle

> Geometry node name: _'Curve Circle'_<br>Blender type:  **GeometryNodeCurvePrimitiveCircle**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.CurveCircle(resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None)
```


### Arguments


#### Input sockets



- **resolution** : _Integer_
- **point_1** : _Vector_
- **point_2** : _Vector_
- **point_3** : _Vector_
- **radius** : _Float_



#### Parameters



- **mode** : _'RADIUS'_ in ('POINTS', 'RADIUS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_
- **center** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Curve](../sockets/Curve.md) [Circle](../sockets/Curve.md#circle) : Constructor


