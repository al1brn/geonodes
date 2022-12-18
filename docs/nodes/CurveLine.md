
# Node CurveLine

> Geometry node name: [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html)<br>
  Blender type: [Curve Line](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS', label=None, node_color=None)
```



## Arguments


### Input sockets

- start : Vector
- end : Vector
- direction : Vector
- length : Float

### Parameters

- mode : str (default = 'POINTS') in ('POINTS', 'DIRECTION')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
