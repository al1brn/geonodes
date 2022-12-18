
# Node SetCurveNormal

> Geometry node name: [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)<br>
  Blender type: [Set Curve Normal](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetCurveNormal(curve=None, selection=None, mode='MINIMUM_TWIST', label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean

### Parameters

- mode : str (default = 'MINIMUM_TWIST') in ('MINIMUM_TWIST', 'Z_UP')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
