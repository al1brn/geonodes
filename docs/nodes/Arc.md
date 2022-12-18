
# Node Arc

> Geometry node name: [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html)<br>
  Blender type: [Arc](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Arc(resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None, node_color=None)
```



## Arguments


### Input sockets

- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector
- radius : Float
- start_angle : Float
- sweep_angle : Float
- offset_angle : Float
- connect_center : Boolean
- invert_arc : Boolean

### Parameters

- mode : str (default = 'RADIUS') in ('POINTS', 'RADIUS')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
- center : Vector
- normal : Vector
- radius : Float
