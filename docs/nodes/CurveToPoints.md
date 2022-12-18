
# Node CurveToPoints

> Geometry node name: [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html)<br>
  Blender type: [Curve to Points](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveToPoints(curve=None, count=None, length=None, mode='COUNT', label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- count : Integer
- length : Float

### Parameters

- mode : str (default = 'COUNT') in ('EVALUATED', 'COUNT', 'LENGTH')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- points : Points
- tangent : Vector
- normal : Vector
- rotation : Vector
