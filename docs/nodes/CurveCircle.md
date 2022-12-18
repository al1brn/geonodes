
# Node CurveCircle

> Geometry node name: [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html)<br>
  Blender type: [Curve Circle](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveCircle(resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None, node_color=None)
```



## Arguments


### Input sockets

- resolution : Integer
- point_1 : Vector
- point_2 : Vector
- point_3 : Vector
- radius : Float

### Parameters

- mode : str (default = 'RADIUS') in ('POINTS', 'RADIUS')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
- center : Vector
