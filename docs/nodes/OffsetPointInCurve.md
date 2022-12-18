
# Node OffsetPointInCurve

> Geometry node name: [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html)<br>
  Blender type: [Offset Point in Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.OffsetPointInCurve(point_index=None, offset=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- point_index : Integer
- offset : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- is_valid_offset : Boolean
- point_index : Integer
