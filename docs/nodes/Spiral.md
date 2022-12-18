
# Node Spiral

> Geometry node name: [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html)<br>
  Blender type: [Spiral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- resolution : Integer
- rotations : Float
- start_radius : Float
- end_radius : Float
- height : Float
- reverse : Boolean

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
