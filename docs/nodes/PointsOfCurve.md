
# Node PointsOfCurve

> Geometry node name: [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html)<br>
  Blender type: [Points of Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.PointsOfCurve(curve_index=None, weights=None, sort_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- curve_index : Integer
- weights : Float
- sort_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- point_index : Integer
- total : Integer
