
# Node TrimCurve

> Geometry node name: [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html)<br>
  Blender type: [Trim Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.TrimCurve(curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- start0 : Float
- start1 : Float
- end0 : Float
- end1 : Float

### Parameters

- mode : str (default = 'FACTOR') in ('FACTOR', 'LENGTH')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
