
# Node CurveLength

> Geometry node name: [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_length.html)<br>
  Blender type: [Curve Length](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveLength(curve=None, label=None)
```



## Arguments


### Input sockets

curve : Curve

### Node label

- label : Geometry node display label (default=None)

## Output sockets

length : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Curve.md) [length](/docs/sockets/Curve.md#length) : Method

