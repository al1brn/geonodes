
# Class Quadrilateral

> Geometry node name: _'Quadrilateral'_<br>Blender type:  **GeometryNodeCurvePrimitiveQuadrilateral**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.Quadrilateral(width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None)
```


### Arguments


#### Input sockets



- **width** : _Float_
- **height** : _Float_
- **bottom_width** : _Float_
- **top_width** : _Float_
- **offset** : _Float_
- **bottom_height** : _Float_
- **top_height** : _Float_
- **point_1** : _Vector_
- **point_2** : _Vector_
- **point_3** : _Vector_
- **point_4** : _Vector_



#### Parameters



- **mode** : _'RECTANGLE'_ in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](../sockets/Curve.md) [Quadrilateral](../sockets/Curve.md#quadrilateral) : Constructor


