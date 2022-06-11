
# Node SplineParameter

> Geometry node name: [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/spline_parameter.html)<br>
  Blender type: [Spline Parameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SplineParameter(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

factor : Float
- length : Float
- index : Integer

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Spline) [capture_parameter](section:Data socket Spline/capture_parameter) : Capture attribute
- [class_name](section:Data socket Spline) [factor](section:Data socket Spline/factor) : Attribute
- [class_name](section:Data socket Spline) [parameter_index](section:Data socket Spline/parameter_index) : Attribute
- [class_name](section:Data socket Spline) [parameter_length](section:Data socket Spline/parameter_length) : Attribute
  
