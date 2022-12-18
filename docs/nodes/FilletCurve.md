
# Node FilletCurve

> Geometry node name: [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html)<br>
  Blender type: [Fillet Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- count : Integer
- radius : Float
- limit_radius : Boolean

### Parameters

- mode : str (default = 'BEZIER') in ('BEZIER', 'POLY')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
