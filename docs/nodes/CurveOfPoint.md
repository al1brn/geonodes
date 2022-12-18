
# Node CurveOfPoint

> Geometry node name: [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html)<br>
  Blender type: [Curve of Point](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveOfPoint(point_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- point_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve_index : Integer
- index_in_curve : Integer
