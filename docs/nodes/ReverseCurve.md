
# Node ReverseCurve

> Geometry node name: [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/reverse_curve.html)<br>
  Blender type: [Reverse Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ReverseCurve(curve=None, selection=None, label=None)
```



## Arguments


### Input sockets

curve : Curve
- selection : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
[Curve](/docs/sockets/Curve.md).[reverse](/docs/sockets/Curve.md#reverse) : Method

