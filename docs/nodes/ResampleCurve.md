
# Node ResampleCurve

> Geometry node name: [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)<br>
  Blender type: [Resample Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT', label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean
- count : Integer
- length : Float

### Parameters

- mode : str (default = 'COUNT') in ('EVALUATED', 'COUNT', 'LENGTH')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
