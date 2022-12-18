
# Node Star

> Geometry node name: [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html)<br>
  Blender type: [Star](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- points : Integer
- inner_radius : Float
- outer_radius : Float
- twist : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
- outer_points : Boolean
