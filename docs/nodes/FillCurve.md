
# Class FillCurve

> Geometry node name: _'Fill Curve'_<br>Blender type:  **GeometryNodeFillCurve**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.FillCurve(curve=None, mode='TRIANGLES', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_



#### Parameters



- **mode** : _'TRIANGLES'_ in ('TRIANGLES', 'NGONS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node


- [Curve](../sockets/Curve.md) [fill](../sockets/Curve.md#fill) : Stacked method


