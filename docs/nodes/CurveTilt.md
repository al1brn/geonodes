
# Node CurveTilt

> Geometry node name: [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_tilt.html)<br>
  Blender type: [Curve Tilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveTilt(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

tilt : Float

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Spline.md) [capture_tilt](/docs/sockets/Spline.md#capture_tilt) : Capture attribute
- [class_name](/docs/sockets/Spline.md) [tilt](/docs/sockets/Spline.md#tilt) : Attribute
  
